#using time module and sleep function

#check the timer is working
#import time
#time.sleep(3)
#print("TIME'S UP")

#print the time in reverse
import time
my_time = int(input("Enter the time in seconds: "))

#adding digital alarm type display in loop
for x in range(my_time, 0, -1):
    seconds = x % 60  # % provides the remainder.
    minutes = int(x/60) % 60 #There are 60 secs in a min
    hours = int(x/3600)  #3600 seconds in an hour
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("TIME'S UP")