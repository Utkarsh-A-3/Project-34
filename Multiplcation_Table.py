"""
Introduction to GUI 
Graphical User Interface (GUI) is nothing but a desktop application which helps you to interact with the computers. They perform different tasks on desktops, laptops and other electronic devices. GUI apps like Text-Editors create, read, update and delete different types of files. Apps like Sudoku, Chess and Solitaire are games which you can play. GUI apps like Google Chrome, Firefox and Microsoft Edge browse through the Internet 

from tkinter import *
root = Tk()
root.title("Display Name")
name = Label(text = "Utkarsh")
name.place(x = 300, y = 200)

from tkinter import *
root = Tk()
name = Label(text = "My favorite color is red")
name.place(x = 200, y = 0)

Nidhi wants to create a GUI program using the python Tkinter module. She wants to display the multiplication table of any number on the screen and then show her program to her younger sister. Write the same program as Nidhi and show it to your friends."""

from tkinter import *
root = Tk()
root.title("Multiplication Table")
number = int(input("Number: "))
for i in range(1,11):
    table = Label(text = f"{number} x {i} =  {number * i}")
    table.pack()

root.mainloop()
""" ● Nidhi's younger sister requested her to create a program that can display the multiplication table of all the numbers from 1 to 10 at the same time. Nidhi got stuck and she is not able to create such type of program. Write a python program to help Nidhi.
"""

from tkinter import *
root = Tk()
root.title("Multiplication Table")
for x in range(1,11):
    for y in range(1,11):
        table = Label(text = f"{x} x {y} =  {x * y}")
        table.grid(row = y, column = x)

root.mainloop()