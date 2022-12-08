#!/usr/bin/pythton3

def search_replace(my_list, search, replace):
    result = [number if number != search else replace for number in my_list]
    return result
