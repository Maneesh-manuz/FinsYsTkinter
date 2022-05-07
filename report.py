from tkinter import *
import tkinter.font as font
from  tkinter import ttk
import tkinter as tk
from PIL import ImageTk,Image
import click

from requests import options
def selected(event):
    if menu.get() == 'Profit & loss':
        import report1
    elif  menu.get() == 'Balance sheet':
        import report2
    elif  menu.get() == 'Account Receivable ':
        import report3
    elif  menu.get() == 'Account Payable':
        import report4
 
    else :
        import report


window = tk.Tk()
window.title("finsYs")
width=window.winfo_screenwidth()
height=window.winfo_screenheight()
window.geometry("%dx%d" %(width,height))
window['bg']='#2f516a'
headingfont=font.Font(family='Helvitica', size=24,)
inv_heading= Label(window, borderwidth=1, relief="raised",width=60,font=headingfont,bg='#243e55', fg='#fff',height=4)
inv_heading.pack(pady=20)

cash=Label(window,text="REPORT",font=('Helvitica',25),bg='#243e55',fg='white').place(x = 220, y =110)                


menu= StringVar()
menu.set("reports")
options=["Profit & loss","Balance sheet","Account Receivable ","Account Payable"]
drop= OptionMenu(window,menu,*options,command=selected )
drop.config(bg='#243e55', fg="white",font=('Arial',18))
drop['menu'].config(bg='#2f516a',fg="white",font=('Arial',18))

drop.place(x=1000,y=110)

inv_heading= Label(window, borderwidth=1, relief="raised",width=60,font=headingfont,bg='#243e55', fg='#fff',height=50)
inv_heading.pack(pady=20)

window.mainloop()