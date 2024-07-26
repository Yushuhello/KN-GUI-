title1=ttk.Label(han1,text="欢迎使用此计算器",bootstyle="success").place(x=5,y=10) # type: ignore
title2=ttk.Label(han1,text="选择所使用燃料类型",bootstyle="success").place(x=5,y=40)
monitor=ttk.StringVar()
def ding():
    print(monitor.get())
choss1=ttk.Radiobutton(han1,text="KNSB",bootstyle="success",value="KNSB",variable=monitor).place(x=5,y=79) # type: ignore
choss2=ttk.Radiobutton(han1,text="KNSU",bootstyle="success",value="KNSU",variable=monitor).place(x=85,y=79)
choss3=ttk.Radiobutton(han1,text="KNDX",bootstyle="success",value="KNDX",variable=monitor).place(x=165,y=79)

ning=ttk.Button(han1,text="确定",command=ding,style="success").place(x=5,y=130)
