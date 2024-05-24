# write a function to count the occurrence of the vowels within a string
def count_vowels(input_string):
    vowels = "aeiou"
    alpha = []
    count = 0
    for char in input_string:
        # print(char)
        if char.isalpha():
            alpha.append(char)

            if char.lower() in vowels:
                # print(char)
                count += 1

    return count


string = "123abce@98o98"
answer = count_vowels(string)
print("Number of vowels in the given string is:", answer)
