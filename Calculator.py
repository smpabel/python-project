# def add(num1,num2):
#     return num1+num2

# def sub(num1,num2):
#     return num1-num2

# def mul(num1,num2):
#     return num1*num2

# def div(num1,num2):
#     return num1/num2

# print("Select Operation. ")
# print("1 for addition")
# print("2 for Subtraction")
# print("3 for Multiplication")
# print("3 for Divition")

# choose = int(input("Enter your choice. "))
# print("You have enter: ", choose)
 

# num1 = int(input("Enter your first value. "))
# num2 = int(input("Enter your second value. "))


# if choose == 1:
#     print(num1,"+",num2,"= ",add(num1,num2))

# elif choose == 2:
#     print(num1,"-",num2,"= ",sub(num1,num2))
        
# elif choose == 3:
#     print(num1,"*",num2,"= ",mul(num1,num2))
        
# elif choose == 4:
#     print(num1,"/",num2,"= ",div(num1,num2))
# else:
#     print("Invalid input")    



class Numbers():
    def __init__(self, numh,numl):
        self.numh = numh
        self.numl = numl
    
    def showNum(self):
        print(self.numh,self.numl)
    
    def addNum(self):
        print("summation of 2 number is: ", self.numh + self.numl)
    
    def subNum(self):
        print("Substraction of 2 number is: ", self.numh - self.numl)
        
    def mulNum(self):
        print("Multiplication of 2 number is: ", self.numh * self.numl)
    
    def divNum(self):
        print("Division of 2 number is: ", self.numh / self.numl)
               

numh = int(input("Enter your first/high value. "))
numl = int(input("Enter your second/low value. "))
print("You have enter: ", numh, "and ",numl)


Number1 = Numbers(numh,numl)
Number1.showNum()
Number1.addNum()
Number1.subNum()
Number1.mulNum()
Number1.divNum()

     