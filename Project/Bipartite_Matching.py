test1 = ("A","B")
test2 = ("A","B","C")

def power(inlist):

  return [[inlist[j] for j in range(len(inlist))
   if (i&(1<<j))] for i in range(1<<len(inlist))]


#print (power(test2))



def partite_sets(graph):
    temp_dic = []
    temp_dic2 =[]
    for x in graph:
        for y in graph:
            if graph[x] == graph[y] and x != y:
                temp_dic.append(x)
                temp_dic.append(y)
                print (temp_dic)
                break




partite_sets({"A" : ["B", "C"], "B" : ["A"], "C" : ["A"]})
