Host dev-snowflake
#HostName 10.69.1.233
 HostName 10.69.1.42
 User abuzunov
 PreferredAuthentications publickey
 IdentityFile ~/.ssh/id_rsa
 ServerAliveInterval 15
 TCPKeepAlive yes
 Protocol 2,1
 LocalForward 10000 localhost:10000
 ProxyCommand ssh dev-bastion -W %h:%p
