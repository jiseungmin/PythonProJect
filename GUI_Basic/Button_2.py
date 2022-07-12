from tkinter import *

root = Tk()
root.title("GUI")

btn1 = Button(root, text="버튼")
btn1.pack()

btn2 = Button(root, padx=10, pady=10, text="버튼2")
btn2.pack()

root.mainloop()
