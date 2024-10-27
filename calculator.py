import tkinter as tk

# Initialize the main window
root = tk.Tk()
root.title("Stylish Calculator")
root.geometry("400x600")
root.config(bg="#2c2f33")

# Define styles
button_font = ("Arial", 18)
input_font = ("Arial", 24)

# Create input display
display_var = tk.StringVar()
display_entry = tk.Entry(root, textvariable=display_var, font=input_font, bg="#202225", fg="white", bd=0, justify="right")
display_entry.grid(row=0, column=0, columnspan=4, ipady=20, padx=10, pady=10, sticky="nsew")

# Button press event
def button_press(value):
    if value == "=":
        try:
            result = str(eval(display_var.get()))
            display_var.set(result)
        except Exception as e:
            display_var.set("Error")
    elif value == "C":
        display_var.set("")
    else:
        display_var.set(display_var.get() + value)

# Define button layout and style
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", "C", "=", "+"]
]

for i, row in enumerate(buttons, start=1):
    for j, button_text in enumerate(row):
        button = tk.Button(root, text=button_text, font=button_font, bg="#7289da", fg="white", activebackground="#99aab5",
                           command=lambda x=button_text: button_press(x))
        button.grid(row=i, column=j, sticky="nsew", padx=5, pady=5, ipadx=10, ipady=20)

# Configure layout to be responsive
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

root.mainloop()
