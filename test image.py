from tkinter import *
root=Tk()
toto=PhotoImage(file="oui.png")
canvas=Canvas(root,width=3000,height=3000)
canvas.pack()
canvas.create_image(0,0,anchor=NW,image=toto)
root.mainloop()
