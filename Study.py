
import os
import time

os.startfile("D:\Japanese-Learning-Application\index.html")
page_number = input("What page number are you on")
mins = 0
# Only run if the user types in "start"
    # Loop until we reach 20 minutes running
while mins != 20:
    print (">>>>>>>>>>>>>>>>>>>>>", mins)
        # Sleep for a minute
    time.sleep(60)
        # Increment the minute total
    mins += 1
    # Bring up the dialog box here

filename = "./index.html"
file = open(filename, "r")
for line in file:
   print(line)



