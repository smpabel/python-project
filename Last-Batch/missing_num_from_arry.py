
def GetMissNum(a):
    n = len(a)
    print("len of a",n)
    total = (n+1)*(n+2)/2
    print("total is",total)
    SumOfa = sum(a)
    print("sum of a",SumOfa)
    return total-SumOfa

a = [1,2,3,5,6]
miss = GetMissNum(a)
print("missing number is ",miss)