
#---------------------------  Define  ---------------------------
farsi2english = dict()
farsi2english[‘salam’] = ‘hi’
farsi2english[‘khodahafez’] = ‘bye’
farsi2english
#{‘salam’: ‘hi’, ‘khodahafez’: ‘bye’}

ghad = {‘jadi’: 180, ‘hasan’: 200, ‘zahra’: 167}
ghad[‘jadi’]
#180
ghad.get(‘jadi’)
#180
ghad.keys()
#dict_keys([‘zahra’, ‘jadi’, ‘hasan’]) 
list(ghad.keys())
#[‘zahra’, ‘jadi’, ‘hasan’]
ghad.values()
#dict_values([167, 180, 200])
list(ghad.values)
#[167, 180, 200]

#---------------------------  Example  ---------------------------
string = 'salam. Jadi is here and testing python for fun'
counter = dict()
for letter in string:
  if letter in counter:
    counter[letter] +=1
	else:
    counter[letter] = 1
for this_one in list(counter.keys()):
	print('%s appeared %s times' % (this_one, counter[this_one]))"
  
#---------------------------  Example  ---------------------------
for letter in string:
  counter[letter] = counter.get(letter, 0) + 1
for this_one in list(counter.keys()):
  print('%s appeared %s times' % (this_one, counter[this_one]))"
