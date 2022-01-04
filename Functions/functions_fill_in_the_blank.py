
def get_user_input():
    """ Function to get user's input """
    verb=str(input('Type a verb:'))
    noun=str(input('Type a noun:'))
    adjective=str(input('Type an adjective:'))
    list=[verb,noun,adjective]
    return list

def fill_in_blanks(list):
    """ Function to fill in the blanks in the story """
    story='I know that John has a {1}, he {0} this. He\'s {2} '.format(list[0],list[1],list[2])
    return story

list=get_user_input()
story=fill_in_blanks(list)
print('{}'.format(story))
