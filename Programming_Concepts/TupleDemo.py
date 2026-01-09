#tuple - collection which is ordered and unchangeable. Allows duplicate members.it is written in round brackets.immutable(cannot change the existing values)
#creating a tuple
my_tuple = (1, 2, 3, 4, 5)
#print("Original Tuple:", my_tuple)
#accessing elements
#print("Accessing elements:")
#print(my_tuple[0])        # First element
#print(my_tuple[1:4])     # Slicing
#print(my_tuple[-1])      # Last element
#modifying elements - tuples are immutable, so we cannot modify them directly
#but we can convert to list, modify and convert back to tuple
#my_list = list(my_tuple) #convert to list
#my_list[1] = 20
#my_tuple = tuple(my_list) #convert back to tuple
#print("After modifying second element:", my_tuple)

#reading tuple using loop
#print("Reading tuple elements using loop:")
#for item in my_tuple:
    #print(item)

#checking if the element is present
#print("Checking if 3 is in the tuple:")
#if 3 in my_tuple:
    #print("Yes, 3 is in the tuple.")
#else:
    #print("No, 3 is not in the tuple.")

#checking length of the tuple
#print("Length of the tuple:", len(my_tuple)) #5

#adding elements - tuples are immutable, so we cannot add elements directly
#but we can convert to list, add and convert back to tuple  
#my_list = list(my_tuple) #convert to list
#my_list.append(6)
#my_tuple = tuple(my_list) #convert back to tuple
#print("After adding element 6:", my_tuple) #(1, 2, 3, 4, 5, 6)

#copying a tuple
#copied_tuple = my_tuple
#print("Copied Tuple:", copied_tuple) #Copied Tuple: (1, 2, 3, 4, 5)

#joining two tuples
#tuple1 = ("a", "b", "c")
#tuple2 = (1, 2, 3)
#joined_tuple = tuple1 + tuple2
#print("Joined Tuple:", joined_tuple) #Joined Tuple: ('a', 'b', 'c', 1, 2, 3)

#using loop to join tuples
#for item in tuple2:
    #tuple1 += (item,) #note the comma to make it a tuple
#print("Joined Tuple using loop:", tuple1) #Joined Tuple using loop: ('a', 'b', 'c', 1, 2, 3)

#removing elements - tuples are immutable, so we cannot remove elements directly
#but we can convert to list, remove and convert back to tuple
my_list = list(my_tuple) #convert to list
my_list.remove(2)
my_tuple = tuple(my_list) #convert back to tuple
print("After removing element 2:", my_tuple) #(1, 3, 4, 5)
#clearing the entire tuple - tuples are immutable, so we cannot clear them directly
del my_tuple
print("After clearing the tuple:", my_tuple) # returns empty tuple (); name error though as my_tuple is not defined






