import json

sample = [{
    "name" : "Rakesh",
    "age" : 12,
    "class" : 6
    },
    {    
    "name" : "Sonu",
    "age" : 11,
    "class" : 6
    }]


with open('new_test.json','w') as j:
    json.dump(sample, j)
