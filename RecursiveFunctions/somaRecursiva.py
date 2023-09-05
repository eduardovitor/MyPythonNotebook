
def somaRecursiva(n):
    if n>=1:
        return n + somaRecursiva(n-1)
    return 0

res = somaRecursiva(50)
print(res)