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

