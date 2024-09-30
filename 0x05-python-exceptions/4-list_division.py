#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []

    for i in range(list_length):
        try:
            a = my_list_1[i]
            b = my_list_2[1]

            div = a / b
        except IndexError:
            print("out of range")
            div = 0
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("diviso=ion by 0")
            div = 0
        result.append(div)
    return result
