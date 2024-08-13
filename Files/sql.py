import mysql.connector
conn = mysql.connector.connect(
    host="DESKTOP-1BVA85T",
    port="3306",
    password="654321",
    database="ashish")
if conn.is_connected():
    print("haaaa")
c = conn.cursor()
c.execute("show databases;")
for i in c:
    print(i)