def list_1(input_list):
    insert_pos = 0
    for num in input_list:
        if num != 0:
            input_list[insert_pos] = num
            insert_pos += 1
    for i in range(insert_pos, len(input_list)):
        input_list[i] = 0

    return input_list

print(list_1([0, 1, 0, 12,3]))
print(list_1([0]))
print(list_1([1, 0, 13, 0, 0, 0, 5]))
print(list_1([9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]))