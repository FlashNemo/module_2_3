my_list = ([42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5])
i = 0
while i <= len(my_list):
    list_ind = i
    if  my_list[list_ind] > 0:
        print(my_list[list_ind])
        i = list_ind + 1
    elif my_list[list_ind] == 0:
        i = list_ind + 1
        continue
    else:
        break







