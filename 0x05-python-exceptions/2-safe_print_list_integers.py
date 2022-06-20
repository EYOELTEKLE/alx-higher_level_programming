#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    j = 0
    while (j < x):
        try:
            print("{:d}".format(my_list[j]), end='')
        except TypeError:
            j = j + 1
            pass
        except ValueError:
            j = j + 1
            pass
        else:
            count += 1
            j = j + 1

    print()
    return (count)
