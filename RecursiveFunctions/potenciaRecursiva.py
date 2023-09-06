def potenciaRecursiva(n,k):
    if k > 0:
        return n * potenciaRecursiva(n,k-1)
    return 1

res = potenciaRecursiva(2,12)
print(res)