import mysql.connector as connection
mydb = connection.connect(host = 'localhost',user = 'root' , passwd = 'mysql',database="Car_service")
cursor = mydb.cursor()

# SELECT * FROM DRIVER;#5
# -- ques-5 num of drivers are given work by future cabs in entire bangalore
Q_52="SELECT COUNT(*) AS NUM_OF_DRIVERS FROM DRIVER ;"

Q_51="SELECT COUNT(*) AS NUM_OF_DRIVERS FROM DRIVER WHERE DRIVING_LICENSE='YES' AND COVID_VACCINATION='YES';"
cursor.execute(Q_51)
print(cursor.fetchall())