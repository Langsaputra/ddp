import tkinter as tk
from tkinter import ttk

class MeteranApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Konversi Meter")
        self.root.geometry("500x500")

        self.input_label = ttk.Label(root, text="Panjang (meter):")
        self.input_label.grid(row=0, column=0, padx=10, pady=10)

        self.input_entry = ttk.Entry(root)
        self.input_entry.grid(row=0, column=1, padx=10, pady=10)

        self.result_label = ttk.Label(root, text="Hasil:")
        self.result_label.grid(row=1, column=0, padx=10, pady=10)

        self.result_value = tk.StringVar()
        self.result_entry = ttk.Entry(root, textvariable=self.result_value, state='readonly')
        self.result_entry.grid(row=1, column=1, padx=10, pady=10)

        self.unit_label = ttk.Label(root, text="Satuan:")
        self.unit_label.grid(row=2, column=0, padx=10, pady=10)

        self.unit_let = tk.StringVar()
        self.unit_let.set("Kilometer")  # Satuan awal
        self.unit_combobox = ttk.Combobox(root, values=["Kilometer", "Hektometer", "Dekameter", "Meter",
                                                        "Decimeter", "Centimeter", "Millimeter"],
                                          textvariable=self.unit_let)
        self.unit_combobox.grid(row=2, column=1, padx=10, pady=10)

        self.calculate_button = ttk.Button(root, text="Hitung", command=self.calculate_length)
        self.calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

    def calculate_length(self):
        try:
            length_meter = float(self.input_entry.get())
            unit_selected = self.unit_let.get()

            # Faktor konversi ke meter
            conversion_factors = {
                "Kilometer": 0.001,
                "Hektometer": 0.01,
                "Dekameter": 0.1,
                "Meter": 1.0,
                "Decimeter": 10.0,
                "Centimeter": 100.0,
                "Millimeter": 1000.0
            }

            # Rumus konversi
            length_converted = length_meter * conversion_factors[unit_selected]
            self.result_value.set(f"{length_converted} {unit_selected}")

            # Menangani kesalahan saat mengubah tipe data
        except ValueError:
            # Tangani kesalahan jika input tidak dapat diubah menjadi float
            self.result_value.set("Masukkan angka valid")

if __name__ == "__main__":
    root = tk.Tk()
    app = MeteranApp(root)
    root.mainloop()

