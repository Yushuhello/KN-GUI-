from tkinter.messagebox import INFO
import ttkbootstrap as ttk #导入ttk
import tkinter as tk #导入tk
root=ttk.Window(title="KN系列火箭计算器",size=(250,250),themename="journal") #搭建窗口 设置主题

zi=ttk.Notebook(root)

han1=ttk.Frame(style="success",width=220,height=220)
han2=ttk.Frame(style="light")

title1=ttk.Label(han1,text="欢迎使用此计算器",bootstyle="success").place(x=5,y=10) # type: ignore
title2=ttk.Label(han1,text="选择所使用燃料类型",bootstyle="success").place(x=5,y=40)
monitor=ttk.StringVar()
def ding():
    print(monitor.get())
choss1=ttk.Radiobutton(han1,text="KNSB",bootstyle="success",value="KNSB",variable=monitor).place(x=5,y=79) # type: ignore
choss2=ttk.Radiobutton(han1,text="KNSU",bootstyle="success",value="KNSU",variable=monitor).place(x=85,y=79)
choss3=ttk.Radiobutton(han1,text="KNDX",bootstyle="success",value="KNDX",variable=monitor).place(x=165,y=79)

ning=ttk.Button(han1,text="确定",command=ding,style="success").place(x=5,y=130)

zi.add(han1,text="tyh")
zi.add(han2,text="ty")

root.mainloop()
