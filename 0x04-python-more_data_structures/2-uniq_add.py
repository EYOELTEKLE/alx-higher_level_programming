#!/usr/bin/python3
def uniq_add(my_list=[]):
    size = len(my_list)
    ans = 0
    new = []
    for i in range(size):
        if my_list[i] not in new:
            new.append(my_list[i])
            ans = ans + my_list[i]
        else:
            continue
    return ans
