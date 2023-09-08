def mdcRecursivo(a,b):
    if a > b:
        return mdcRecursivo(a-b,b)
    elif a < b:
        return mdcRecursivo(b-a,a)
    else:
        return a

res = mdcRecursivo(48,18)
print(res)

