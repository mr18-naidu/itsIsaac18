import mysql.connector as connection
mydb = connection.connect(host = 'localhost',user = 'root' , passwd = 'mysql',database="Car_service")
cursor = mydb.cursor()

# -- ques -3 find driver which driver has driven most
Q_3="""SELECT * FROM
(SELECT D.DRIVER_NAME,D.DRIVER_ID,COUNT(D.DRIVER_ID),RANK() OVER (ORDER BY COUNT(D.DRIVER_ID) DESC ) AS D_RANK FROM 
CABS C JOIN DRIVER D
ON C.DRIVER_ID=D.DRIVER_ID
JOIN BOOKING B
ON B.CAB_ID=C.CAB_ID
GROUP BY D.DRIVER_ID)A
WHERE D_RANK=1;"""
cursor.execute(Q_3)
print(cursor.fetchall())