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
list1 = ["A", "B", "C"]
list2 = ["A", "B", "C"]
print(is_same(list1,list2)) #True

#same size, different order
list1 = ["A", "B", "C"]
list2 = ["B", "C", "A"]
print(is_same(list1,list2)) #True

#different size, different contents
list1 = ["A", "B", "C"]
list2 = ["B", "C", "A", "D"]
print(is_same(list1,list2)) #False

#same size, different contents
list1 = ["A", "B", "C"]
list2 = ["D", "E", "F"]
print(is_same(list1,list2)) #False
