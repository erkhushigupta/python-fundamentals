#code to generate discount pop ups using GUI, wherein a on running the code a pop up will appear on the user's screen with a
#button Click me! , On clicking the button , the discount code would be visible to the user

# References: I have taken the help of geeksforgeeks to get an idea to make such program

#This program can help increase sales


#Importing tkinter library which  provides Python users with a simple way 
#to create GUI elements using the widgets found in the Tk toolkit. Tk widgets can be used to construct buttons, menus, data fields

#pop ups to give discount codes

import tkinter as tk

def display_message():
    message_label.configure(text="Get Shirts at 90% off using code GET90")

root = tk.Tk()

message_label = tk.Label(root, text="")
message_label.pack()

button = tk.Button(root, text="Click me!", command=display_message)
button.pack()

root.mainloop()


#Input: this program has no input, on running the code a pop upp will appear on the users screen



#Output would give a pop up with a button saying Click me on clicking, the discount code would be displayed