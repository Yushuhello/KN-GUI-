from queue import Full
import pyvista as pv
import numpy as np
from tkinter.messagebox import INFO
import ttkbootstrap as ttk #导入ttk
import tkinter as tk #导入tk
root=ttk.Window(title="KN系列火箭计算器",size=(500,500),themename="journal",resizable=(0,0)) #搭建窗口 设置主题

zi=ttk.Notebook(root)

han1=ttk.Frame(style="light",width=490,height=490)
han2=ttk.Frame(style="light")

dingfirst=ttk.StringVar()
dingsecond=ttk.StringVar()
dingthird=ttk.StringVar()

title1=ttk.Label(han1,text="发动机长度(mm):",bootstyle="success").place(x=5,y=15)
into1=ttk.Entry(han1,style="success",textvariable=dingfirst).place(x=140,y=10)

title2=ttk.Label(han1,text="发动机内半径(mm):",bootstyle="success").place(x=5,y=55)
into2=ttk.Entry(han1,style="success",textvariable=dingsecond).place(x=140,y=50)

title3=ttk.Label(han1,text="发动机外半径(mm):",bootstyle="success").place(x=5,y=95)
into3=ttk.Entry(han1,style="success",textvariable=dingthird).place(x=140,y=90)
def full_hope():
    print("76")

choose1=ttk.Menubutton(han1,style="success-outline",text="选择一种吧",menu="full").place(x=140,y=130)
full=ttk.Menu(choose1)
full.add_cascade(label="tyytt",command=full_hope)

title4=ttk.Label(han1,text="发动机壳体材质:",bootstyle="success").place(x=5,y=135)


def decide():
    into1_type=dingfirst.get()
    into2_type=dingsecond.get()
    into3_type=dingthird.get()
    print(into1_type)
    print(into2_type)
    print(into3_type)   
    
button1=ttk.Button(han1,text="确定",style="success-outline",command=decide).place(x=10,y=200)


zi.add(han1,text="发动机质量计算")
zi.add(han2,text="ty")
zi.place(x=5,y=5)

root.mainloop()
   


