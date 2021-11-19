#Super class
class Phone: 
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price
    
    def full_name(self):
        return f"{self.brand} model:{self.model}"

# Sub Class
class Smart_Phone(Phone):
    def __init__(self,brand,model,price,ram,back_camera):

        # Call super class
        super().__init__(brand,model,price)
        self.ram = ram
        self.back_camera = back_camera

#Multilevel Inheritance
class flagship_Phone(Smart_Phone):
    def __init__(self,brand,model,price,ram,back_camera,front_camera):
        
        super().__init__(brand,model,price,ram,back_camera)
        self.front_camera = front_camera

    #method Overridding 
    def full_name(self):
        return f"{self.brand} model:{self.model} {self.ram} {self.front_camera} {self.back_camera} price: {self.price} "


#obj Define
phn1 =Phone('Nokia','1100',1250)
sphn1 =Smart_Phone('Redmi', 'note7Pro',20000,' 4GB',' 48 Mp')
fphn1 = flagship_Phone('Mi', 'note7Pro',22000,' 6GB',' 48 Mp','16 Mp')

# Obj call
print(phn1.full_name())
print(sphn1.full_name() + " Price:", +sphn1.price)
print(fphn1.full_name())


#list 
l = [(2,1), (3,4), (5,6), (7,8), (9,10)] #list come tuple
 # unpack 
l1, l2 = (zip(*l))
print(type(l1))

l1 = list(l1)
l2 = list(l2)

print(l1)
print(l2)

print(type(l1))
new_list = []

for pair in zip(l1,l2):
    new_list.append(max(pair))
print("New max list",new_list)
