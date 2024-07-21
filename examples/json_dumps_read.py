import json  
# Key:value mapping  
student  = {  
    "Name" : "Peter",  
    "Roll_no" : "0090014",  
    "Grade" : "A",  
    "Age": 20,  
    "Subject": [
        "Computer Graphics", "Discrete Mathematics", "Data Structure"
        ]  
}  

b = json.dumps(student, indent=4)
print(b)