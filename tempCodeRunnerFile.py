30:
        win = Tk()
        win.title("Yonsei EDL")
        win.geometry('200x100+200+200')
        def clickMe():
          messagebox.showinfo("CO2 detected", str.get())
        str = StringVar()
        # textbox = ttk.Entry(win, width=20, textvariable=str)
        # textbox.grid(column = 0 , row = 0)
        action=ttk.Button(win, text="CO2 detected", command=clickMe)
        action.grid(column=0, row=1)
        win.mainloop()