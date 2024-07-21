# Try and Except example 
   
a = ["python2.x", "python3.x", "java"]  
try:   
     for i in range( 4 ):  
        print( "Index:", i,",Elements:",a[i] ) 

# Any error in Try block will be excuted in the Except block.    
except:  
    print ("Index is out of range") 