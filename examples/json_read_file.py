import json

with open("test.json","r") as f:
    content = f.read()
    print(content)

print(50 * '-','Another Output',50 * '-')

f = open("test.json","r")
print(f.read())
f.close()