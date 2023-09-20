
def par(n):
    if n%2==0:
        return n

def iterateFilter(obj):
    try:
        print(next(obj))
        iterateFilter(obj)
    except StopIteration:
        return   
    
numbers = (1,2,3,4,5,6,7,8,9,10) # a immutable tuple
filtered_numbers = filter(par,numbers) # filter as a high order function
iterateFilter(filtered_numbers)