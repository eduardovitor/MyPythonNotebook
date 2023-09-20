def multby(factor): # Using this function, it is possible to generate smaller functions like multiply by two or three
    def mult(num):
        return num * factor
    return mult

twice = multby(2)
three_times = multby(3)

numbers = [1,2,3,4,5]

numbers_twice = list(map(twice,numbers))

print(numbers_twice)

numbers_three_times = list(map(three_times,numbers))

print(numbers_three_times)

