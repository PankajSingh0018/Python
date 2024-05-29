""" Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

"""


def roman_to_integer(num):

    li = [digit for digit in num]
    # print(li)
    # creating a dictionary for roman numerical
    di = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    counter = 0

    for key, value in di.items():
        for item in li:
            if item == key:
                # print(value)
                counter += value

    return counter


num = input("Enter the Roman number you want to convert : ")

result = roman_to_integer(num)

print(f"The Integer Value of the Roman Number is {result}")
