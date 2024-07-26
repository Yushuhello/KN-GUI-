import tkinter as tk
import ttkbootstrap as ttk

root = tk.Tk()
root.geometry('310x300+500+500')
#
l=ttk.Label(root,bootstyle="simplex",text='txt文件查看器',font=('微软雅黑',15))
l.pack()
e=ttk.Entry(bootstyle="simplex")
e.place(x=140,y=133)
l2=ttk.Label(root,bootstyle="simplex",text='请输入绝对路径：',font=('微软雅黑',11))
l2.place(x=14,y=135)
def gh():
    path=e.get()
    print(path)
    fg = path
    f = open(fg, 'r', encoding='utf-8')
    print(f.read())
    l3 = ttk.Label(root, bootstyle="simplex", text=f, font=('微软雅黑', 11))
    l3.place(x=10)
b1=ttk.Button(root,bootstyle="simplex",text='打开',command=gh)
b1.place(x=140,y=200)
#
root.mainloop()