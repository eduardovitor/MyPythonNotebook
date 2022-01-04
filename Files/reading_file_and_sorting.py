
my_file_path="animals.txt"
mode1='r'
mode2='w'
animals_list=[]
try:
    with open(my_file_path, mode1) as animals_file:
        for line in animals_file:
            animals_list.append(line)
except:
    print('Could not open the file {}'.format(my_file_path))

animals_list.sort()

with open("animals_sorted.txt", mode2) as animals_sorted_file:
    for animal in animals_list:
        animals_sorted_file.write(animal)

