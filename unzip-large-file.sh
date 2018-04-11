Would there be a way of decompressing it 'while deleting it'?

This is what you asked for. But it may not be what you really want. Use at your own risk.

If the 420GB file is stored on a filesystem with sparse file and punch hole support (e.g. ext4, xfs, but not ntfs), it would be possible to read a file and free the read blocks using fallocate --punch-hole. However, if the process is cancelled for any reason, there may be no way to recover since all that's left is a half-deleted, half-uncompressed file. Don't attempt it without making another copy of the source file first.

Very rough proof of concept:

# dd if=/dev/urandom bs=1M count=6000 | pigz --fast > urandom.img.gz
6000+0 records in
6000+0 records out
6291456000 bytes (6.3 GB, 5.9 GiB) copied, 52.2806 s, 120 MB/s
# df -h urandom.img.gz 
Filesystem      Size  Used Avail Use% Mounted on
tmpfs           7.9G  6.0G  2.0G  76% /dev/shm
urandom.img.gz file occupies 76% of available space, so it can't be uncompressed directly. Pipe uncompressed result to md5sum so we can verify later:

# gunzip < urandom.img.gz | md5sum
bc5ed6284fd2d2161296363edaea5a6d  -
Uncompress while hole punching: (this is very rough without any error checking whatsoever)

total=$(stat --format='%s' urandom.img.gz) # bytes
total=$((1+$total/1024/1024)) # MiB
for ((offset=0; offset < $total; offset++))
do
    # read block
    dd bs=1M skip=$offset count=1 if=urandom.img.gz 2> /dev/null
    # delete (punch-hole) blocks we read
    fallocate --punch-hole --offset="$offset"MiB --length=1MiB urandom.img.gz
done | gunzip > urandom.img
Result:

# ls -alh *
-rw-r--r-- 1 root root 5.9G Jan 31 15:14 urandom.img
-rw-r--r-- 1 root root 5.9G Jan 31 15:14 urandom.img.gz
# du -hcs *
5.9G    urandom.img
0       urandom.img.gz
5.9G    total
# md5sum urandom.img
bc5ed6284fd2d2161296363edaea5a6d  urandom.img
The checksum matches, the size of the source file reduced from 6GB to 0 while it was uncompressed in place.

But there are so many things that can go wrong... better don't do it at all or if you really have to, at least use a program that does saner error checking. The loop above does not guarantee at all that the data was read and processed before it gets deleted. If dd or gunzip returns an error for any reason, fallocate still happily tosses it... so if you must use this approach better write a saner read-and-eat program.
