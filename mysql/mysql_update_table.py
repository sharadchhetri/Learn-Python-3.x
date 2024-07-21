import mysql.connector  
#Create the connection object   
myconn = mysql.connector.connect(host = "192.168.4.3", user = "python", passwd = "password", database = "python")  
#creating the cursor object  
cur = myconn.cursor()  

sql = "insert into Employee(name, id, salary, dept_id, branch_name) values (%s, %s, %s, %s, %s)"   
val = ("Raj",100, 48000.50, 1001, "New Delhi") 
  
try:  
    cur.execute(sql,val)    
    myconn.commit()
    print(cur.rowcount,"record inserted!")      
except:  
    myconn.rollback()
    print('Either error from command OR Not able to connect to MySQL Server')
myconn.close()