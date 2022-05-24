import mysql.connector as connection
mydb = connection.connect(host = 'localhost',user = 'root' , passwd = 'mysql',database="Car_service")
cursor = mydb.cursor()

# -- ques-2rank the companies in order of the number of cabs used by them
Q_2="""SELECT C.CUST_NAME,COUNT(C.CUST_ID) AS NUM_OF_BOOKINGS ,DENSE_RANK() OVER (ORDER BY COUNT(C.CUST_ID) DESC ) AS RANK1 FROM
BOOKING B JOIN CUSTOMER C
ON B.CUST_ID=C.CUST_ID
WHERE B.TRANSACTION_ID IS NOT NULL
GROUP BY C.CUST_NAME;"""
cursor.execute(Q_2)
print(cursor.fetchall())


Q_21="SELECT COUNT(*),CUST_ID FROM BOOKING WHERE TRANSACTION_ID IS NOT NULL GROUP BY CUST_ID;"
Q_22="SELECT COUNT(*),CUST_ID FROM BOOKING WHERE TRANSACTION_ID IS NULL GROUP BY CUST_ID;"
