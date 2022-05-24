# -- ques-1 number of drivers without covid_Certification

import mysql.connector as connection
mydb = connection.connect(host = 'localhost',user = 'root' , passwd = 'mysql',database="Car_service")
cursor = mydb.cursor()


Q_1="SELECT COUNT(*) AS NUM_OF_DRIVERS FROM DRIVER WHERE COVID_VACCINATION='NO'"
cursor.execute(Q_1)
print(cursor.fetchall())





# SELECT * FROM BOOKING;







