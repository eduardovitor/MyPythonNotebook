def seqCollatz(n):
    print("{} ".format(int(n)))
    if n>1:
        if n%2==0:
            return seqCollatz(n/2)
        elif n%2!=0:
            return seqCollatz((n*3)+1)
    elif n<=1:
       return n
    
seq = seqCollatz(7)