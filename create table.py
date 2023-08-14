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
mycursor.execute('create table ineuron.fsds(student_id int, firstname varchar(50), lastname varchar(60), registration_date DATE, class varchar(20), course_name varchar(50))')