import mysql.connector as connection
mydb = connection.connect(host = 'localhost',user = 'root' , passwd = 'mysql',database="Car_service")
cursor = mydb.cursor()

# -- ques-4 prove that there are 3 types of cabs with min count of 2 each in each area of north bangalore
Q_4="""SELECT A.AREA_ID,COUNT(*),CAR_TYPE_ID FROM REGION R JOIN AREA A ON 
R.REGION_ID=A.REGION_ID
JOIN CABS C ON
C.AREA_ID=A.AREA_ID
WHERE R.REGION_NAME='North_Bengaluru'
GROUP BY A.AREA_ID,CAR_TYPE_ID ;"""
cursor.execute(Q_4)
print(cursor.fetchall())