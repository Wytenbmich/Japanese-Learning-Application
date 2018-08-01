
import os
import time
import tkinter as tk
import webbrowser
from tkinter import simpledialog
from tkinter import messagebox
 

#Open pdf
os.startfile("D:\Japanese-Learning-Application\index.html")
#Sets study time limit
timelimit = 20
#Initalises message box windows
application_window = tk.Tk() 
application_window.overrideredirect(1)
application_window.withdraw()
#Loops until study time is finished
while timelimit > 0:
    #Defines it as a metho so that it can be called upon if extra time is needed
    def studytime(timelimit):
        one_minute = timelimit
        one_minute -= 1
        mins = 0
# Only run if the user types in "start"
        # Loop until we reach 20 minutes running
        while mins < timelimit:
            print (">>>>>>>>>>>>>>>>>>>>>", mins)
            # Sleep for a minute
            time.sleep(10)
            # Increment the minute total
            mins += 1
        # Bring up the dialog box here
            if (mins == one_minute):
                messagebox.showinfo("1 Minute Left!!!","1 Minute remaining")

    

    timelimit = int(simpledialog.askstring("Input", "How many more minutes do you need, (0 = finished)?",
        parent=application_window))
    if timelimit>0:
        studytime(timelimit)
    else:
        break

answer = simpledialog.askstring("Input", "What page number are you on?",
                                parent=application_window)
f = open('index.html','w')

message = '''
<!DOCTYPE html>
<html>
<head>
	<title>Japanese Learning</title>
	<link href="./Style.css" type="text/css" rel="stylesheet">
</head>
<body>

<embed src="D:/Japanesefiles/kanjitextbook.pdf#page=''' + answer + '''&zoom=150" width=100% height=1000px />

</body>
</html>


'''

f.write(message)
f.close()







