def is_same(list1, list2):
    is_same = True

    if len(list1) == len(list2):
        for item in list1:
            if item not in list2:
                is_same = False
    else:
        is_same = False

    return is_same


list1 = ["A", "B", "C"]
list2 = ["B", "C", "D"]

print(is_same(list1,list2))
