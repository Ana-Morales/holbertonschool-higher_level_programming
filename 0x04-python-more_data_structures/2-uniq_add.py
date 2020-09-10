#!/usr/bin/python3
def uniq_add(my_list=[]):
    ans = 0
    for n in set(my_list):
        ans += n
    return ans
