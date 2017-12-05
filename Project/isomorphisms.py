def is_same(list1, list2):
    is_same = True

    if len(list1) == len(list2):
        for item in list1:
            if item not in list2:
                is_same = False
    else:
        is_same = False
    return is_same

#same size, same order
#list1 = ["A", "B", "C"]
#list2 = ["A", "B", "C"]
#print(is_same(list1,list2)) #True

#same size, different order
#list1 = ["A", "B", "C"]
#list2 = ["B", "C", "A"]
#print(is_same(list1,list2)) #True

#different size, different contents
#list1 = ["A", "B", "C"]
#list2 = ["B", "C", "A", "D"]
#print(is_same(list1,list2)) #False

#same size, different contents
#list1 = ["A", "B", "C"]
#list2 = ["D", "E", "F"]
#print(is_same(list1,list2)) #False

def switch(graph,vert1,vert2):
    temp_g = graph


    for x in list(temp_g):

        for y in temp_g[x]:
            if y == vert2:
                ind = temp_g[x].index(vert2)
                temp_g[x].remove(vert2)
                temp_g[x].insert(ind,vert1)

            elif y == vert1:
                ind = temp_g[x].index(vert1)
                temp_g[x].remove(vert1)
                temp_g[x].insert(ind,vert2)


    x1 = temp_g[vert1]
    x2 = temp_g[vert2]
    for i in temp_g:
        if i == vert1:
            temp_g[vert2] = x1
        elif i == vert2:
            temp_g[vert1] = x2


    return temp_g


#print (switch({"A" : ["B", "C"], "B" : ["A", "D"], "C" : ["A", "D"], "D" : ["B", "C"]}, "A", "C"))



def list_perm(list):

    help_perm(list,0)

def help_perm(list, step = 0):
    if step == len(list):
        print "".join(list)

    for i in range(step, len(list)):

        lst_temp= [character for character in list]
        lst_temp[step], lst_temp[i] = lst_temp[i], lst_temp[step]
        help_perm(lst_temp, step + 1)
list_perm(["A","B","C"])
