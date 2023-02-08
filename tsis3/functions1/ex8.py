def spy_game(list):
    spy_list=[]
    for x in range(len(list)):
        if list[x]==0 or list[x]==7:
            spy_list.append(list[x])
        else:
            continue
    if spy_list==[0,0,7]:
        return True
    else:
        return False
    

print(spy_game([1,2,4,0,0,7,5])) 
spy_game([1,0,2,4,0,5,7]) 
spy_game([1,7,2,0,4,5,0])

