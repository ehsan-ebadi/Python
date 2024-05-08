
#---------------------------  Seprate  ---------------------------
l=[4, 5, 9, -1, 1.5, ‘jadi’]
l[0]
#4
l[:4]
#[4, 5, 9, -1]
l[-2]
#1.5

#---------------------------  Iteration  ---------------------------
l2 = [l, 5, [1, 2]]
l2
#[[4, 5, 9, -1, 1.5, ‘jadi’], 5, [1, 2]]

for i in range(0, len(l2)):
    Print (l2[i])
#[4, 5, 9, -1, 1.5, ‘jadi’]
#5
#[1, 2]

#---------------------------  Change  ---------------------------
l[0] = 8
#[8, 5, 9, -1, 1.5, ‘jadi’]

#---------------------------  Operator  ---------------------------
l1 = [1, 2]
l2 = [‘jadi’, ‘naghi’]
l1 + l2
#[1, 2, ‘jadi’, ‘naghi’]

#---------------------------  Method  ---------------------------
l1.append(‘new’)
l1
#[1, 2, ‘new’]

l1.extend([5, 6, 7])
l1
#[1, 2, 'new', 5, 6, 7]

del l1[2]
l1 
#[1, 2, 5, 6, 7]

l1.sort()
l1
#[1, 2, 5, 6, 7]

l1.pop()
#7
l1
#[1, 2, 5, 6]

sum(l1) / len(l1)
#3.5

l1.remove(2)
l1
#[1, 5, 6]

#---------------------------  Convert  ---------------------------
s = ‘some words are here’
s.split(‘a’)
#[‘some words ’, ‘re here’]
list_of_words = s.split()
list_of_words
#[‘some’, ‘words’, ‘are’, ‘here’]

"‘-’.join(list_of_words)
#‘some-words-are-here’

l2
#[‘jadi’, ‘naghi’]
‘bachasboon’.join(l2)
#‘jadibechasboonnaghi’

