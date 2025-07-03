#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk, messagebox

def text_to_hex(text: str) -> str:
    return text.encode("utf-8").hex()

def hex_to_text(hex_str: str) -> str:
    return bytes.fromhex(hex_str).decode("utf-8")

def convert():
    input_text = input_box.get("1.0", tk.END).strip()
    if not input_text:
        messagebox.showwarning("Input needed", "Please enter some text or hex to convert. [This was made with love by github.com/epicinver]")
        return

    direction = conversion_choice.get()
    try:
        if direction == "Text to Hex":
            output = text_to_hex(input_text)
        else:  # Hex to Text
            output = hex_to_text(input_text)
    except Exception as e:
        messagebox.showerror("Conversion error", f"Error: {e}")
        return

    output_box.config(state=tk.NORMAL)
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, output)
    output_box.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Hex/Text Converter by Epicinver")
root.geometry("500x350")
root.resizable(False, False)

conversion_choice = tk.StringVar(value="Text to Hex")

# Dropdown to choose conversion type
ttk.Label(root, text="Choose conversion:").pack(pady=(10,0))
conversion_menu = ttk.OptionMenu(root, conversion_choice, "Text to Hex", "Text to Hex", "Hex to Text")
conversion_menu.pack(pady=(0,10))

# Input label and text box
ttk.Label(root, text="Input:").pack(anchor="w", padx=10)
input_box = tk.Text(root, height=6, width=58)
input_box.pack(padx=10)

# Convert button
convert_btn = ttk.Button(root, text="Convert", command=convert)
convert_btn.pack(pady=10)

# Output label and text box (read-only)
ttk.Label(root, text="Output:").pack(anchor="w", padx=10)
output_box = tk.Text(root, height=6, width=58, state=tk.DISABLED)
output_box.pack(padx=10)

root.mainloop()

