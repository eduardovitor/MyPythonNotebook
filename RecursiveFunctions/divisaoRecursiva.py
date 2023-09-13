def divisaoRecursiva(a,b): # 2,1
    if a > b:
        if a!=b:
            return 1 + divisaoRecursiva(a-b,b)
        else:
            return 1
    elif a == b:
        return 1
    elif a < b:
        if a!=b:
            return 1 + divisaoRecursiva(b-a,a)
        else:
            return 1
    
res = divisaoRecursiva(2,16)
print(res)