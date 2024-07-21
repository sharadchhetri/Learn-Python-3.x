import mysql.connector

myconn = mysql.connector.Connect(host = "192.168.4.3", user = "python", passwd = "password", database = "python")

try:
    # Cursor Object
    cur = myconn.cursor()

    cur.execute("select name,id from Employee")
    result = cur.fetchall()

    for x in result:
        print(x);
except:
    myconn.rollback()
    print("Check Mysql Connection or query")

myconn.close()