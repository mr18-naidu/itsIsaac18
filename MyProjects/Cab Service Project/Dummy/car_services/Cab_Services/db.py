import mysql.connector as connection
mydb = connection.connect(host = 'localhost',user = 'root' , passwd = 'mysql',database="Car_service")
cursor = mydb.cursor()

create_query1 = """CREATE TABLE if not exists REGION  (REGION_ID INT PRIMARY KEY,REGION_NAME VARCHAR(50),STATE VARCHAR(50))"""
cursor.execute(create_query1)


CREATE_BOOKING_TABLE="""CREATE TABLE if not exists BOOKING (BOOKING_ID INT,CAB_ID VARCHAR(10),TRANSACTION_ID INT,RIDE_DATE date,CONSTRAINT BOOK_ID_PK PRIMARY KEY(BOOKING_ID),CONSTRAINT CAB_ID_FK FOREIGN KEY(CAB_ID) REFERENCES CABS(CAB_ID));"""
cursor.execute(CREATE_BOOKING_TABLE)





for row in df.values:
    data.append(tuple(row))
insert_query = "INSERT INTO BOOKING VALUES(?,?,?,?,?)" 
cursor.executemany(insert_query,data)

select_querry="select * from BOOKING"
rows=cursor.execute(select_querry)
for i in cursor:
    print(i)