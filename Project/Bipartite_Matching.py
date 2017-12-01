test1 = ("A","B")
test2 = ("A","B","C")

def power(inlist):

  return [[inlist[j] for j in range(len(inlist))
   if (i&(1<<j))] for i in range(1<<len(inlist))]


print (power(test2))



#def partite_sets(graph):
