# List is collection which is ordered and changeable. Allows duplicate members.it is written in square brackets.Mutable(can change the existing values)
#creating a list
#my_list = [1, 2, 3, 4, 5]
#my_list2 = ["apple", "banana", "cherry"]
#my_list3 = [1, "hello", 3.14, True]
#my_list4 = []
#print("Original Lists:")
#print(my_list)
#print(my_list2)
#print(my_list3)
#print(my_list4)

# Accessing elements
#print("Accessing elements:")
#print(my_list[0])        # First element
#print(my_list2[1])      # Second element
#print(my_list3[-1])     # Last element
#print(my_list[1:4])     # Slicing
#print(my_list2[:2])     # Slicing from start
#print(my_list3[2:])     # Slicing to end

# Modifying elements
#print(my_list2) #['apple', 'banana', 'cherry']
#my_list2[1] = "blueberry"
#print("After modifying second element:", my_list2) #['apple', 'blueberry', 'cherry']

#read the list using loop
#print("Reading list elements using loop:")
#for item in my_list2:
    #print(item)

#checking if the element is present
#print("Checking if 'banana' is in the list:")
#if "banana" in my_list2:
    #print("Yes, 'banana' is in the list.")
#else:
    #print("No, 'banana' is not in the list.")

#checking length of the list
#print("Length of the list:", len(my_list2))

# Adding elements
#print("Before adding elements:", my_list2)
#my_list2.append("date")  # Adding at the end - ['apple', 'banana', 'cherry', 'date']
#my_list2.insert(1, "date")  # Adding at index 1 - ['apple', 'date', 'banana', 'cherry']
#print("After appending 'date':", my_list2)

#removing elements - pop, remove, del, clear
#print("Before removing elements:", my_list2)
#my_list2.remove("banana")  # Remove by value - ['apple', 'cherry', 'date']
#popped_item = my_list2.pop()  # Remove last item - ['apple', 'cherry']
#print("After removing 'banana':", my_list2)
#print("Popped item:", popped_item)

#remove using del
#print("Before deleting element at index 0:", my_list2) #['apple', 'banana', 'cherry', 'date']
#del my_list2[0]  # Delete by index - ['banana', 'cherry', 'date']
#print("After deleting element at index 0:", my_list2)

# Clearing the entire list
#my_list2.clear()
#print("After clearing the list:", my_list2) # returns empty list []

#copying a list - copy and list()
#print("Original list:", my_list2)
#copied_list = my_list2.copy()
#print("Copied list:", copied_list)
#another_copied_list = list(my_list2)
#print("Another copied list using list():", another_copied_list)

# Joining two lists - + operator and extend(), loop
#print("Joining two lists:")
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
#using + operator
#joined_list = list1 + list2
#print("Using + operator:", joined_list) #['a', 'b', 'c', 1, 2, 3]

#using extend()
#list1.extend(list2)
#print("Using extend():", list1) #['a', 'b', 'c', 1, 2, 3]

#using loop
for item in list2:
    list1.append(item)
print("Using loop to append elements from list2 to list1:", list1) #['a', 'b', 'c', 1, 2, 3]