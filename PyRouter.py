import subprocess, shlex,os
from Tkinter import *


def Made_rot():
    namered=str(E3.get())
    EnPass=str(E4.get())
    RouterDef=os.path.join(*['netsh wlan set hostednetwork mode=allow ssid='+namered+' key='+EnPass+' keyusage=persistent'])
    #RouterDef save to  on file txt  and mada is exists
    subprocess.call(RouterDef, shell=True)
    subprocess.call('netsh wlan start hostednetwork', shell=True)
def test():
    print("oi")


root = Tk()

w = Label(root, text="config router")
w.pack()
w.grid(row=1, column=3)
sp = Label(root, text="")
sp.pack()
sp.grid(row=0, column=1)

Button(root, text='nome da  rede', command=test).grid(row=2, column=2, sticky=W, pady=5)
Button(root, text='senha da rede', command=test).grid(row=3, column=2, sticky=W, pady=5)
Button(root, text='Desconectar', command=test).grid(row=4, column=3, sticky=W, pady=5)

E3 = Entry(root)
E3["width"]=100
E3.grid(row=2, column=3)
E4 = Entry(root)
E4["width"]=100
E4.grid(row=3, column=3)

root.geometry("700x200")
root.resizable(width=False, height=False)
root.mainloop()