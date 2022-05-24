import mysql.connector
conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="******",
  database ="car_service"
)
mycursor = conn.cursor()