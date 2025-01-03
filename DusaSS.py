import tkinter as tk
from tkinter import ttk, filedialog, messagebox

# Function to make the window draggable
def drag_window(event):
    root.geometry(f"+{event.x_root - offset_x}+{event.y_root - offset_y}")

# Function to start dragging
def start_drag(event):
    global offset_x, offset_y
    offset_x = event.x
    offset_y = event.y

# Function to exit the application
def close_window():
    root.destroy()

# Function for the attach button
def attach(button):
    button.config(state="disabled")  # Disable button
    root.title("DusaSS V1.3 - Attached")
    root.after(2000, lambda: root.title("DusaSS V1.3"))  # Reset title after 2 seconds

# Function to save the content as a Lua file
def save_as_lua():
    try:
        file_path = filedialog.asksaveasfilename(
            defaultextension=".lua",
            filetypes=[("Lua Files", "*.lua"), ("All Files", "*.*")],
            title="Save as Lua File"
        )
        if file_path:
            with open(file_path, "w") as file:
                file.write(textbox.get("1.0", tk.END).strip())
            messagebox.showinfo("Save Successful", f"File saved as: {file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while saving: {e}")

# Function to load content from a Lua file
def load_from_lua():
    try:
        file_path = filedialog.askopenfilename(
            filetypes=[("Lua Files", "*.lua"), ("All Files", "*.*")],
            title="Open Lua File"
        )
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
            textbox.delete("1.0", tk.END)
            textbox.insert("1.0", content)
            messagebox.showinfo("Load Successful", f"File loaded: {file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while loading: {e}")

# Main GUI
root = tk.Tk()
root.title("DusaSS V1.3")
root.geometry("600x400")  # Default size
root.configure(bg="gray")
root.overrideredirect(True)  # Remove window decorations
root.attributes('-topmost', True)  # Always on top

# HEADER (Custom title bar)
header = tk.Frame(root, bg="black", height=30)
header.pack(side="top", fill="x")

# Title label
title_label = tk.Label(header, text="DusaSS V1.3", bg="black", fg="white", font=("Arial", 12))
title_label.pack(side="left", padx=10)

# Close button
close_button = tk.Button(header, text="X", bg="black", fg="white", bd=0, font=("Arial", 12), command=close_window)
close_button.pack(side="right", padx=10)

# Draggable functionality for the custom header
header.bind("<Button-1>", start_drag)
header.bind("<B1-Motion>", drag_window)

# TEXTBOX
textbox = tk.Text(root, bg="darkgrey", fg="white", font=("Arial", 12), insertbackground="white", wrap="word", height=12)
textbox.pack(padx=20, pady=(20, 10), fill="x")

# BUTTON FRAME
button_frame = tk.Frame(root, bg="gray")
button_frame.pack(pady=(5, 20))

# Buttons
execute_button = ttk.Button(button_frame, text="Execute")
execute_button.pack(side="left", padx=10)

clear_button = ttk.Button(button_frame, text="Clear", command=lambda: textbox.delete("1.0", tk.END))
clear_button.pack(side="left", padx=10)

load_button = ttk.Button(button_frame, text="Load", command=load_from_lua)
load_button.pack(side="left", padx=10)

save_button = ttk.Button(button_frame, text="Save", command=save_as_lua)
save_button.pack(side="left", padx=10)

r6_button = ttk.Button(button_frame, text="R6")
r6_button.pack(side="left", padx=10)

# Attach button
attach_button = ttk.Button(button_frame, text="Attach", command=lambda: attach(attach_button))
attach_button.pack(side="left", padx=10)

root.mainloop()
