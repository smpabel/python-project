name = input("Enter file:")
handle = open(name)
file_dict={}
for line in handle:
    if not line.startswith("From "):
        continue
    else:
        line=line.split()
        time=line[5]
        stime=time.split(":")
        hour = stime[:2]
        file_dict[hour]= file_dict.get(hour,0)+1

lst = list()
for k,v in file_dict.items():
    lst.append((k,v))

lst.sort()
for k,v in lst:
    print(k,v)



    