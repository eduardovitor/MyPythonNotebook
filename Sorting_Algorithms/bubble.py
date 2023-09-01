

list_bubble = [7,4,2,8,3,15,29,1,11]

def bubbleSort(bubble_list):
    loopActive = True
    while(loopActive):
        changes = 0
        for i in range(0,len(list_bubble)-1):
            if(list_bubble[i]>list_bubble[i+1]):
                greatest = list_bubble[i]
                list_bubble[i] = list_bubble[i+1]
                list_bubble[i+1] = greatest
                changes+=1
            if(i==len(list_bubble)-2):
                if(changes==0):
                    loopActive = False
    return list_bubble

res = bubbleSort(list_bubble)
print(res)