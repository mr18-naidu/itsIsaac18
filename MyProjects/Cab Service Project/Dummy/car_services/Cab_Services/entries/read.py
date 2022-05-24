# import mysql_connector as mc

from multiprocessing import connection
import mysql.connector as conn
import numpy as np

connector = conn.connect(host = 'localhost',user = 'root' , passwd = 'mysql',database="Car_service")
cur = connector.cursor()



import pandas as pd
df = pd.read_csv("BOOKING.csv", parse_dates=["RIDE_DATE"], infer_datetime_format="%d-%m-%Y")

# print(df.head(30))
data = []

for row in df.values:
    # # print(type(row[1]), row[1], float(np.nan))
    # if type(row[1]) != float:
    #     row[1] = None
    data.append((row[0],row[1] if type(row[1]) != float else None ,row[2],row[3],row[4]))
# print(data)

insert_query = "INSERT INTO BOOKING VALUES(%s,%s,%s,%s,%s)" 
cur.executemany(insert_query,data)
connector.commit()
connector.close()
