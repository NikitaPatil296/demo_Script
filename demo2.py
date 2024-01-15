import tkinter as tk
from tkinter import filedialog
import os

def convert_to_decimal():
    hex1 = entry_hex1.get()
    hex2 = entry_hex2.get()
    hex3 = entry_hex3.get()

    try:
        decimal1 = int(hex1, 16)
        decimal2 = int(hex2, 16)
        decimal3 = int(hex3, 16)
    
        entry_decimal1.delete(0, tk.END)
        entry_decimal2.delete(0, tk.END)
        entry_decimal3.delete(0, tk.END)

        entry_decimal1.insert(0, str(decimal1))
        entry_decimal2.insert(0, str(decimal2))
        entry_decimal3.insert(0, str(decimal3))

        result_label.config(text="")
    except ValueError:
        result_label.config(text="Invalid hexadecimal input. Please enter valid hex numbers.")

def open_pdf_file(module_id):
    module_id_str = entry_decimal1.get()

    if not module_id_str:
        result_label.config(text="Module ID is empty. Please enter a valid Module ID.")
        return

    try:
        module_id = int(module_id_str)
        pdf_path = f"D:\\SCRIPT\\demo_Script\\fsoc ws2223 lecture_{module_id}.pdf"

        if os.path.isfile(pdf_path):
            os.startfile(pdf_path)
        else:
            result_label.config(text="PDF file not found for the specified Module ID.")
    except ValueError:
        result_label.config(text="Invalid Module ID. Please enter a valid integer.")

# Create the main window

root = tk.Tk()
root.title("DET Module Helper")

# Create labels and entry widgets for hex inputs
label_hex1 = tk.Label(root, text="Module Id")
label_hex2 = tk.Label(root, text="API Id")
label_hex3 = tk.Label(root, text="Error Id")

entry_hex1 = tk.Entry(root)
entry_hex2 = tk.Entry(root)
entry_hex3 = tk.Entry(root)

# Create labels and entry widgets for decimal outputs
label_decimal1 = tk.Label(root, text="Module Name")
label_decimal2 = tk.Label(root, text="API")
label_decimal3 = tk.Label(root, text="Error Description")

entry_decimal1 = tk.Entry(root, state=tk.DISABLED)  # Disable editing
entry_decimal2 = tk.Entry(root, state=tk.DISABLED)
entry_decimal3 = tk.Entry(root, state=tk.DISABLED)

# Create a label for displaying error messages
result_label = tk.Label(root, text="", fg="red")

# Create the execute button
execute_button = tk.Button(root, text="Execute", command=convert_to_decimal, width=50)

# Create the "Open PDF" button
open_pdf_button = tk.Button(root, text="Open PDF", command=open_pdf_file)

label_hex1.grid(row=0, column=0, padx=5, pady=5)
entry_hex1.grid(row=0, column=1, padx=5, pady=5)
label_decimal1.grid(row=0, column=2, padx=5, pady=5)
entry_decimal1.grid(row=0, column=3, padx=5, pady=5)

label_hex2.grid(row=1, column=0, padx=5, pady=5)
entry_hex2.grid(row=1, column=1, padx=5, pady=5)
label_decimal2.grid(row=1, column=2, padx=5, pady=5)
entry_decimal2.grid(row=1, column=3, padx=5, pady=5)

label_hex3.grid(row=2, column=0, padx=5, pady=5)
entry_hex3.grid(row=2, column=1, padx=5, pady=5)
label_decimal3.grid(row=2, column=2, padx=5, pady=5)
entry_decimal3.grid(row=2, column=3, padx=5, pady=5)

result_label.grid(row=3, column=0, columnspan=4, padx=5, pady=5)

execute_button.grid(row=4, column=0, columnspan=4, pady=10 , padx=30)

open_pdf_button.grid(row=6, column=0, columnspan=3, pady=10, padx=30)

# Start the Tkinter event loop
root.mainloop()
