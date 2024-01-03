import tkinter as tk


def tambahkan():
    angka1 = int(input1.get())
    angka2 = int(input2.get())
    hasil = angka1 * angka2
    label_hasil["text"] = f"Hasil : {hasil}"


root = tk.Tk()
root.title("Kalkulator Perkalian")
root.geometry("500x500")

label = tk.Label(master=root, text= "Kalkulator Perkalian")
labelplus = tk.Label(master=root, text ="*")
label_hasil = tk.Label(master=root, text="Hasil :")

input1 = tk.Entry(master=root)
input2 = tk.Entry(master=root)

button = tk.Button(master=root, text="Perkalian",
command=tambahkan)


label.pack()
input1.pack()
input2.pack()
button.pack()
labelplus.pack()
label_hasil.pack()

root.mainloop()