#!/usr/bin/pythton3

def search_replace(my_list, search, replace):
    result = [replace if item == search else item for item in my_list]
    return result
