# write a function to check get the product of all the numbers present in a string
def product(input_string):
    mul = 1
    for char in input_string:
        # print(char)
        if char.isdigit():
            mul *= int(char)
        else:
            continue
    return mul


string = "123abce@98o98"
answer = product(string)

print(f"The product of all the numbers present in the string is : {answer}")
