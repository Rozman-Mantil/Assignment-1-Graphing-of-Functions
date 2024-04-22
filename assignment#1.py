#Rozman Mantil
#A code that plots each function individually
import numpy as np
import matplotlib.pyplot as plt

functions = [
    "x**2 - 10",
    "x**2 + x - 100",
    "x**10 - x**8 + x**2 - 8",
    "x**4 + x**3 + x**2 + x + 1",
    "(x**2 + x + 10) / (2*x)",
    "np.sin(x) / (3*x)",
    "x**3 + 2*x**2 - 10*x + 3",
    "np.cos(x) / (5*x)",
    "(x**3) / (2*x) - 10*x",
    "(x + 2) * (x + 3) * (x - 4)"
]

x_values = np.linspace(-10, 10, 1000)

for i, func in enumerate(functions):
    plt.figure(figsize=(8, 6))
    try:
        y_values = eval(func, {'__builtins__': None}, {'x': x_values})
        plt.plot(x_values, y_values, label=func)
        plt.title("Plot of Function " + str(i+1) + ": " + func)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid(True)
        plt.legend()
        plt.show()
    except Exception as e:
        print("Error evaluating function:", e)
