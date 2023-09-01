

l = [7,4,2,8,3,15,29,1,11]

def selection_sort(list_selection):
    for i in range(0,len(list_selection)-1):
        if(list_selection[i]>list_selection[i+1]):
            smallest = list_selection[i+1]
            list_selection[i+1] = list_selection[i]
            list_selection[i] = smallest
        j = i+2
        while(j<len(list_selection)):
            if (list_selection[j]<list_selection[i]):
                prev_smallest = list_selection[i]
                list_selection[i] = list_selection[j]
                list_selection[j] = prev_smallest
            j+=1
    return list_selection
    
res = selection_sort(l)
print(res)