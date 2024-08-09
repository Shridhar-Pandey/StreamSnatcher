import os
from tkinter import *

# Create the main application window
root = Tk()
root.geometry('500x150+400+100')
root.title("YouTube Video Downloader")

# Function to run the batch file
def runit():
    os.startfile('link.bat')

# Function to create and execute the batch file for downloading
def downloadtv():
    with open('link.bat', 'w') as down_load:
        down_load.write(f'youtube-dl {link.get()}')
    runit()

# Create the UI elements
f = Frame(root)
f.grid()
Label(f, text='### YouTube Video Downloader ###', font=("Arial", 15), padx=6).pack()
Label(f, text='').pack()
f1 = Frame(root)
f1.grid()
Label(f1, text='Enter the link here:', font=("Arial", 12)).grid(row=1)
link = StringVar()
Entry(f1, font=("Arial", 12), textvariable=link, width=40).grid(row=1, column=1, pady=5, padx=10)
Button(f1, text='Download', padx=50, relief=RAISED, font=("Arial", 10), borderwidth=5, command=downloadtv).grid(row=2, column=1, pady=10)

# Run the main loop
root.mainloop()
