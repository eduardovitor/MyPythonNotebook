
from functools import reduce

def sum(numbers):
    return reduce(lambda x,y: x+y, numbers)

def mult(numbers):
    return reduce(lambda x,y: x*y, numbers)

def sum_mult(numbers):
    return sum(numbers) + mult(numbers)
    

if __name__ == "__main__":
    nums = [1,2,3,4,5,6]
    print(sum_mult(nums))