from functools import reduce


numbers = (1,2,3,4,5,6,7,8,9,10) # a immutable tuple
 # The map function receives a function and a list; it applies the function to the list passed
result_plus_two = map(lambda x: x*2, numbers) # Could use a defined function rather than lambda
# apply a function to every iterable cumulatively and returns a single value
final_result = reduce(lambda x,y: x+y, result_plus_two) 
print(final_result)