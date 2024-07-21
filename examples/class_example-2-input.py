# Class example

# Declare Variable
modelname = input('Write Scooty Model Name: ')
modelyear = int(input('Year of Scooty Model: '))

# Declare Class
class scooty:
    def __init__(self,modelname,modelyear):
        self.modelname = modelname
        self.modelyear = modelyear
    def display(self):
        print(self.modelname,',',self.modelyear)

# Declare Object
c1 = scooty(modelname, modelyear)

c1.display()