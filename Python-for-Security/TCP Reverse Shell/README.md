## Attacker
```netstat -antp | grep 8080```

## Victim
```
Shell> cd*New Folder
Shell> scan 192.168.162.128:21,23,80,8080,8888
```
- With these options:
  - File Transfer
  - Target Directory Navigation
  - Low Level Port Scanner

## Exporting To EXE
```
pip install pyinstaller
pyinstaller -F -w client.py
```

## Dynamic DNS Shell
Register and make a dns record for your public ip

Install the agent on your server to automatically update dns record on noip.com while the ip changed:
```
cd /usr/local/src/
wget http://www.noip.com/client/linux/noip-duc-linux.tar.gz
tar xf noip-duc-linux.tar.gz
cd noip-2.1.9-1/
make install
```

## Exercise 1
- When we hit enter key multiple times our shell breaks due to improper handling of empty string. The simplest way is by adding a new line in our server code saying if the user input was empty string ' ' then we do nothing or we may send a trivial command like "whoami" ????????????????When we hit enter key multiple times our shell breaks due to improper handling of empty string. The simplest way is by adding a new line in our server code saying if the user input was empty string ' ' then we do nothing or we may send a trivial command like "whoami" ????????????????

## Exercise 2
- Update your client and server scripts where you can push a file from the attacker machine down to the target machine.
  - Try to take an advantage of the 'transfer' function 
  - Add a new "if" statement like 'download' 
