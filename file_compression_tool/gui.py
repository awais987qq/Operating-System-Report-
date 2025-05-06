import tkinter as tk
from tkinter import filedialog, messagebox
import os
from compress import compress_file, compress_folder
from integrity import verify_integrity

def browse_input():
    path = filedialog.askopenfilename()
    if not path:
        path = filedialog.askdirectory()
    if path:
        input_path.set(path)

def compress():
    path = input_path.get()
    fmt = format_var.get()
    level = level_var.get()
    verify = verify_var.get()

    if not os.path.exists(path):
        messagebox.showerror("Error", "Input path does not exist.")
        return

    # Map formats to extensions
    extension_map = {
        "zip": ".zip",
        "gzip": ".gz",
        "tar": ".tar",
        "7z": ".7z"
    }

    output = path + extension_map.get(fmt, ".zip")

    try:
        if os.path.isdir(path):
            if fmt in ["gzip", "7z"]:
                raise ValueError(f"{fmt.upper()} format does not support folder compression in this tool.")
            compress_folder(path, output, fmt, level)
        else:
            compress_file(path, output, fmt, level)

        messagebox.showinfo("Success", f"Compressed to: {output}")

        if verify:
            result = verify_integrity(path, output)
            if result:
                messagebox.showinfo("Integrity", "Integrity check passed.")
            else:
                messagebox.showwarning("Integrity", "Integrity check failed.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI layout
root = tk.Tk()
root.title("File Compression Tool")

input_path = tk.StringVar()
format_var = tk.StringVar(value="zip")
level_var = tk.StringVar(value="best")
verify_var = tk.BooleanVar()

tk.Label(root, text="Input File/Folder:").pack()
tk.Entry(root, textvariable=input_path, width=50).pack()
tk.Button(root, text="Browse", command=browse_input).pack(pady=5)

tk.Label(root, text="Format:").pack()
tk.OptionMenu(root, format_var, "zip", "gzip", "tar", "7z").pack()

tk.Label(root, text="Compression Level:").pack()
tk.OptionMenu(root, level_var, "fast", "best").pack()

tk.Checkbutton(root, text="Verify Integrity", variable=verify_var).pack(pady=5)
tk.Button(root, text="Compress", command=compress, bg="lightblue").pack(pady=10)

root.mainloop()
