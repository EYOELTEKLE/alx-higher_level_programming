#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    ans = []
    message = ''
    message2 = ''
    message3 = ''
    for i in range(0, list_length):
        try:
            ans.append(my_list_1[i] / my_list_2[i])
        except TypeError:
            message = "wrong type"
            ans.append(0)
        except ZeroDivisionError:
            message2 = "division by 0"
            ans.append(0)
        except IndexError:
            message3 = "out of range"
            ans.append(0)
        finally:
            text = 'completion'
    if (message2 != ''):
        print(message2)
    if (message != ''):
        print(message)
    if (message3 != ''):
        print(message3)
    return ans
