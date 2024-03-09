import tkinter as tk
def button_click(symbol):

    if symbol=="C":
        entry.delete(tk.END,0)


    elif symbol=="=":
      try:
        result=eval(entry.get(0,tk.END))
        entry.insert(tk.END,str(result))
      except Exception as e:
        entry.delete(0,tk.END)
        entry.insert(tk.END,"error")

    else:

       entry.insert(tk.END,symbol)

root=tk.TK()
root.Title("dynamic calculator")
root.geometry("1000x700")
root.mainloop()
