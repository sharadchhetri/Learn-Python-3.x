import mysql.connector

##  GRANT ALL ON *.* to 'root'@'192.168.4.1' IDENTIFIED BY '123456' WITH GRANT OPTION; ##


try:
    myconn = mysql.connector.connect(host = "192.168.4.3", user = "root", passwd = "123456")

    #creating the cursor object  
    cur = myconn.cursor()

    cur.execute("DROP DATABASE IF EXISTS Test123")
    dbs = cur.execute("show databases")

except:
    # This will rollback means undoing all data changes from the current transaction
    myconn.rollback()
    print('Not able to connect to MySQL Server')

# List databases
for i in cur:
    print(i)

myconn.close() 