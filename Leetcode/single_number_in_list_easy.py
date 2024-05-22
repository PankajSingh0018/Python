def single_number(number_list: list[int]):
    dic = {}
    count = 1
    for item in number_list:
        if item in dic:
            dic[item] = count + 1

        else:
            dic[item] = count

    for key, value in dic.items():

        if value == 1:

            single_number = key

    return single_number


result = single_number([1, 2, 1, 2, 3, 3, 4])
print(result)
