def plus_one(digit: list[int]) -> list[int]:

    new_num = ""

    for item in digit:
        new_num += str(item)

    final_number = int(new_num) + 1

    res = str(final_number)
    
    li = [int(num) for num in res]
    print(li)

    return final_number


result = plus_one([1,2,3])