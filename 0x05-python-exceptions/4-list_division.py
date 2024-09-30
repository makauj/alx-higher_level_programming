#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []

    for i in range(list_length):
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                print("out of range")
                result.append(0)
            else:
                a = my_list_1[i]
                b = my_list_2[i]

                if not isinstance(a, (int, float)):
                    print("wrong type")
                    result.append(0)
                elif not isinstance(b, (int, float)):
                    print("wrong type")
                    result.append(0)
                else:
                    try:
                        division_result = a / b
                        result.append(division_result)
                    except ZeroDivisionError:
                        print("division by 0")
                        result.append(0)
        except Exception:
            print("out of range")
            result.append(0)
    return result
