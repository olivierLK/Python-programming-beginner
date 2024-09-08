import math
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator Program")
        self.root.geometry("300x300")

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(pady=10, expand=True)

        self.basic_frame = tk.Frame(self.notebook)
        self.trigonometric_frame = tk.Frame(self.notebook)
        self.hyperbolic_frame = tk.Frame(self.notebook)
        self.graph_frame = tk.Frame(self.notebook)

        self.notebook.add(self.basic_frame, text="Basic Operations")
        self.notebook.add(self.trigonometric_frame, text="Trigonometric Operations")
        self.notebook.add(self.hyperbolic_frame, text="Hyperbolic Trigonometric Operations")
        self.notebook.add(self.graph_frame, text="Graph")

        self.basic_operations()
        self.trigonometric_operations()
        self.hyperbolic_trigonometric_operations()
        self.graph_operations()

    def basic_operations(self):
        tk.Label(self.basic_frame, text="Basic Operations", font=("Arial", 16)).pack()

        tk.Button(self.basic_frame, text="Addition", command=self.addition).pack()
        tk.Button(self.basic_frame, text="Subtraction", command=self.subtraction).pack()
        tk.Button(self.basic_frame, text="Multiplication", command=self.multiplication).pack()
        tk.Button(self.basic_frame, text="Division", command=self.division).pack()

    def trigonometric_operations(self):
        tk.Label(self.trigonometric_frame, text="Trigonometric Operations", font=("Arial", 16)).pack()

        tk.Button(self.trigonometric_frame, text="Sine", command=self.sine).pack()
        tk.Button(self.trigonometric_frame, text="Cosine", command=self.cosine).pack()
        tk.Button(self.trigonometric_frame, text="Tangent", command=self.tangent).pack()

    def hyperbolic_trigonometric_operations(self):
        tk.Label(self.hyperbolic_frame, text="Hyperbolic Trigonometric Operations", font=("Arial", 16)).pack()

        tk.Button(self.hyperbolic_frame, text="Hyperbolic Sine", command=self.hyperbolic_sine).pack()
        tk.Button(self.hyperbolic_frame, text="Hyperbolic Cosine", command=self.hyperbolic_cosine).pack()
        tk.Button(self.hyperbolic_frame, text="Hyperbolic Tangent", command=self.hyperbolic_tangent).pack()
        tk.Button(self.hyperbolic_frame, text="Inverse Hyperbolic Sine", command=self.inverse_hyperbolic_sine).pack()
        tk.Button(self.hyperbolic_frame, text="Inverse Hyperbolic Cosine", command=self.inverse_hyperbolic_cosine).pack()
        tk.Button(self.hyperbolic_frame, text="Inverse Hyperbolic Tangent", command=self.inverse_hyperbolic_tangent).pack()

    def graph_operations(self):
        tk.Label(self.graph_frame, text="Graph", font=("Arial", 16)).pack()

        tk.Button(self.graph_frame, text="Sine Graph", command=self.sine_graph).pack()
        tk.Button(self.graph_frame, text="Cosine Graph", command=self.cosine_graph).pack()
        tk.Button(self.graph_frame, text="Tangent Graph", command=self.tangent_graph).pack()

    def addition(self):
        self.operation_window("Addition", lambda x, y: x + y)

    def subtraction(self):
        self.operation_window("Subtraction", lambda x, y: x - y)

    def multiplication(self):
        self.operation_window("Multiplication", lambda x, y: x * y)

    def division(self):
        self.operation_window("Division", lambda x, y: x / y if y != 0 else float('inf'))

    def sine(self):
        self.trigonometric_window("Sine", math.sin)

    def cosine(self):
        self.trigonometric_window("Cosine", math.cos)

    def tangent(self):
        self.trigonometric_window("Tangent", math.tan)

    def hyperbolic_sine(self):
        self.hyperbolic_window("Hyperbolic Sine", math.sinh)

    def hyperbolic_cosine(self):
        self.hyperbolic_window("Hyperbolic Cosine", math.cosh)

    def hyperbolic_tangent(self):
        self.hyperbolic_window("Hyperbolic Tangent", math.tanh)

    def inverse_hyperbolic_sine(self):
        self.hyperbolic_window("Inverse Hyperbolic Sine", math.asinh)

    def inverse_hyperbolic_cosine(self):
        self.hyperbolic_window("Inverse Hyperbolic Cosine", math.acosh)

    def inverse_hyperbolic_tangent(self):
        self.hyperbolic_window("Inverse Hyperbolic Tangent", math.atanh)

    def operation_window(self, title, operation):
        window = tk.Toplevel(self.root)
        window.title(title)

        tk.Label(window, text="Number 1:").pack()
        num1_entry = tk.Entry(window)
        num1_entry.pack()

        tk.Label(window, text="Number 2:").pack()
        num2_entry = tk.Entry(window)
        num2_entry.pack()

        def calculate():
            try:
                num1 = float(num1_entry.get())
                num2 = float(num2_entry.get())
                result = operation(num1, num2)
                messagebox.showinfo("Result", f"The result is {result}")
            except ValueError:
                messagebox.showerror("Error", "Invalid input")

        tk.Button(window, text="Calculate", command=calculate).pack()

    def trigonometric_window(self, title, operation):
        window = tk.Toplevel(self.root)
        window.title(title)

        tk.Label(window, text="Angle (in degrees):").pack()
        angle_entry = tk.Entry(window)
        angle_entry.pack()

        def calculate():
            try:
                angle = float(angle_entry.get())
                result = operation(math.radians(angle))
                messagebox.showinfo("Result", f"The result is {result}")
            except ValueError:
                messagebox.showerror("Error", "Invalid input")

        tk.Button(window, text="Calculate", command=calculate).pack()

    def hyperbolic_window(self, title, operation):
        window = tk.Toplevel(self.root)
        window.title(title)

        tk.Label(window, text="Number:").pack()
        num_entry = tk.Entry(window)
        num_entry.pack()

        def calculate():
            try:
                num = float(num_entry.get())
                result = operation(num)
                messagebox.showinfo("Result", f"The result is {result}")
            except ValueError:
                messagebox.showerror("Error", "Invalid input")

        tk.Button(window, text="Calculate", command=calculate).pack()

    def sine_graph(self):
        fig, ax = plt.subplots()
        x = [i for i in range(-360, 361)]
        y = [math.sin(math.radians(i)) for i in x]
        ax.plot(x, y)
        ax.set_title("Sine Graph")
        ax.set_xlabel("Degrees")
        ax.set_ylabel("Value")

        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()
        canvas.get_tk_widget().pack()

    def cosine_graph(self):
        fig, ax = plt.subplots()
        x = [i for i in range(-360, 361)]
        y = [math.cos(math.radians(i)) for i in x]
        ax.plot(x, y)
        ax.set_title("Cosine Graph")
        ax.set_xlabel("Degrees")
        ax.set_ylabel("Value")

        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()
        canvas.get_tk_widget().pack()

    def tangent_graph(self):
        fig, ax = plt.subplots()
        x = [i for i in range(-360, 361) if i != 90 and i != 270]
        y = [math.tan(math.radians(i)) for i in x]
        ax.plot(x, y)
        ax.set_title("Tangent Graph")
        ax.set_xlabel("Degrees")
        ax.set_ylabel("Value")

        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()
        canvas.get_tk_widget().pack()

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
