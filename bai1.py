import numpy as np
import tkinter as tk
from tkinter import Label, Entry, Button, StringVar

class LinearEquationSolverApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Linear Equation Solver App")

        self.so_phuong_trinh_var = StringVar()
        self.so_phuong_trinh_var.set("2")  # Số mặc định là 2

        self.frame = tk.Frame(self.master)
        self.frame.pack(padx=10, pady=10)

        Label(self.frame, text="Số phương trình:").grid(row=0, column=0)
        Entry(self.frame, textvariable=self.so_phuong_trinh_var).grid(row=0, column=1)

        self.btn_create_entries = Button(self.frame, text="Tạo Hệ số", command=self.create_entries)
        self.btn_create_entries.grid(row=1, column=0, columnspan=2, pady=5)

        self.result_label = Label(self.master, text="")
        self.result_label.pack(pady=10)

    def create_entries(self):
        try:
            so_phuong_trinh = int(self.so_phuong_trinh_var.get())
            so_bien = so_phuong_trinh  # Số biến bằng số phương trình

            self.entries = []

            for i in range(so_phuong_trinh):
                row = 2 + i
                Label(self.frame, text=f"Hệ số phương trình {i + 1}:").grid(row=row, column=0)
                entries_row = []
                for j in range(so_bien):
                    entry = Entry(self.frame)
                    entry.grid(row=row, column=j + 1)
                    entries_row.append(entry)
                self.entries.append(entries_row)

            self.btn_solve = Button(self.master, text="Giải", command=self.solve_equations)
            self.btn_solve.pack(pady=10)

        except ValueError:
            self.result_label.config(text="Vui lòng nhập số nguyên cho số phương trình.")

    def solve_equations(self):
        try:
            he_so = []
            tu_do = []

            for i, row in enumerate(self.entries):
                he_so_phuong_trinh = [float(entry.get()) for entry in row]
                he_so.append(he_so_phuong_trinh)
                tu_do_phuong_trinh = float(input(f"Hệ số tự do của phương trình {i + 1}: "))
                tu_do.append(tu_do_phuong_trinh)

            ket_qua = self.giai_he_phuong_trinh(he_so, tu_do)

            if ket_qua is not None:
                result_text = "\nKết quả:\n"
                for i, bien in enumerate(ket_qua):
                    result_text += f"Biến {i + 1}: {bien}\n"
                self.result_label.config(text=result_text)
            else:
                self.result_label.config(text="\nHệ phương trình không xác định hoặc không có nghiệm duy nhất.")

        except ValueError:
            self.result_label.config(text="Vui lòng nhập số thực cho các hệ số và hệ số tự do.")

    def giai_he_phuong_trinh(self, coefficients, constants):
        try:
            he_so_matrix = np.array(coefficients)
            he_so_tu_do = np.array(constants)
            ket_qua = np.linalg.solve(he_so_matrix, he_so_tu_do)
            return ket_qua
        except np.linalg.LinAlgError:
            return None

if __name__ == "__main__":
    root = tk.Tk()
    app = LinearEquationSolverApp(root)
    root.geometry("400x400")
    root.mainloop()
    