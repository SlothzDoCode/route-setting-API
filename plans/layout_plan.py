import tkinter as tk
from tkinter import *

display = tk.Tk()

ModelArea = tk.Label(display,width=170,height=45, bg="black",fg = "white",text="3d view area")
ModelArea.place(x=0,y=100)

holdCatalogue = tk.Label(display,width=15,height=45,bg="red",text="catalogue\n of all\n holds")
holdCatalogue.place(x=1315,y=100)

controlPanel = tk.Label(display, width=200, height=5, bg="yellow",text="controls panel")
controlPanel.place(x=0,y=0)


display.attributes('-fullscreen',True)
mainloop()
