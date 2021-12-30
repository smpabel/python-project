# nested dict
# dict1 = {
#     1:{101:"a",102:"b",103:"c"},
#     2:{104:"d",105:"e",101:"f"}
# }

# for i in dict1:
#     print(i)

# for i in dict1:
#     for j in dict1[i]:
#         print(j,"=",dict1[i][j])
#     print()

# a = {101:"pabel",102:"helal",103:"karim"}
# print(a)
# print(type(a))
# print()

# n = int(input("How many dict u want to input: "))
# for i in range(n):
#     k = int(input("Enter key Id: "))
#     v = input("Enter value: ")
#     a.update({k:v})

# print() 
# print(a)
# print() 

# run = True
# def search():

#     m = int(input("Enter Id for search value: "))
#     for key,value in a.items():
#         global run
#         if m == key:
#             print(m,"value is: ",value)
#         else:
#             print("wrong ID") 
#     run = False  
            

# while run:
#     search()


a =  {101:"pabel",102:"helal",103:"karim"}
n = int(input("How many dict u want to input: "))
for i in range(n):
    k = int(input("Enter key Id: "))
    v = input("Enter value: ")
    a.update({k:v})
id =  int(input("Enter ID for search: "))
print(a[id])
