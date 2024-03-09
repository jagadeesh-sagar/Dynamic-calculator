import tkinter as tk
from tkinter import PhotoImage
def button_click(symbol):

    if symbol=="C":
        entry.delete(0,tk.END)


    elif symbol=="=":
      try:
        result=eval(entry.get())
        entry.delete(0,tk.END)
        entry.insert(tk.END,str(result))
      except Exception as e:
        entry.delete(0,tk.END)
        entry.insert(tk.END,"error")

    else:

       entry.insert(tk.END,symbol)

root=tk.Tk()
root.title("dynamic calculator")
root.geometry("800x800")


entry=tk.Entry(root,width=50,borderwidth=7,insertwidth=7,insertbackground="red",insertborderwidth=5)
entry.grid(row=0,column=0,rowspan=3,columnspan=3,padx=10,pady=50)# (row=0, column=0, columnspan=4, padx=10, pady=10)
"""button=[("7",0)
        
        ]"""
button1=tk.Button(root,text="1",command=lambda symbol="1":button_click(symbol),width=5,height=2)
button1.grid(row=4,column=0,rowspan=1,columnspan=1,padx=1,pady=1)
button2=tk.Button(root,text="2",command=lambda symbol="2":button_click(symbol),width=5,height=2)
button2. grid(row=4,column=1,rowspan=1,columnspan=1,padx=5,pady=5)
button3=tk.Button(root,text="3",command=lambda symbol="3":button_click(symbol),width=5,height=2)
button3. grid(row=4,column=2,padx=5,pady=5)
button4=tk.Button(root,text="4",command=lambda symbol="4":button_click(symbol),width=5,height=2)
button4. grid(row=5,column=0,padx=5,pady=5)
button5=tk.Button(root,text="5",command=lambda symbol="5":button_click(symbol),width=5,height=2)
button5. grid(row=5,column=1,padx=5,pady=5)
button6=tk.Button(root,text="6",command=lambda symbol="6":button_click(symbol),width=5,height=2)
button6. grid(row=5,column=2,padx=5,pady=5)
button7=tk.Button(root,text="7",command=lambda symbol="7":button_click(symbol),width=5,height=2)
button7. grid(row=6,column=0,padx=5,pady=5)
button8=tk.Button(root,text="8",command=lambda symbol="8":button_click(symbol),width=5,height=2)
button8. grid(row=6,column=1,padx=5,pady=5)
button9=tk.Button(root,text="9",command=lambda symbol="9":button_click(symbol),width=5,height=2)
button9. grid(row=6,column=2,padx=5,pady=5)
button10=tk.Button(root,text="0",command=lambda symbol="0":button_click(symbol),width=5,height=2)
button10. grid(row=7,column=0,padx=5,pady=5)
button11=tk.Button(root,text="+",command=lambda symbol="+":button_click(symbol),width=5,height=2)
button11. grid(row=7,column=1,padx=5,pady=5)
button12=tk.Button(root,text="-",command=lambda symbol="-":button_click(symbol),width=5,height=2)
button12. grid(row=7,column=2,padx=5,pady=5)
button13=tk.Button(root,text="*",command=lambda symbol="*":button_click(symbol),width=5,height=2)
button13. grid(row=8,column=0,padx=5,pady=5)
button14=tk.Button(root,text="/",command=lambda symbol="/":button_click(symbol),width=5,height=2)
button14. grid(row=8,column=1,padx=5,pady=5)
button15=tk.Button(root,text="C",command=lambda symbol="C":button_click(symbol),width=5,height=2)
button15. grid(row=8,column=2,padx=5,pady=5)
button16=tk.Button(root,text="=",command=lambda symbol="=":button_click(symbol),width=5,height=2)
button16. grid(row=9,column=0,columnspan=3,padx=5,pady=5)

root.mainloop()
