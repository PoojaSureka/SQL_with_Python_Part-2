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

mycursor.execute("""insert into ineuron.fsds values(789, 'pooja', 'pooja', '2022-11-11' , 'data science', 'fsds'),
(769, 'kumari', 'sureka', '2022-11-11' , 'data science', 'fsds'),
(769, 'rohit', 'sureka', '2022-11-11' , 'data science', 'fsds'),
(769, 'rahul', 'sharma', '2022-11-11' , 'data science', 'fsds'),
(769, 'kumari', 'sinha', '2022-11-11' , 'data science', 'fsds'),
(989, 'pooja', 'kumari', '2022-11-11' , 'data science', 'fsds')""")

mydb.commit()

mycursor.execute('select * from ineuron.fsds')

for i in mycursor:
    print(i)    