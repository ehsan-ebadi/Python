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

