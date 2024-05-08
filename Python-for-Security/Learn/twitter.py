from bs4 import BeautifulSoup as soupy
import urllib.request
import re

html = urllib.requests.urlopen('https://twitter.com/HussamKhrais').read()
soup = soupy(html, features=""html.parser"")
x = soup.find(""meta"", {""name"":""description""})['content']
filter = re.findall(r'""(.*)""', x)[0]
print(filter)

# ------------ Exercise ------------
1. Create a new twitter account for testing purposes.
2. Tweet your kali IP address and a port number of your choice.
3. From the Windows (Target) machine retrieve the HTML of
https://twitter.com/<YourAccount> and parse the tweet which you have just created.
4. Use our previous persistent reverse TCP shell (which we created in module 2) and instead of hardcoding the IP address of the Kali, make it dynamically changing based on the latest tweet.
5. Verify that the connection to the kali is successful.
