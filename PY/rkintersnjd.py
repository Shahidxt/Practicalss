import tkinter as tk

window = tk.Tk()

window.geometry("300x100")

window.title("Shahid")

# entry = tk.Entry(window, text="sjaj")
# label = tk.Label(window, text="this is label")
# button = tk.Button(window, text='button')

# entry.grid(column=1, row=1)
# label.grid(column=0, row=1)
# button.grid(column=1, row=2)

result = tk.Label(window)

def Show():
    ba = textbox.get()
    result.config(text=ba)
    result.grid(column=1, row=5)


textbox = tk.Entry(window)
label = tk.Label(window, text="Enter Value: ")
exit = tk.Button(window, text="Exit", command=window.destroy)
Hello = tk.Button(window, text="Hello", command=Show)

textbox.grid(column=1, row=1)
label.grid(column=0, row=1)

Hello.grid(column=0, row=2)
exit.grid(column=0, row=3)
result.grid(column=0, row=4)

window.mainloop()
