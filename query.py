import mysql.connector
# import mysql.connector
#create user 'user'@'%' identified by 'password'
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
print(mydb)
mycursor = mydb.cursor()

mycursor.execute('select * from ineuron.fsds')

for i in mycursor:
    print(i)

mycursor.execute('select student_id, firstname, class from ineuron.fsds ')

for i in mycursor:
    print(i)

mycursor.execute('select * from ineuron.fsds  where student_id = 989')

for i in mycursor:
    print(i)

mycursor.execute('select * from ineuron.fsds  where student_id > 789')

for i in mycursor:
    print(i)

mycursor.execute('select * from ineuron.fsds  where student_id >= 789')

for i in mycursor:
    print(i)


mycursor.execute("select * from ineuron.fsds  where firstname = 'pooja' and class = 'data science'")

for i in mycursor:
    print(i)

mycursor.execute("select lastname from ineuron.fsds  where firstname = 'pooja' and class = 'data science'")

for i in mycursor:
    print(i)

mycursor.execute("update ineuron.fsds  set firstname = 'roshan' where student_id = 769 ")

mydb.commit()

mycursor.execute("update ineuron.fsds  set class = 'mysql'")

mydb.commit()

mycursor.execute("delete from  ineuron.fsds  where lastname = 'sinha'")

mydb.commit()

mycursor.execute("delete from  ineuron.fsds  where lastname = 'pooja' and firstname = 'pooja'")

mydb.commit()

mycursor.execute("select min(student_id) from ineuron.fsds")

for i in mycursor:
    print(i)

mycursor.execute("select max(student_id) from ineuron.fsds")

for i in mycursor:
    print(i)

mycursor.execute("select count(*) from ineuron.fsds")

for i in mycursor:
    print(i)

mycursor.execute("update ineuron.fsds set class = 'data science' where student_id between 769 and 789")

mydb.commit()

mycursor.execute("update ineuron.fsds set class = 'mongodb' where student_id between 989 and 990")

mydb.commit()

mycursor.execute("select count(*) from ineuron.fsds group by class")

for i in mycursor:
    print(i)

mycursor.execute("select count(*), class from ineuron.fsds group by class")

for i in mycursor:
    print(i)

mycursor.execute("drop table ineuron.fsds")

mydb.commit()


