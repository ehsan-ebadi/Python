#---------------------------  Iteration  ---------------------------
f = open('/tmp/scores.txt')
for line in f:
    print(line.strip())
    
#---------------------------  read  ---------------------------
f = open('/tmp/scores.txt')
lines = f.readlines()
lines
#[‘12\n’, ‘9\n’, ‘8\n’, ‘1\8n’, ‘20\n’, ‘11\n’, ‘3\n’, ‘3.75\n’, ‘9\n’, ‘9\n’]
for line in lines:
    print(line.strip())
    
#---------------------------  Write  ---------------------------
f = open('/tmp/scores.txt', 'w')
x = 3
f.write(str(x))
f.close()

#---------------------------  CSV  ---------------------------
import csv
from statistics import mean
with open('/tmp/grades.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        name = row[0]
        for grade in row[1:]:
            these_grades.append(int(grade))
        print("average of %10s is %6f" % (name, mean(these_grades0))
