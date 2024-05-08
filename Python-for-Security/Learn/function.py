
#---------------------------  Built-in  ---------------------------
type(4.4)
#<class 'float'>

age = '40'
int(age) + 1 = 41

#---------------------------  Library  ---------------------------
import math
math.sin(0.6)

#---------------------------  Define  ---------------------------
def sum(a, b):
    result = a + b
    return result

#---------------------------  Lambda  ---------------------------
myfunc = lambda x: x * 2
myfunc(3)
#6

#---------------------------  map  ---------------------------
mylist = [1, 3, 4, 2, 0.5] 
list(map(lambda x: x*2, mylist))
#[2, 6, 8, 4, 1.0]

numbers = [10, 11, 8, 6, 100, 7, 9, 21]
list(map(lambda x: ‘big’ if x>10 else ‘small’, numbers))
#[‘small’, ‘big’, ‘small’, ‘small’, ‘big’, ‘small’, ‘small’, ‘big’]

#---------------------------  filter  ---------------------------
my_list = [1, 5, 6, 8, 10, 11]
list(filter(lambda x: x % 2 == 0, my_list))
#[6, 8, 10]

#---------------------------  Generator Function Yields  ---------------------------
def firstn():
    yield 1
    yield 2
    yield 3
for i in firstn():
    print (i)
#1
#2
#3

def firstn(n):
    num = 0
    while (num<n):
        yield num
        num += 1
for i in firstn(3):
    print(i)
#1
#2
#3
