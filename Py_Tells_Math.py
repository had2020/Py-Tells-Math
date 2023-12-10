# Importing the Tkinter and math modules
import tkinter as tk
import math

# Creating the main window
root = tk.Tk()
root.title("Py_Tells_Time")
root.geometry("400x250")

# Creating the display entry
display = tk.Entry(root, font=("Arial", 20), justify="right")
display.pack(padx=10, pady=10)

# Creating the buttons frame
buttons = tk.Frame(root)
buttons.pack()

# Defining the functions for the calculator
def insert(text):
    # Inserts the text at the cursor position
    display.insert(tk.INSERT, text)

def delete():
    # Deletes the character before the cursor
    display.delete(display.index(tk.INSERT) - 1)

def clear():
    # Clears the display
    display.delete(0, tk.END)

def evaluate():
    # Evaluates the expression in the display
    try:
        result = eval(display.get())
        clear()
        insert(result)
    except Exception as e:
        clear()
        insert("Error: " + str(e))

def factorial(n):
    # Returns the factorial of n
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def sin(x):
    # Returns the sine of x in radians
    return math.sin(x)

def cos(x):
    # Returns the cosine of x in radians
    return math.cos(x)

def tan(x):
    # Returns the tangent of x in radians
    return math.tan(x)

def log(x):
    # Returns the natural logarithm of x
    return math.log(x)

def sqrt(x):
    # Returns the square root of x
    return math.sqrt(x)

def power(x, y):
    # Returns x raised to the power of y
    return math.pow(x, y)

# Creating the buttons
btn_1 = tk.Button(buttons, text="1", font=("Arial", 20), command=lambda: insert("1"))
btn_2 = tk.Button(buttons, text="2", font=("Arial", 20), command=lambda: insert("2"))
btn_3 = tk.Button(buttons, text="3", font=("Arial", 20), command=lambda: insert("3"))
btn_4 = tk.Button(buttons, text="4", font=("Arial", 20), command=lambda: insert("4"))
btn_5 = tk.Button(buttons, text="5", font=("Arial", 20), command=lambda: insert("5"))
btn_6 = tk.Button(buttons, text="6", font=("Arial", 20), command=lambda: insert("6"))
btn_7 = tk.Button(buttons, text="7", font=("Arial", 20), command=lambda: insert("7"))
btn_8 = tk.Button(buttons, text="8", font=("Arial", 20), command=lambda: insert("8"))
btn_9 = tk.Button(buttons, text="9", font=("Arial", 20), command=lambda: insert("9"))
btn_0 = tk.Button(buttons, text="0", font=("Arial", 20), command=lambda: insert("0"))
btn_dot = tk.Button(buttons, text=".", font=("Arial", 20), command=lambda: insert("."))
btn_plus = tk.Button(buttons, text="+", font=("Arial", 20), command=lambda: insert("+"))
btn_minus = tk.Button(buttons, text="-", font=("Arial", 20), command=lambda: insert("-"))
btn_mul = tk.Button(buttons, text="*", font=("Arial", 20), command=lambda: insert("*"))
btn_div = tk.Button(buttons, text="/", font=("Arial", 20), command=lambda: insert("/"))
btn_mod = tk.Button(buttons, text="%", font=("Arial", 20), command=lambda: insert("%"))
btn_pow = tk.Button(buttons, text="^", font=("Arial", 20), command=lambda: insert("**"))
btn_del = tk.Button(buttons, text="DEL", font=("Arial", 20), command=delete)
btn_clr = tk.Button(buttons, text="CLR", font=("Arial", 20), command=clear)
btn_eql = tk.Button(buttons, text="=", font=("Arial", 20), command=evaluate)
btn_sin = tk.Button(buttons, text="sin", font=("Arial", 20), command=lambda: insert("sin("))
btn_cos = tk.Button(buttons, text="cos", font=("Arial", 20), command=lambda: insert("cos("))
btn_tan = tk.Button(buttons, text="tan", font=("Arial", 20), command=lambda: insert("tan("))
btn_log = tk.Button(buttons, text="log", font=("Arial", 20), command=lambda: insert("log("))
btn_sqrt = tk.Button(buttons, text="sqrt", font=("Arial", 20), command=lambda: insert("sqrt("))
btn_fact = tk.Button(buttons, text="!", font=("Arial", 20), command=lambda: insert("factorial("))
btn_lpar = tk.Button(buttons, text="(", font=("Arial", 20), command=lambda: insert("("))
btn_rpar = tk.Button(buttons, text=")", font=("Arial", 20), command=lambda: insert(")"))

# Arranging the buttons in a grid
btn_1.grid(row=0, column=0, padx=5, pady=5)
btn_2.grid(row=0, column=1, padx=5, pady=5)
btn_3.grid(row=0, column=2, padx=5, pady=5)
btn_4.grid(row=1, column=0, padx=5, pady=5)
btn_5.grid(row=1, column=1, padx=5, pady=5)
btn_6.grid(row=1, column=2, padx=5, pady=5)
btn_7.grid(row=2, column=0, padx=5, pady=5)
btn_8.grid(row=2, column=1, padx=5, pady=5)
btn_9.grid(row=2, column=2, padx=5, pady=5)
btn_0.grid(row=3, column=0, padx=5, pady=5)
btn_dot.grid(row=3, column=1, padx=5, pady=5)
btn_plus.grid(row=0, column=3, padx=5, pady=5)
btn_minus.grid(row=1, column=3, padx=5, pady=5)
btn_mul.grid(row=2, column=3, padx=5, pady=5)
btn_div.grid(row=3, column=3, padx=5, pady=5)
btn_mod.grid(row=0, column=4, padx=5, pady=5)
btn_pow.grid(row=1, column=4, padx=5, pady=5)
btn_del.grid(row=2, column=4, padx=5, pady=5)
btn_clr.grid(row=3, column=4, padx=5, pady=5)
btn_eql.grid(row=3, column=2, padx=5, pady=5)
btn_sin.grid(row=0, column=5, padx=5, pady=5)
btn_cos.grid(row=1, column=5, padx=5, pady=5)
btn_tan.grid(row=2, column=5, padx=5, pady=5)
btn_log.grid(row=3, column=5, padx=5, pady=5)
btn_sqrt.grid(row=0, column=6, padx=5, pady=5)
btn_fact.grid(row=1, column=6, padx=5, pady=5)
btn_lpar.grid(row=2, column=6, padx=5, pady=5)
btn_rpar.grid(row=3, column=6, padx=5, pady=5)

# Starting the main loop
root.mainloop()
