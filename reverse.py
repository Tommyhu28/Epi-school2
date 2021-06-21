def my_reverse(items):
    size = len(items)
    if (size < 1): return None
    my_list = []
    count = 1
    while (count <= size):
        my_list.append(items[-count])
        count += 1
    return print(my_list)



# s_list = [12,11,10,9,8]

# my_reverse(s_list)