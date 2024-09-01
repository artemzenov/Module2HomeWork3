my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
current_index_list = 0

while current_index_list <= (len(my_list) - 1):
    if my_list[current_index_list] > 0:
        print(my_list[current_index_list])
    elif my_list[current_index_list] < 0:
        break
    current_index_list += 1
