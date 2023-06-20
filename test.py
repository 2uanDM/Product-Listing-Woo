import tkinter as tk

root = tk.Tk()

# Define a function to be called when the state of the radiobuttons change


def on_radiobutton_change():
    print("Radio button 1 selected" if radio_var.get()
          == 1 else "Radio button 2 selected")


# Create a canvas and draw two rectangles for the radio buttons
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()
canvas.create_rectangle(100.0, 100.0, 120.0, 120.0, fill="#D9D9D9", outline="")
canvas.create_text(140, 110, text="Option 1")
canvas.create_rectangle(200.0, 100.0, 220.0, 120.0, fill="#D9D9D9", outline="")
canvas.create_text(240, 110, text="Option 2")

# Create a variable to store the state of the radiobuttons
radio_var = tk.IntVar()

# Create the Radiobuttons and set their position
radio_button_1 = tk.Radiobutton(
    root, text="", variable=radio_var, value=1, command=on_radiobutton_change)

radio_button_2 = tk.Radiobutton(
    root, text="", variable=radio_var, value=2, command=on_radiobutton_change)
radio_button_2_window = canvas.create_window(
    210, 110, anchor="nw", window=radio_button_2)

# Start the tkinter event loop
root.mainloop()
