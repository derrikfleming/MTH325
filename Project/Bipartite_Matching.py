test1 = ("A","B")
test2 = ("A","B","C","D")

def power(inlist):

  return [[inlist[j] for j in xrange(len(inlist))
if (i&(1<<j))] for i in xrange(1<<len(inlist))]


print power(test2)
