def GetMissNum(a):
    n = len(a)
    print(n)
    total = (n+1)*(n+2)/2
    print(total)
    SumOfa = sum(a)
    print(SumOfa)
    return total-SumOfa





a = [1,2,3,5,6]
miss = GetMissNum(a)
print(miss)