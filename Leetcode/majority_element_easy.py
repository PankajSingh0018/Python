def majority_elements(num_list: list[int]):
    dic = {}
    length_of_list = len(num_list)
    list_of_majority_numbers = []

    # Count occurrences of each element
    for item in num_list:
        if item in dic:
            dic[item] += 1
        else:
            dic[item] = 1

    # Check for majority elements
    for key, value in dic.items():
        if value > length_of_list // 2:
            majority_element = key

    return majority_element


# Example usage
result = majority_elements([3, 2, 3])
print(result)  # Output should be [2]
