#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_ls = []
    for i in range(list_length):
        try:
            new_ls.append(my_list_1[i]/my_list_2[i])
        except ZeroDivisionError:
            print("division by 0")
            new_ls.append(0)
            continue
        except (ValueError, TypeError):
            print("wrong type")
            new_ls.append(0)
            continue
        except IndexError:
            print("out of range")
            new_ls.append(0)
            continue
        finally:
            pass
    return new_ls
