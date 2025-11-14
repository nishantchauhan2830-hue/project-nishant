import tkinter as tk

# Function to update the expression in the entry widget
def press(key):
    entry_var.set(entry_var.get() + str(key))

# Function to evaluate expression
def equalpress():
    try:
        result = str(eval(entry_var.get()))
        entry_var.set(result)
    except:
        entry_var.set("Error")

# Function to clear entry
def clear():
    entry_var.set("")

# Create main window
root = tk.Tk()
root.title("Basic Calculator")
root.geometry("300x400")

# Entry widget
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20),
                 bd=10, relief="sunken", justify="right")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=15, pady=10)

# Button layout list
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Create buttons
for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, font=("Arial", 18), height=2,
                        width=5, bg="lightgreen", command=equalpress)
    else:
        btn = tk.Button(root, text=text, font=("Arial", 18), height=2,
                        width=5, command=lambda t=text: press(t))

    btn.grid(row=row, column=col, padx=5, pady=5)

# Clear button (C)
clear_btn = tk.Button(root, text="C", font=("Arial", 18),
                      height=2, width=22, bg="lightcoral", command=clear)
clear_btn.grid(row=5, column=0, columnspan=4, padx=5, pady=5)

# Run application
root.mainloop()