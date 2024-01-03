import tkinter as tk

root = tk.Tk()
root.title ("Perhitungan")
root.config(bg="lightyellow")
root.geometry("500x500")

# Judul
label1 = tk.Label(master=root, text= "Perhitungan Arus", font = "Normal 25", bg="lightyellow")
label1.grid (row=0, column=0, columnspan=4, pady=20, padx=30)

pilihan = 0

# Fungsi
def tegangan():
    global pilihan
    pilihan = 1
    label2.config(text="Arus")
    label3.config(text="Hambatan")
    label4.config(text="X")
    label5.config(text= "Hasil Tegangan :")
    label6.config(text="")


def arus():
    global pilihan
    pilihan = 2
    label2.config(text="Arus")
    label3.config(text="Hambatan")
    label4.config(text="/")
    label5.config(text= "Hasil Arus :")
    label6.config(text="")

def hambatan():
    global pilihan
    pilihan = 3
    label2.config(text="Tegangan")
    label3.config(text="Arus")
    label4.config(text="/")
    label5.config(text= "Hasil Hambatan :")
    label6.config(text="")

def total():
    global pilihan
    if pilihan == 1:
        rumus = int(e1.get()) * int(e2.get())
        label6.config(text=rumus)

    if pilihan == 2:
        rumus = int(e1.get()) / int(e2.get())
        label6.config(text=rumus)

    if pilihan == 3:
        rumus = int(e1.get()) / int(e2.get())
        label6.config(text=rumus)


# Button
b1 = tk.Button(master=root, text="Tegangan", width=10, font="Normal 15", relief="ridge", bd=5, activebackground="black",
               command=tegangan)
b1.grid (row=1, column=0, padx=15)

b2 = tk.Button(master=root, text="Arus", width=10, font="Normal 15", relief="ridge", bd=5, activebackground="black",
               command=arus)
b2.grid (row=1, column=1, padx=15)

b3 = tk.Button(master=root, text="Hambatan", width=10, font="Normal 15", relief="ridge", bd=5, activebackground="black",
               command=hambatan)
b3.grid (row=1, column=2, padx=15)

# Penanda

label2 = tk.Label(master=root, text="", bg="lightyellow", font="Normal 20")
label2.grid (row=2, column=0, pady=30, padx=15)

label3 = tk.Label(master=root, text="", bg="lightyellow", font="Normal 20")
label3.grid (row=2, column=2, pady=30, padx=15)

# Input
e1 = tk.Entry(master=root, bd=5, relief="ridge", font="Normal 20", width=10)
e1.grid(row=3, column=0)

label4 = tk.Label(master=root, text="/", font="Normal 20", bg="lightyellow")
label4.grid (row=3, column=1)

e2 = tk.Entry(master=root, bd=5, relief="ridge", font="Normal 20", width=10)
e2.grid(row=3, column=2)

b4 = tk.Button(master=root, text="Hitung", activebackground="black", bd=5, relief="ridge", font="Normal 15", width=10, 
               command=total)
b4.grid(row=4, column=1, pady=30)


# Hasil

label5 = tk.Label(master=root, text="", font="Normal 20", bg="lightyellow")
label5.grid(row=5, column=0, pady=20)

label6 = tk.Label(master=root, text="", font="Normal 20", bg="lightyellow")
label6.grid(row=5, column=1, pady=20)


root.mainloop()