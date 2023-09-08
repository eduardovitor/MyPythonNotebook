def contagemDigitosRecursiva(n):
    if n < 10:
        return 1
    return 1 + contagemDigitosRecursiva(n/10)

res = contagemDigitosRecursiva(12345)
print(res)