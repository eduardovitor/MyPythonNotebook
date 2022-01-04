items_list=[]
while True:
    item=str(input('Type an item to buy: '))
    if len(item)==0:
        break
    items_list.append(item)
print('Your shopping list was:')
for item in items_list:
    print('{}'.format(item))
#Example of range function
"""
animals = ['toad', 'lion', 'seal', 'fox', 'owl', 'whale', 'elk']

for number in range(0, len(animals), 2):

    print(animals[number])

"""
#Concatenating lists
"""
animals = ['toad', 'lion', 'seal']

more_animals = ['fox', 'owl', 'whale']

all_animals = animals + more_animals

print(all_animals)

"""
#Handling exceptions

"""
animals = ['toad', 'lion', 'seal']

try:

    sheep_index = animals.index('sheep')

except:

    sheep_index = 'No sheep found.'

print(sheep_index)

"""
