
#---------------------------  Iteration  ---------------------------
a = ‘salam’
for i in range(0, len(a)):
    print(i, a[i])
    
for letter in ‘hi’:
    print(letter)

#---------------------------  Seprate  ---------------------------
s = “man daram miram”
s[4:8]
#daram
s[:-3]
#man daram mi
s = ‘M’ + s[1:]
#Man daram miram


#---------------------------  Existance  ---------------------------
'ad' in ‘jadi’
#True

#---------------------------  Method  ---------------------------
‘jadi’.upper()
#‘JADI’

‘salam jadi’.count(‘a’)
#3

s = ‘hello’
s.startswith(‘h’)
#True

s.find(‘l’)
#2

s.find(‘l’, 3)
#3

‘  srtgsrtshr  ’.strip()
#‘srtgsrtshr’

#---------------------------  Add Variable to String  ---------------------------
name = ‘jadi’
sen = 40
print(‘hello %s chetori? Midooni %s salet shode?’ % (name, sen))
#hello jadi chetori? Midooni 40 salet shode?
