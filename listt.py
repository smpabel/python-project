lst = [10,20,30,40]
print(lst)
n = int(input("enter how many value do u want "))
for i in range(0,n):
    ele = (input())
    lst.append(ele)
print(lst)
# name = lst[0]
# age = lst[1]
# gpa = lst[2]
# print("name=",name,"age ", age, "GPA= ",gpa)
# lst.insert(1,15)
# print(lst)
lst.pop(-2)
print(lst)
lst.sort()
print(lst)
# print("minimum number is: ", lst[0])
