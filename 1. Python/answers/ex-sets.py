# sets
list(set(list1) & set(list2))

# list comprehension
[x for x in set(list1+list2) if x in list2 and x in list1]

# for loop
new_list = []
for x in list1+list2:
    if x in list1 and x in list2 and x not in new_list:
        new_list.append(x)
new_list
