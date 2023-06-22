
def Union(lst1, lst2):
    final_list = list(set(lst1) | set(lst2))
    return final_list



def Matchmaker(lsttuple, lst):
    final = []

    for str in lst:
        for tuple in lsttuple:
         if str == tuple[0]:
            final.append(tuple[1])


    return final



klist= [(8,99),(9,98),(2,97),(4,55),(7,32),(6,30)]
list=[1,2,3,4,5,6]



print(Matchmaker(klist,list))
