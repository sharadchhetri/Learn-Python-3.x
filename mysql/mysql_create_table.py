import mysql.connector

try:
    myconn = mysql.connector.connect(host = "192.168.4.3", user = "python", passwd = "password", database = "python")

    #creating the cursor object  
    cur = myconn.cursor()
    dbs = cur.execute("create table IF NOT EXISTS Employee(name varchar(20) not null, id int(20) not null primary key, salary float not null, Dept_id int not null)")
    dbs2 = cur.execute("create table IF NOT EXISTS Department(name varchar(20) not null, Dept_id int(20) not null primary key)")
    dbs3 = cur.execute("alter table Employee add branch_name varchar(20) not null")  

except:
    # This will rollback means undoing all data changes from the current transaction
    myconn.rollback()
    print('Either error from command OR Not able to connect to MySQL Server')