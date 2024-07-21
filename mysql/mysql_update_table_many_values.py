import mysql.connector  
      
#Create the connection object   
myconn = mysql.connector.connect(host = "192.168.4.3", user = "python", passwd = "password", database = "python") 
  
#creating the cursor object  
cur = myconn.cursor()

sql = "insert into Employee(name, id, salary, dept_id, branch_name) values (%s, %s, %s, %s, %s)"  
val = [("John", 102, 25000.00, 201, "Newyork"),
       ("David",103,25000.00,202,"Port of spain"),
       ("Nick",104,90000.00,201,"Newyork"),
       ("Roger",105,90000.00,201,"California")
       ]  
      
try:  
    #inserting the values into the table  
    cur.executemany(sql,val)
    #commit the transaction   
    myconn.commit()  
    print(cur.rowcount,"records inserted!")  
      
except:  
    myconn.rollback()
    print('Either error from command OR Not able to connect to MySQL Server')

# close the myql connection
myconn.close()