install cntlm:  Cntlm: Fast NTLM Authentication Proxy in C

 

Config cntlm.ini:


Username username

Domain  NAM

Password <passwd>

 

#your proxy from IE LAN settings

Proxy  webproxy.net:8080

Proxy  webproxyp.net:8080

NoProxy  localhost, 127.0.0.*, 10.*, 192.168.*

Listen  3128

 

Allow 127.0.0.1

#your IP

Allow 10.106.18.138

start it:

cntlm -v -c cntlm.ini

 

Now in cmd.exe:

 

pip install --upgrade pip --proxy  127.0.0.1:3128

 

Collecting pip
  Downloading https://files.pythonhosted.
44c8a6e917c1820365cbebcb6a8974d1cd045ab4/

    100% |███████████████████████████████
Installing collected packages: pip
  Found existing installation: pip 9.0.1
    Uninstalling pip-9.0.1:
      Successfully uninstalled pip-9.0.1

Successfully installed pip-10.0.1

 

C:\Users\username\P\Python37-32>

 

works!

 

TODO

Hiding password: https://stormpoopersmith.com/2012/03/20/using-applications-behind-a-corporate-proxy/ 
