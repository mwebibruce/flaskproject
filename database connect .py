import mysql.connector
#INSERT INTO `staff` (`id`, `fullnames`, `dateofbirth`, `specialty`) VALUES (NULL, 'Joyce Wairimu', '2025-05-09', 'othopidic ');
#INSERT INTO `staff` (`id`, `fullnames`, `dateofbirth`, `specialty`) VALUES (NULL, 'Sandra gesare', '2025-05-14', 'oncology nursing
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="nursesheduledb"
)
print(mydb)
mycursor = mydb.cursor()

#mycursor.execute("SHOW DATABASES")

#for x in mycursor:
 # print(x)


  
mycursor.execute("SELECT * FROM staff WHERE fullnames LIKE 'a%';")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

