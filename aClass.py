
# class Bike():
#     honda = 60
#     runner = 80
    
#     def my_bike(self):
#         print(self.honda)
#         print(self.runner)
        
# bike1 = Bike()
# bike1.my_bike()

# bike2 = Bike()
# bike2.my_bike()
        
        
class Numbers():
    def __init__(self, numh,numl):
        self.numh = numh
        self.numl = numl
    
    def getNum(self):
        print(self.numh,self.numl)
    
    def addNum(self):
        print("summation of 2 number is: ", self.numh + self.numl)
               
newNumber = Numbers(50,40)
newNumber.getNum()

newNumber2 = Numbers(500,420)
newNumber2.getNum()

addNumber = Numbers(10,420)
addNumber.addNum()
