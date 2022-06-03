#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        for i in range(len(my_list)):
            if i == 0:
                mmax = my_list[0]
            else:
                if my_list[i] > mmax:
                    mmax = my_list[i]
    return mmax
