## tkinter 

import tkinter as tk
from tkinter import ttk
"""root = tk.Tk()
root.title("sample")
''' 
widgets are added here
'''
root.mainloop() 

root.destroy() # to close the window"""

# Tkinter Widget
""" 
Label - The Label widget is used to provide a single-line caption for other widgets. It can also contain images.

Button - The Button widget is used to display the buttons in your application.

Entry - The Entry widget is used to display a single-line text field for accepting values from a user.

Text - The Text widget is used to display text in multiple lines.

Radiobutton - The Radiobutton widget is used to display a number of options as radio buttons. The user can select only one option at a time.

Checkbutton - The Checkbutton widget is used to display a number of options as checkboxes. The user can select multiple options at a time.

Combobox – walk you through the steps of creating a combobox widget.

Message - The Message widget is used to display multiline text fields for accepting values from a user.

Frame - The Frame widget is used as a container widget to organize other widgets.

Menu - The Menu widget is used to provide various commands to a user. These commands are contained inside Menubutton.

Menubutton - The Menubutton widget is used to display menus in your application. 

Canvas - The Canvas widget is used to draw shapes, such as lines, ovals, polygons and rectangles, in your application.
"""


# Label
"""from tkinter import *

root = Tk()
root.title("My First GUI")

label = Label(root, text="Hello, World!")
label.pack()

root.mainloop()

# button
import tkinter as tk
r = tk.Tk()
r.title('Counting Seconds')
button = tk.Button(r, text='Stop', width=25, command=r.destroy)
button.pack()
r.mainloop()"""

# Entry
"""from tkinter import *
master = Tk()
Label(master, text='First Name').grid(row=0)
Label(master, text='Last Name').grid(row=1)
e1 = Entry(master)
e2 = Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
mainloop() """

# Text
"""from tkinter import *
root = Tk()
T = Text(root, height=2, width=30)
T.pack()
T.insert(END, 'HI\nBEST WEBSITE\n')
mainloop()"""

# RadioButton
""" from tkinter import *
root = Tk()
v = IntVar()
Radiobutton(root, text='yes', variable=v, value=1).pack(anchor=W)
Radiobutton(root, text='No', variable=v, value=2).pack(anchor=W)
mainloop() """

# CheckButton
""" from tkinter import *
master = Tk()
var1 = IntVar()
Checkbutton(master, text='male', variable=var1).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton(master, text='female', variable=var2).grid(row=1, sticky=W)
mainloop() """

# pack() method
""" import tkinter as tk

root = tk.Tk()
root.title("Pack Example")

# Create three buttons
button1 = tk.Button(root, text="Button 1")
button2 = tk.Button(root, text="Button 2")
button3 = tk.Button(root, text="Button 3")

# Pack the buttons vertically
button1.pack()
button2.pack()
button3.pack()

root.mainloop() """

# grid() method
""" import tkinter as tk

root = tk.Tk()
root.title("Grid Example")

# Create three labels
label1 = tk.Label(root, text="Label 1")
label2 = tk.Label(root, text="Label 2")
label3 = tk.Label(root, text="Label 3")

# Grid the labels in a 2x2 grid
label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=1, column=0, columnspan=2)

root.mainloop() """

# Message
""" from tkinter import *
main = Tk()
ourMessage = 'This is our Message'
messageVar = Message(main, text=ourMessage)
messageVar.config(bg='lightgreen')
messageVar.pack()
main.mainloop() """

# place() method
""" import tkinter as tk

root = tk.Tk()
root.title("Place Example")

# Create a label
label = tk.Label(root, text="Label")

# Place the label at specific coordinates
label.place(x=50, y=50)

root.mainloop() """

## Combobox
""" import tkinter as tk
from tkinter import ttk

def select(event):
    selected_item = combo_box.get()
    label.config(text="Selected Item: " + selected_item)

root = tk.Tk()
root.title("Combobox Example")

label = tk.Label(root, text="Selected Item: ")
label.pack()

combo_box = ttk.Combobox(root, values=["Option 1", "Option 2", "Option 3"], state='readonly')
combo_box.pack()

combo_box.set("Option 1")

combo_box.bind("<<ComboboxSelected>>", select)
root.mainloop() """

# Listbox
""" from tkinter import *
top = Tk()
Lb = Listbox(top)
Lb.insert(1, 'Python')
Lb.insert(2, 'Java')
Lb.insert(3, 'C++')
Lb.insert(4, 'Any other')
Lb.pack()
top.mainloop() """

# Scrollbar
""" from tkinter import *
root = Tk()
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
mylist = Listbox(root, yscrollcommand=scrollbar.set)

for line in range(20):
    mylist.insert(END, 'This is line number' + str(line))
mylist.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=mylist.yview)
mainloop() """

# Menu
""" from tkinter import *
root = Tk()
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open...')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')
mainloop() """

# Canvas
""" from tkinter import *
master = Tk()
w = Canvas(master, width=40, height=60)
w.pack()
w.create_line(0, 10, 30, 10 )
mainloop()  """

""" import tkinter as tk

root = tk.Tk()
root.title("Canvas Demo")

canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()

canvas.create_line(50, 50, 350, 50, fill="blue", width=3)

canvas.create_rectangle(100, 100, 300, 200, outline="green", fill="lightgreen")

canvas.create_oval(150, 150, 250, 250, outline="red", fill="pink")

canvas.create_text(200, 280, text="Hello Canvas!", font=("Arial", 16), fill="purple")

root.mainloop() """

""" import tkinter as tk

root = tk.Tk()
root.title("Canvas Demo")

c=tk.Canvas(root, width=400, height=300, bg="white")
c.pack()
a=c.create_oval(150, 150, 250, 250, outline="red", fill="pink")
b=[]
b.append(a)

def cmove():
    for i in b:
        c.move(i, 5, 0)
    c.after(50, cmove)
cmove()
root.mainloop() """


