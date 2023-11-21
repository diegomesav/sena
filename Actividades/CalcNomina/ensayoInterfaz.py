import tkinter as tk

ventana = tk.Tk()
ventana.geometry("400x300")

textField = tk.Entry(ventana)
textField.pack()

label = tk.Label(ventana)
label.pack()

def boxText():
    text20 = textField.get()
    label["text"] = text20
    print(text20)
    textField.delete("0","end")


button1 = tk.Button(ventana, text="click", command=boxText)
button1.pack()




ventana.mainloop()