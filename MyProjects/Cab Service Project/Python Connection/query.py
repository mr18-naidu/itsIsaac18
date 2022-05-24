import pandas as pd
import mysql.connector as sql
conn = sql.connect(
  host="localhost",
  user="root",
  password="Isaac@18!",
  database ="car_service"
)
mycursor = conn.cursor()
try:
    C_Q1="""CREATE TABLE REGION(
    REGION_ID INT PRIMARY KEY,
    REGION_NAME VARCHAR(50),
    STATE VARCHAR(50)
    );"""
    mycursor.execute(C_Q1)
    conn.commit()
except:
    print("error1")

#AREA TABLE
try:
    C_Q2="""CREATE TABLE AREA(
    AREA_ID VARCHAR(10),
    REGION_ID INT,
    AREA_NAME VARCHAR(255),
    CONSTRAINT AREA_ID_PK PRIMARY KEY (AREA_ID),
    CONSTRAINT AREA_REGION_FK FOREIGN KEY (REGION_ID) REFERENCES REGION(REGION_ID)
    );"""
    mycursor.execute(C_Q2)
    conn.commit()
except:
    print("error2")


#DRIVER
try:
    C_Q3="""CREATE TABLE DRIVER(
    DRIVER_ID VARCHAR(10),
    DRIVER_NAME VARCHAR(255),
    PHONE_NUMBER BIGINT,
    COVID_VACCINATION CHAR(4) CHECK(COVID_VACCINATION ="YES" OR COVID_VACCINATION ="NO"  ),
    DRIVING_LICENSE CHAR(4) CHECK(DRIVING_LICENSE ="YES" OR DRIVING_LICENSE ="NO"  ),
    CONSTRAINT DRIVER_ID_PK PRIMARY KEY (DRIVER_ID)
    );"""
    mycursor.execute(C_Q3)
    conn.commit()
except:
    print("error3")

#CABS
try:
    C_Q4="""CREATE TABLE CABS(
    CAB_ID VARCHAR(10),
    DRIVER_ID VARCHAR(10),
    AREA_ID VARCHAR(10),
    CAR_TYPE_ID INT,
    CONSTRAINT CAB_ID_PK PRIMARY KEY(CAB_ID),
    CONSTRAINT AREA_ID_FK FOREIGN KEY (AREA_ID) REFERENCES  AREA(AREA_ID),
    CONSTRAINT DRIVER_ID_FK FOREIGN KEY (DRIVER_ID) REFERENCES  DRIVER(DRIVER_ID),
    CONSTRAINT CAR_TYPE_FK FOREIGN KEY (CAR_TYPE_ID) REFERENCES  CAR_TYPE(CAR_TYPE_ID)
    );"""
    mycursor.execute(C_Q4)
    conn.commit()
except:
    print("error4")

#CAR_TYPE
try:
    C_Q5="""CREATE TABLE CAR_TYPE(
    CAR_TYPE_ID INT,
    CAR_TYPE VARCHAR(255),
    CONSTRAINT CAR_TYPE_ID_PK PRIMARY KEY(CAR_TYPE_ID)
    );"""
    mycursor.execute(C_Q5)
    conn.commit()
    
except:
    print("error5")

#CUSTOMER_TABLE
try:
    C_Q6="""CREATE TABLE CUSTOMER(
    CUST_ID INT AUTO_INCREMENT,
    CUST_NAME VARCHAR(50),
        CAB_ID VARCHAR(10),
        CONSTRAINT CUST_ID_PK PRIMARY KEY(CUST_ID),
        CONSTRAINT CAB_CUST_FK FOREIGN KEY(CAB_ID) REFERENCES CABS(CAB_ID)
        );"""
    mycursor.execute(C_Q6)
    conn.commit()
except:
    print("error6")
try:
    C_Q7="""CREATE TABLE if not exists BOOKING (BOOKING_ID INT,CAB_ID VARCHAR(10),
      TRANSACTION_ID INT,RIDE_DATE date,
      CONSTRAINT BOOK_ID_PK PRIMARY KEY(BOOKING_ID),
      CONSTRAINT CAB_ID_FK FOREIGN KEY(CAB_ID) REFERENCES CABS(CAB_ID)); """
    mycursor.execute(C_Q6)
    conn.commit()
except:
    print("error7")




df1=pd.read_csv("AREA.csv")
df2=pd.read_csv("BOOKING_TABLE.CSV")
df3=pd.read_csv("CUSTOMER.CSV")
df4=pd.read_csv("REGION.CSV")
df5=pd.read_csv("CAR_TYPE.csv")
df6=pd.read_csv("CABS.CSV")
df7=pd.read_csv("DRIVER.CSV")


data1=[]
for i in df1.values:
    data1.append(i)
insert_querry7="""INSERT INTO AREA VALUES (%s,%s,%s)"""
mycursor.executemany(insert_querry7,data1)
conn.commit()


data2=[]
for row in df2.values:
    data2.append((row[0],row[1] if type(row[1],)!= float else None ,row[2],row[3],row[4]))
insert_querry6="""INSERT INTO BOOKING_TABLE VALUES (%s,%s,%s,%s,%s)"""
mycursor.executemany(insert_querry6,data2)
conn.commit()

data3=[]
for i in df3.values:
    data3.append(i)
insert_querry5="""INSERT INTO CUSTOMER VALUES (%s,%s)"""
mycursor.executemany(insert_querry5,data3)
conn.commit()
    
data4=[]
for i in df4.values:
    data4.append(i)
insert_querry4="""INSERT INTO REGION VALUES (%s,%s,%s)"""
mycursor.executemany(insert_querry4,data4)
conn.commit()

data5=[]
for i in df5.values:
    data5.append(i)
insert_querry3="""INSERT INTO CAR_TYPE VALUES (%s,%s)"""
mycursor.executemany(insert_querry3,data5)
conn.commit()
    
    
data6=[]
for i in df6.values:
    data6.append(i)
insert_querry2="""INSERT INTO CABS VALUES (%s,%s,%s,%s)"""
mycursor.executemany(insert_querry2,data6)
conn.commit()   
    
data7=[]
for i in df7.values:
    data7.append(i)
insert_querry1="""INSERT INTO DRIVER VALUES (%s,%s,%s,%s,%s)"""
mycursor.executemany(insert_querry1,data7)
conn.commit()