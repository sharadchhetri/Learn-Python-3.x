filer = open('test.txt','r')
print(filer.read())
filer.close()

filew = open("test.txt","w")
filew.write("This is new write")
filew.close()

filea = open("test.txt","+a")
filea.write("\nThis is appended line 2 \nThe another line we have added here.\nThere was a forest called Champakvan")
filea.close()

# with open("test.txt",'r') as f:
#     content = f.read();    
#     print(content) 
