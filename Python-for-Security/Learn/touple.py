
#---------------------------  Define  ---------------------------
t = (1, 2, 3)
t[0]
#1
t[0] = 45
#TypeError: ‘tuple’ object does not support item assignment
t = tuple()
t = (0, 1, 2, 3, 4, ‘hello’)
t[1:3]
#(1, 2)

#---------------------------  Seprate  ---------------------------
email = ‘jadi@gmail.com’
emial.split(‘@’)
#[‘jadi’, ‘gmail.com’]

name, domain = email.split(‘@’)
name
#‘jadi’
domain
#‘gmail.com’

#---------------------------  Convert  ---------------------------
vazn = {‘jadi’: 75, ‘sara’: 68, ‘jafar’: 80, ‘mehdi’: 100}
vazn.items()
#dict_items([(‘jadi’: 75), (‘sara’: 68), (‘jafar’: 80), (‘mehdi’: 100)])
list(vazn.items())
#[(‘jadi’: 75), (‘sara’: 68), (‘jafar’: 80), (‘mehdi’: 100)] 
for naem, vazn in list(vazn.items())
    print (‘vazn %s taghriban %s’ % (name, vazn))
