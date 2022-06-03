#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx > len(my_list) - 1:
        return my_list
    else:
        new = []
        for i in range(len(my_list)):
            new.append(my_list[i])
        new[idx] = element
        return new
