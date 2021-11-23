import tkinter as tk
import time

root = tk.Tk()
root.geometry('750x380')
root.title("Halaman Utama")
root.configure(background='cyan')
w = tk.PhotoImage(file="member_update_lagi.png")
w1 = tk.Label(root,image=w)
w1.place(x=55,y=150)
x = tk.PhotoImage(file="non_member_update.png")
x1 = tk.Label(root, image=x)
x1.place(x=580,y=150)
u = tk.PhotoImage(file="logo_update_lagi.png")
u1 = tk.Label(root, image=u,bd=0)
u1.place(x=220,y=100)
v = tk.IntVar()
rb1 = tk.Radiobutton(root,bg="cyan",variable=v,value=0,text="Member",font="Helvetica 15")
rb2 = tk.Radiobutton(root,bg="cyan",variable=v,value=1,text="Non Member",font="Helvetica 15")
rb1.place(x=53,y=270)
rb2.place(x=560,y=270)
y = tk.Label(root,text="SELAMAT DATANG DI ARETA LAUNDRY!!!",bg='cyan',font="Times 20")
y.place(x=120,y=40)
waktu = time.asctime(time.localtime(time.time()))
jam = tk.Label(root,text=waktu,bg='cyan',font="Verdana 10")
jam.place(x=300,y=10)
def move1():
    root.destroy()
    if v.get()==0 :
        from log_in import vp_start_gui
        vp_start_gui()
    else :
        from orderan import vp_start_gui
        vp_start_gui()
buton1=tk.Button(text="Lanjut",bg="dark blue",fg="white",command=move1,width=10)
buton1.place(x=380,y=330)
def move2():
    root.destroy()
    from registered import vp_start_gui
    vp_start_gui()
buton2=tk.Button(text="Daftar",bg="dark blue",fg="white",command=move2,width=10)
buton2.place(x=280,y=330)
root.mainloop()
