import mysql.connector

## The cursor object is defined as an abstraction specified in the Python DB-API 2.0. It helps us to have multiple separate working environments through the same connection to the database.
  
# #Create the connection object   
# myconn1 = mysql.connector.connect(host = "192.168.4.3", user = "python",passwd = "password", database = 'python')  
  
# #printing the connection object   
# print(myconn1)

try:
    myconn = mysql.connector.connect(host = "192.168.4.3", user = "python", passwd = "password", database = 'python')
    print(myconn)
    print('Able to connect to Database Server')
    #creating the cursor object  
    cur = myconn.cursor()
    print(cur)  

except:
    print('Not able to connect to MySQL Server')