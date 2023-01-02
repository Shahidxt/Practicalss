import tkinter as tk


parrent =tk.Tk()
ent = tk.StringVar()
parrent.geometry("400x500")
button1 = tk.Entry(parrent ,width=30)

def gettext():
    data = button1.get()
    text.config(text=data)
    
text = tk.Label(parrent,text='')
text.grid(row = 4, column = 1, pady = 2)   

Exit =tk.Button(parrent,text="Exit",command=parrent.destroy)
button1.grid(row = 1, column = 1, pady = 2)        
Exit.grid(row = 3, column = 1, pady = 2)   
print(button1.get())

button2 =tk.Button(parrent,text="button2",command=gettext)
list = tk.Listbox(parrent)
list.insert(1,"Python")
list.insert(2,"JavaScript")
list.insert(3,"DBMS")

button2.grid(row = 2, column = 1, pady = 2)        
list.grid(row = 0, column = 0, pady = 0)       
parrent.mainloop()
