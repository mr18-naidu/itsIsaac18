import mysql.connector as connection
mydb = connection.connect(host = 'localhost',user = 'root' , passwd = 'mysql',database="Car_service")
cursor = mydb.cursor()

# -- ques-6 total no of pick-up points in each region of bangalore
Q_61="select region_id,count(*) as NUM_OF_PICKUP_POINTS from area group by region_id;"

Q_62="""select r.region_name,count(*) as NUM_OF_PICKUP_POINTS from area a join region r
on a.REGION_ID=r.REGION_ID group by a.region_id;"""

cursor.execute(Q_62)
print(cursor.fetchall())