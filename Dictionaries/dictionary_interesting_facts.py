dictionary={
'Viktor':'likes to dance', 
'John':'doesn\'t eat bread every day',
'Carl':'Has a motorcycle and doesn\'t like to read',
'Edward':'Doesn\'t like to wait and is a fan of superheros',
'Dayane':'Smokes and gets drunk all the time'
}

for key in dictionary:
   print('{}:{}'.format(key,dictionary[key]))

print('')
alter_key=str(input('Type a key to alter the fact:\n'))
alter_fact=str(input('Type a new fact about this person:\n'))
dictionary[alter_key]=alter_fact
print('Now I want you to add one more person the list\n')
new_key=str(input('Type the person\'s name:\n'))
new_fact=str(input('Type a fact about this person:\n'))
dictionary[new_key]=new_fact
print('')
for key in dictionary:
   print('{}:{}'.format(key,dictionary[key]))



