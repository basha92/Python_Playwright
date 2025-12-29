#set - collection which is unordered, unindexed, and does not allow duplicate values. written in curly braces {}. it is mutable.
#duplicates will be ignored
#myset = {"apple", "banana", "cherry", "apple"}
#print(myset)  # Output: {'banana', 'cherry', 'apple'}

#accessing items - cannot access items by index, but can loop through the set
#for item in myset:
    #print(item)

#length of set
#print(len(myset))  # Output: 3

#check if item exists
#print("banana" in myset)  # Output: True
#print("orange" in myset)  # Output: False 

#adding items - add one item using add(), multiple items using update()
#myset.add("orange")
#print(myset)  # Output: {'banana', 'cherry', 'apple', 'orange'}
#myset.update(["mango", "grape"])
#print(myset)  # Output: {'banana', 'cherry', 'apple', 'orange', 'mango', 'grape'}

#removing items - remove() raises error if item not found, discard() does not
#myset.remove("banana")
#print(myset)  # Output: {'apple', 'cherry'}
#myset.discard("kiwi")  # No error
#print(myset)  # Output: {'apple', 'cherry'}
#popped_item = myset.pop()  # removes and returns an arbitrary item
#print(popped_item) # Output: 'apple' or 'cherry'
#print(myset) # Output: set with one less item``
#myset.remove("abc") # This will raise a KeyError since "abc" is not in the set
#print(myset)

#clear set
#myset.clear()
#print(myset)  # Output: set() - this will clear only values inside the set
#delete set
#del myset
#print(myset)  # This will raise a NameError since myset is deleted

#joining sets - union() or update() - we can mention either set or any iterable (like list, tuple, etc.) or values directly.
#set1 = {"a", "b", "c"}
#set2 = {1, 2, 3}
#union
#set3 = set1.union(set2)
#print(set3)  # Output: {'a', 1, 2, 3, 'b', 'c'} - order can be random, not ordered.
#update
#set1.update(set2)
#print(set1)  # Output: {'a', 1, 2, 3, 'b', 'c'}