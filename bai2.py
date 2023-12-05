import tkinter as tk
from tkinter import scrolledtext
from sympy import symbols, diff, integrate, simplify

class MathToolApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Math Tool")

        # Tạo khung nhập biểu thức
        self.expression_entry = tk.Entry(self.root, width=30)
        self.expression_entry.pack(pady=10)

        # Tạo nút "Đạo hàm"
        self.derivative_button = tk.Button(self.root, text="Đạo hàm", command=self.compute_derivative)
        self.derivative_button.pack(pady=5)

        # Tạo nút "Nguyên hàm"
        self.integral_button = tk.Button(self.root, text="Nguyên hàm", command=self.compute_integral)
        self.integral_button.pack(pady=5)

        # Tạo nút "Tích phân"
        self.integration_button = tk.Button(self.root, text="Tích phân", command=self.compute_integration)
        self.integration_button.pack(pady=5)

        # Tạo khung hiển thị kết quả
        self.result_frame = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=40, height=10)
        self.result_frame.pack(pady=10)

    def compute_derivative(self):
        expression = self.expression_entry.get()
        x = symbols('x')

        try:
            function = simplify(expression)
            derivative = diff(function, x)
            result_text = f"Đạo hàm của {expression} là: {derivative}"
        except Exception as e:
            result_text = f"Lỗi: {e}"

        self.display_result(result_text)

    def compute_integral(self):
        expression = self.expression_entry.get()
        x = symbols('x')

        try:
            function = simplify(expression)
            integral = integrate(function, x)
            result_text = f"Nguyên hàm của {expression} là: {integral}"
        except Exception as e:
            result_text = f"Lỗi: {e}"

        self.display_result(result_text)

    def compute_integration(self):
        expression = self.expression_entry.get()
        x = symbols('x')

        try:
            function = simplify(expression)
            integration = integrate(function, x)
            result_text = f"Tích phân của {expression} là: {integration}"
        except Exception as e:
            result_text = f"Lỗi: {e}"

        self.display_result(result_text)

    def display_result(self, text):
        self.result_frame.delete(1.0, tk.END)
        self.result_frame.insert(tk.END, text)

if __name__ == "__main__":
    root = tk.Tk()
    app = MathToolApp(root)
    root.mainloop()
