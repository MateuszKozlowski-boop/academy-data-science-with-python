all_num_list = []

for el in my_list:
    if str(el).replace('.','').isdigit():
        all_num_list.append(el)
all_num_list


# How to only count numbers with one decimal point:

all_num_list = []

for el in my_list:
    if str(el).replace('.','').isdigit() and str(el).count('.') < 2:
        all_num_list.append(el)
all_num_list
