## Attacker
```
python3 httpServer.py
```

## Victim 1
- with these options
  - File Transfer
  - Persistence 
  - Connection attempt error
  - Screen Capturing
  - Searching for Content
```
pip install pillow
```
```
Shell> grab*video.mp4
Shell> screencap
Shell> search C:\*.pdf
```

## Victim 2 (Bypassing Host Based Firewall)
Hijacking Internet Explorer - Shell Over Internet Explorer - Server Side is the same as HTTP Reverse Shell
```
pip install pywin32
```


## Notes
- any interactive commands, will not work in shell such as telnet
- IF the anti-virus (signature based) was able to catch the EXE even before opening it. Then you need to change the packaging method as that would change the signature of the exported EXE  .For example Pyinstaller uses UPX to compress the size of the EXE output. But also many Malwre does use UPX as well. So it's worth to try with  --noupx   Do not use UPX Or even other software to export into EXE
- IF the anti-virus (heuristic based) did catch your exe after opening it. Then this means you need to change the structure or the order of your source code.  Just change the pattern or the behavior of how your code actually works. For example try to Add some random delay,  Add some random operations like create a text file, append random text and then delete the file, Change the order of doing things, Offload some operations/commands to subprocess 

## Exercise
- Fire up Wireshark and monitor the HTTP GET/POST that is going back and forth.
- Use the "follow TCP stream" feature on wireshark and  write down the default value used in Requests user-agent.
- Search on the web for user-agent values for a well known browsers like Chrome, Firefox
- Change the user agent on your HTTP client to make it looks like coming from  Google chrome.
- Run Wireshark again and verify the changes.
