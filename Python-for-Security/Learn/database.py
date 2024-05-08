#---------------------------  Install  ---------------------------
install mariadb-server mariadb
systemctl start mariadb
mysql -u root

#---------------------------  Connection  ---------------------------
pip install mysql-connector-python

import mysql.connector
cnx = mysql.connector.connect(user=’root’, password=’’, host=’127.0.0.1’, database=’learn’)
cursor = cnx.cursor()

#---------------------------  Read  ---------------------------
query = ‘select * from people’
cursor.execute(query)
for (name, age, gender) in cursor
    print (‘%s is a %s and his age is %s’ % (name, age, gender))
cnx.close

#---------------------------  Write  ---------------------------
cursor.execute(‘insert into people values (\‘far\’, \‘f\’, 38)’)
cnx.commit
cnx.close
