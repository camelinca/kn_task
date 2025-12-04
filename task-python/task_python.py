import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        price = float(input_price.get())
        discount = float(input_discount.get())

        final_price = price - (price * discount / 100)
        label_result.config(text=f"Final Price: Rp. {final_price:,.2f}")

    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid!")

root = tk.Tk()
root.title("Discount Calculator")
root.geometry("300x200")  

label_price = tk.Label(root, text="Original Price:")
label_price.pack()
input_price = tk.Entry(root)
input_price.pack()

label_discount = tk.Label(root, text="Discount (%):")
label_discount.pack()
input_discount = tk.Entry(root)
input_discount.pack()

btn_calc = tk.Button(root, text="Calculate", command=calculate)
btn_calc.pack(pady=10)

label_result = tk.Label(root, text="Final Price: Rp. 0.00")
label_result.pack()

root.mainloop()
