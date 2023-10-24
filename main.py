import tkinter as tk

root = tk.Tk()
root.title('calculator')
root.geometry('300x375+0+0')
root.config(bg='gray')
root.resizable(False, False)


equation = tk.StringVar()
entry_value ='' 


def show(val):
    global entry_value
    entry_value = entry_value + str(val)
    equation.set(entry_value)
  

def clear():
    global entry_value
    entry_value = ''
    equation.set(entry_value)

def solve():
    global entry_value
    result = str(eval(entry_value))
    equation.set(result)

def back():
    global entry_value
    while entry_value:
        entry_value = entry_value[:-1]
        equation.set(entry_value)
        break

    
  





entry = tk.Entry(root, width=70, font=('Arial Bold', 28), textvariable=equation).place(x=0,y=0)

tk.Button(root, text='(', width=9, height=3, relief='flat', command=lambda:show('(')).place(x=1,y=50)
tk.Button(root, text=')', width=9, height=3, relief='flat', command=lambda:show(')')).place(x=76,y=50)
tk.Button(root, text='%', width=9, height=3, relief='flat', command=lambda:show('%')).place(x=151,y=50)
tk.Button(root, text='/', width=9, height=3, relief='flat', command=lambda:show('/')).place(x=226,y=50)

tk.Button(root, text='1', width=9, height=3, relief='flat', command=lambda:show(1)).place(x=1,y=108)
tk.Button(root, text='2', width=9, height=3, relief='flat', command=lambda:show(2)).place(x=76,y=108)
tk.Button(root, text='3', width=9, height=3, relief='flat', command=lambda:show(3)).place(x=151,y=108)
tk.Button(root, text='*', width=9, height=3, relief='flat', command=lambda:show('*')).place(x=226,y=108)

tk.Button(root, text='4', width=9, height=3, relief='flat', command=lambda:show(4)).place(x=1,y=166)
tk.Button(root, text='5', width=9, height=3, relief='flat', command=lambda:show(5)).place(x=76,y=166)
tk.Button(root, text='6', width=9, height=3, relief='flat', command=lambda:show(6)).place(x=151,y=166)
tk.Button(root, text='-', width=9, height=3, relief='flat', command=lambda:show('-')).place(x=226,y=166)

tk.Button(root, text='7', width=9, height=3, relief='flat', command=lambda:show(7)).place(x=1,y=224)
tk.Button(root, text='8', width=9, height=3, relief='flat', command=lambda:show(8)).place(x=76,y=224)
tk.Button(root, text='9', width=9, height=3, relief='flat', command=lambda:show(9)).place(x=151,y=224)
tk.Button(root, text='+', width=9, height=3, relief='flat', command=lambda:show('+')).place(x=226,y=224)

tk.Button(root, text='c', width=9, height=3, relief='flat', command=clear).place(x=1,y=282)
tk.Button(root, text='0', width=9, height=3, relief='flat', command=lambda:show(0)).place(x=76,y=282)
tk.Button(root, text='.', width=9, height=3, relief='flat', command=lambda:show('.')).place(x=151,y=282)
tk.Button(root, text='=', width=9, height=3, bg='red' , relief='flat', command=solve).place(x=226,y=282)
tk.Button(root, text='➡', bg='red' ,width=9,height=2, relief='flat', command=back,
          justify='center',background='blue',fg='white').place(x=226,y=340)





root.mainloop()


