def my_range(m,n):
    if (m > n): return None
    my_list = []
    while (m < n):
        my_list.append(m)
        m += 1
    return print(my_list)

# my_range(2,3)