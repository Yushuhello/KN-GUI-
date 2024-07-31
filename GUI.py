from queue import Full
from ttkbootstrap.dialogs import Messagebox
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
dingfourth=ttk.StringVar()

title1=ttk.Label(han1,text="发动机长度(mm):",bootstyle="success").place(x=5,y=15)
into1=ttk.Entry(han1,style="success",textvariable=dingfirst).place(x=140,y=10)

title2=ttk.Label(han1,text="发动机内半径(mm):",bootstyle="success").place(x=5,y=55)
into2=ttk.Entry(han1,style="success",textvariable=dingsecond).place(x=140,y=50)

title3=ttk.Label(han1,text="发动机外半径(mm):",bootstyle="success").place(x=5,y=95)
into3=ttk.Entry(han1,style="success",textvariable=dingthird).place(x=140,y=90)

title4=ttk.Label(han1,text="发动机壳体密度(g/c㎡):",bootstyle="success").place(x=5,y=135)
into4=ttk.Entry(han1,style="success",textvariable=dingfourth).place(x=175,y=130)


def decide():
    into1_type=int(dingfirst.get())
    into2_type=int(dingsecond.get())
    into3_type=int(dingthird.get())
    into4_type=int(dingfourth.get())
    print(into1_type)
    print(into2_type)
    print(into3_type)
    print(into4_type)
    a=3.1415926*(into3_type**2-into2_type**2)
    b=into1_type
    c=(a*b)/1000
    d=into4_type*c
    print(d)
    title6=ttk.Label(han1,text=d,style="success",relief="flat").place(x=100,y=250)
button1=ttk.Button(han1,text="确定",style="success-outline",command=decide).place(x=10,y=200)
def box():
    Messagebox.ok(message='铁:7.86g/cm³ \n铝:2.7 g/cm³ \n铝合金:2.63～2.85g/cm3 \n碳纤维:1.5～2.0g/cm3 \nPVC:1.3~1.45g/cm³',title="密度参考",alert=True)
button2=ttk.Button(han1,text="密度参考",style="success-outline",command=box).place(x=70,y=200)

title5=ttk.Label(han1,text="质量(g):",style="success",relief="flat").place(x=10,y=250)

zi.add(han1,text="发动机质量计算")
zi.add(han2,text="发动机推力模拟")
zi.place(x=5,y=5)

root.mainloop()
#创作者：yushu


