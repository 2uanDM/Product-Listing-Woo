import tkinter as tk


def mode_selected(selected_mode):
    if selected_mode == "Basic":
        # Hide advanced options
        option_label.pack_forget()
        option_entry.pack_forget()
        option_button.pack_forget()

        # Show basic options
        basic_label.pack()
        basic_entry.pack()
        basic_button.pack()
    elif selected_mode == "Advanced":
        # Hide basic options
        basic_label.pack_forget()
        basic_entry.pack_forget()
        basic_button.pack_forget()

        # Show advanced options
        option_label.pack()
        option_entry.pack()
        option_button.pack()


root = tk.Tk()

# Mode selection dropdown
modes = ["Basic", "Advanced"]
selected_mode = tk.StringVar(root)
selected_mode.set(modes[0])  # Default mode
mode_dropdown = tk.OptionMenu(
    root, selected_mode, *modes, command=mode_selected)
mode_dropdown.pack()

# Basic options
basic_label = tk.Label(root, text="Basic Option:")
basic_label.pack()
basic_entry = tk.Entry(root)
basic_entry.pack()
basic_button = tk.Button(root, text="Basic Button")
basic_button.pack()

# Advanced options (Initially hidden)
option_label = tk.Label(root, text="Advanced Option:")
option_entry = tk.Entry(root)
option_button = tk.Button(root, text="Advanced Button")

root.mainloop()
