
count=1

with open("file.txt",'r') as file:
    for line in file:
        if line.isspace()==False:
           print('{}: {}'.format(count,line))
           count+=1
