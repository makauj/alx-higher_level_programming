#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 and idx > len(myList) - 1:
        return my_list

    new_list = []
    for i in range(len(my_list) - 1):
        if i != idx:
            new_list.append(my_list[i])

    return new_list

