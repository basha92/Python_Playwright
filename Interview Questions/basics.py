#1. find the first non repeating character in a string
#solution: get the user input srting, iterate through each character and if the count is not exceeding 1, then return the character.
#method 1: using function.
'''def first_non_repeating_character(s):
    for char in s:
        if s.count(char) == 1:
            return char
    return None

def main():
    user_input = input("Enter a string: ")
    result = first_non_repeating_character(user_input)
    if result:
        print(f"The first non-repeating character is: {result}")
    else:
        print("All characters are repeating.")

if __name__ == "__main__":
    main()'''

#method 2: importing counter from collections module.
'''from collections import Counter
user_input = input("Enter a string:")
char_count = Counter(user_input)
for char in char_count:
    if char_count[char] == 1:
        print(f"the first non repeating character is: {char}")
        break'''

#2: Important and most repeating: check whether the given strign is palindrome - the reverse matches the initial.
'''user_input = input("Enter a string: ")
reverse_input = user_input[::-1]   #slice the string from end
if reverse_input == user_input:
    print("Entered string is palindrome")
else:
    print("It is not palindrome")'''

#3. Count the characters
from collections import Counter   #conter stores the character:counts pair in the set. so iterate through that to get the value
user_input = input("Enter a string:")
char_count = Counter(user_input)
# print(char_count) #output - Counter({'a': 2, 't': 2, 'o': 2, 'u': 1, 'm': 1, 'i': 1, 'n': 1}), input - engineering
for char, count in char_count.items():
    print(f"The count of {char} is {count}")