## adding imege 
""" import tkinter as tk
from tkinter import PhotoImage
root=tk.Tk()
root.title("Adding Image")

image=PhotoImage(file='QR.png')
image_label = tk.Label(root, image=image)
image_label.pack()

root.mainloop() """

# PIL
""" import tkinter as tk
from PIL import Image, ImageTk

root=tk.Tk()

image=Image.open('spidy.jpg')
image=ImageTk.PhotoImage(image)

image_lable=tk.Label(root, image=image)
image_lable.pack()

root.mainloop()

# image as button
import tkinter as tk
from PIL import Image, ImageTk

root=tk.Tk()
root.title('image as button')

image=Image.open('Dodge-Challenger.png')
image=ImageTk.PhotoImage(image)

image_button=tk.Button(root, image=image)
image_button.pack()

root.mainloop() """

# speech
""" import tkinter as tk
import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        status_label.config(text="Listening...")
        window.update()
        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio)
            result_text.set(text)
            status_label.config(text="Recognition complete.")
        except sr.UnknownValueError:
            result_text.set("Could not understand audio.")
            status_label.config(text="Try again.")
        except sr.RequestError:
            result_text.set("API unavailable.")
            status_label.config(text="Error.")

# GUI setup
window = tk.Tk()
window.title("Speech Recognition App")
window.geometry("400x200")

result_text = tk.StringVar()

tk.Label(window, text="Click to Speak", font=("Arial", 14)).pack(pady=10)
tk.Button(window, text="Start Listening", command=recognize_speech).pack(pady=10)
tk.Label(window, textvariable=result_text, wraplength=350, font=("Arial", 12)).pack(pady=10)
status_label = tk.Label(window, text="", font=("Arial", 10), fg="blue")
status_label.pack()

window.mainloop() """   

""" import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk

def generate_qr():
    data = entry.get()
    if not data:
        messagebox.showwarning("Input Error", "Please enter some text to generate QR code.")
        return

    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img = img.resize((200, 200))  # Resize for display

    img_tk = ImageTk.PhotoImage(img)
    qr_label.config(image=img_tk)
    qr_label.image = img_tk  # Keep reference to avoid garbage collection

# GUI setup
root = tk.Tk()
root.title("QR Code Generator")

tk.Label(root, text="Enter text or URL:").pack(pady=5)
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

tk.Button(root, text="Generate QR Code", command=generate_qr).pack(pady=10)

qr_label = tk.Label(root)
qr_label.pack(pady=10)

root.mainloop() """

# bank
""" import tkinter as tk
from tkinter import messagebox

# Dictionary to store account data
accounts = {}

def create_account():
    name = name_entry.get()
    amount = amount_entry.get()
    if name in accounts:
        messagebox.showerror("Error", "Account already exists!")
    else:
        accounts[name] = int(amount)
        messagebox.showinfo("Success", f"Account created for {name} with balance {amount}")

def deposit():
    name = name_entry.get()
    amount = amount_entry.get()
    if name not in accounts:
        messagebox.showerror("Error", "Account does not exist!")
    else:
        try:
            accounts[name] += int(amount)
            messagebox.showinfo("Success", f"₹{amount} deposited to {name}'s account")
        except ValueError:
            messagebox.showerror("Error", "Invalid amount")

def withdraw():
    name = name_entry.get()
    amount = amount_entry.get()
    if name not in accounts:
        messagebox.showerror("Error", "Account does not exist!")
    else:
        try:
            amt = amount
            if accounts[name] >= int(amt):
                accounts[name] -= int(amt)
                messagebox.showinfo("Success", f"₹{amt} withdrawn from {name}'s account")
            else:
                messagebox.showerror("Error", "Insufficient balance")
        except ValueError:
            messagebox.showerror("Error", "Invalid amount")

def check_balance():
    name = name_entry.get()
    if name not in accounts:
        messagebox.showerror("Error", "Account does not exist!")
    else:
        balance = accounts[name]
        messagebox.showinfo("Balance", f"{name}'s balance: ₹{balance}")

# GUI setup
root = tk.Tk()
root.title("Simple Bank App")

tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Amount:").grid(row=1, column=0, padx=10, pady=5)
amount_entry = tk.Entry(root)
amount_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Button(root, text="Create Account", command=create_account).grid(row=2, column=0, pady=10)
tk.Button(root, text="Deposit", command=deposit).grid(row=2, column=1, pady=10)
tk.Button(root, text="Withdraw", command=withdraw).grid(row=3, column=0, pady=10)
tk.Button(root, text="Check Balance", command=check_balance).grid(row=3, column=1, pady=10)

root.mainloop() """

# train
""" import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Live Running Train")
root.geometry("800x200")

# Create a canvas to draw the train
canvas = tk.Canvas(root, width=800, height=200, bg="skyblue")
canvas.pack()

# Draw the train (simple rectangles for engine and coaches)
train_parts = []
x_start = -200  # Start off-screen
for i in range(4):  # 1 engine + 3 coaches
    part = canvas.create_rectangle(x_start + i*60, 80, x_start + i*60 + 50, 130, fill="red" if i == 3 else "blue")
    train_parts.append(part)

# Draw wheels
    wheel1 = canvas.create_oval(x_start + i*60 + 5, 130, x_start + i*60 + 20, 145, fill="black")
    wheel2 = canvas.create_oval(x_start + i*60 + 30, 130, x_start + i*60 + 45, 145, fill="black")
    train_parts.extend([wheel1, wheel2])

# Animate the train
def move_train():
    for part in train_parts:
        canvas.move(part, 5, 0)
    canvas.after(10, move_train)

move_train()
root.mainloop() """
