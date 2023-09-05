def somaDecimalRecursiva(n):
    if n>1:
        return 1/n + somaDecimalRecursiva(n-1)
    return 1

res = somaDecimalRecursiva(20)
print(res)