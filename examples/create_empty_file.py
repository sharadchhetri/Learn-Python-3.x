# Create an empty file.

file_empty = open("new_file.txt","w")
file_empty.close()

# Write some lines
file_write = open("another_file.txt","w")
file_write.write("This is new line and it is python written.\nWriting another line for testing")
