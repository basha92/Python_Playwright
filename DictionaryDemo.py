#dictionary - collection which is unordered, changeable and indexed. No duplicate members.Key:value pair. written in curly braces{}
#ordered as of python version 3.7
#creating a dictionary
my_dict={"name":"John","age":30,"city":"New York"}
print(my_dict)

#accessing values
#print("using name key to access the value:", my_dict["name"]) #using key
#print("using get method to get value:", my_dict.get("age")) #using get() method

#changing values
#my_dict["age"]=31
#my_dict.update({"city":"Los Angeles"})
#print("Updated dictionary:", my_dict)

#adding items
#my_dict["job"]="Engineer"
#print("Dictionary after adding job:", my_dict)

#reading the dictionary items using loop
#reading keys
#for key in my_dict:  #this reads only keys
    #print("Key:", key)

#reading values
#for value in my_dict.values():   #this reads onlu values
    #print("Value:", value)

#reading key-value pairs
#for key, value in my_dict.items():
    #print("Key:", key, "Value:", value)

#check if key exists - to access keys just mention the dictionary name or use keys() method
#if "job" in my_dict:
    #print("job exists in the dictionary")
#else:
    #print("job does not exist in the dictionary")

#check if value exists - to access values use values() method
#if 31 in my_dict.values():
    #print("31 exists in the dictionary values")
#else:
    #print("31 does not exist in the dictionary values")

#checking no of items in dictionary
#print("Number of items in the dictionary:", len(my_dict))

#removing items
#my_dict.pop("name")  #removes item with specified key. raise error if key not found
#my_dict.popitem()   #removes last inserted item
#del my_dict["age"]  #removes item with specified key
#my_dict.clear()    #removes all items and returns empty dictionary
#print("Dictionary after removals:", my_dict)

#deleting the dictionary
#del my_dict
#print("Dictionary after deletion:", my_dict)  #this will raise an error as dictionary is deleted


