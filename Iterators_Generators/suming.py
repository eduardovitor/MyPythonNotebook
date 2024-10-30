
def summing(n):
    i = 1
    step = 1
    while step <= n:
        yield i
        step += 1
        i += step

for s in summing(5):
    print(s)


