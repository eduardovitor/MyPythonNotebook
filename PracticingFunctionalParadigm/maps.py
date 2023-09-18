def iterate_map(map_obj):
    try:
        print(next(map_obj))
        iterate_map(map_obj)
    except StopIteration:
        return
    

numbers = (1,2,3,4,5,6,7,8,9,10) # a immutable tuple
 # The map function receives a function and a list; it applies the function to the list passed
result_plus_two = map(lambda x: x*2, numbers) # Could use a defined function rather than lambda
# Iterating over the map object without using for/while
iterate_map(result_plus_two)

