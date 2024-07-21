import os

if os.path.exists("pythonTest"):
    os.rmdir("pythonTest")
else:
    print('Directory not found, hence rmdir command is not executed')

# get working directory
a = os.getcwd()
print(a)