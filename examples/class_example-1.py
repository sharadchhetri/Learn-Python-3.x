# Class example
class scooty:
    def __init__(self,modelname,year):
        self.modelname = modelname
        self.year = year
    def display(self):
        print(self.modelname,',',self.year)

c1 = scooty('Hero Pleasure','2024')
c1.display()