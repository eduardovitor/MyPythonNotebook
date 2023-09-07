def numerosPell(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return (2 * numerosPell(n-1)) + numerosPell(n-2)

res = numerosPell(7)
print(res)