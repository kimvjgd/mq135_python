# from tkinter import *
# from tkinter import ttk
# from tkinter import messagebox
# win = Tk()
# win.title("Yonsei EDL")
# win.geometry('200x100+200+200')
# def clickMe():
#   messagebox.showinfo("CO2 detected", str.get())
# str = StringVar()
# # textbox = ttk.Entry(win, width=20, textvariable=str)
# # textbox.grid(column = 0 , row = 0)
# action=ttk.Button(win, text="CO2 detected", command=clickMe)
# action.grid(column=0, row=1)
# win.mainloop()

# import tkinter.messagebox as msgbox
# from tkinter import *

# root = Tk()
# root.title("EDL LAB")
# root.geometry('320x240')

# response = msgbox.askokcancel("Y / N", "EDL LAB\n\n측정을 계속하시겠습니까?")


# print(response)

from tkinter import *

root = Tk()
root.title("DongDong")
root.geometry("640x480")

def create_new_file():
  print('new file created')

# File Menu
menu = Menu(root)
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New File", command = create_new_file)
menu_file.add_command(label="New Window")
menu_file.add_separator()
menu_file.add_command(label="Open File")
menu_file.add_separator()
menu_file.add_command(label="Save All", state="disable")
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)


menu.add_cascade(label="Edit")

root.config(menu=menu)
root.mainloop()