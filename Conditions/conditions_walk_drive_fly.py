miles=int(input('What distance will you travel (miles)?'))
if miles < 3:
    print('I suggest walking')
elif miles > 3 and miles < 300 :
    print('I suggest driving')
elif miles >= 300:
    print('I suggest flying')
#using indentation of four spaces
