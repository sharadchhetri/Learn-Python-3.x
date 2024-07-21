import mysql.connector  
      
#Create the connection object   
myconn = mysql.connector.connect(host = "192.168.4.3", user = "python", passwd = "password", database = "python") 
  
#creating the cursor object  
cur = myconn.cursor()

sql = "delete from Employee where id=105"
      
try:  
    #inserting the values into the table  
    cur.execute(sql)
    #commit the transaction   
    myconn.commit()  
    print(cur.rowcount,"records is removed!")
except:  
    myconn.rollback()
    print('Either error from command OR Not able to connect to MySQL Server')

# close the myql connection
myconn.close()