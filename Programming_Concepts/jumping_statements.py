#this file is about the jumping statements like break, continue and pass statements in python
#---break statement---- this will terminate the loop when the specified condition is met
#for i in range(1, 11):
    #if i == 5:
        #break  # when i is 5, the loop will terminate
    #print(i)

#---continue statement---- this will exclude the specified condition and continue the loop
for i in range(1, 11):
    if i == 5 or i == 3 or i == 7:
        continue  # when i is 5, the loop will skip this iteration, won't print 5
    print(i)