
def pig_speak(text):
    pig_speak=text
    text_length=len(pig_speak)
    print('        {}'.format('_'*text_length))
    print('       <{}>'.format(pig_speak))
    print('        {}'.format('-'*text_length))
    print('       /')
    print('^..^ /')
    print('~((oo)')
    print('" "')

def main():
    text=str(input('Type what the pig said:'))
    text_length=len(text)
    pig_speak(text)

if __name__ == '__main__':
    main()

