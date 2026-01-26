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
'''from collections import Counter   #conter stores the character:counts pair in the set. so iterate through that to get the value
user_input = input("Enter a string:")
char_count = Counter(user_input)
# print(char_count) #output - Counter({'a': 2, 't': 2, 'o': 2, 'u': 1, 'm': 1, 'i': 1, 'n': 1}), input - engineering
for char, count in char_count.items():
    print(f"The count of {char} is {count}")'''

#4. Anagram - a word, phrase, or name formed by rearranging the letters of another, such as spar, formed from rasp.
#check whether the two given strings are anagram

'''s1 = input("Enter the string1:").lower()
s2 = input("Enter the string2:").lower()
if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")'''


#5. Find the group of anagrams from a given list of strings
#method 1: using dictionary
'''input_strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
anagram_dict = {}
for string in input_strings:
    sorted_str = ''.join(sorted(string))
    if sorted_str in anagram_dict:
        anagram_dict[sorted_str].append(string)
    else:
        anagram_dict[sorted_str] = [string]

print("Groups of anagrams:")
for group in anagram_dict.values():
    print(group)'''

#method 2: using default dict from collections module
'''from collections import defaultdict
input_strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
anagram_dict = defaultdict(list)
for string in input_strings:
    sorted_str = ''.join(sorted(string))
    anagram_dict[sorted_str].append(string)
print("Groups of anagrams:")
for group in anagram_dict.values():
    print(group)'''

#6. sort the dictionary in descending order by value
input_dict = {'apple': 5, 'banana': 2, 'orange': 8, 'grape': 3}
sorted_dict = dict(sorted(input_dict.items(), key=lambda item: item[1], reverse=True))
print("Dictionary sorted in descending order by value:")
print(sorted_dict)

#without using lambda function
def sort_by_value(item):
    return item[1]
sorted_dict = dict(sorted(input_dict.items(), key=sort_by_value, reverse=True))
print("wihtout lambda function:", sorted_dict)