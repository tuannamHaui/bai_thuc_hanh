import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import numpy as np
import math

class GeometryCalculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Học Hình Học")

        # Tạo một LabelFrame cho các hình học
        self.geometry_frame = ttk.LabelFrame(master, text="Các Hình Học")
        self.geometry_frame.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W+tk.E+tk.N+tk.S)

        # Tạo một Label và Combobox để chọn hình học
        ttk.Label(self.geometry_frame, text="Chọn Hình Học:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.shape_var = tk.StringVar()
        self.shape_combobox = ttk.Combobox(self.geometry_frame, textvariable=self.shape_var, values=["Hình Vuông", "Hình Chữ Nhật", "Hình Tròn", "Hình Tam Giác"])
        self.shape_combobox.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
        self.shape_combobox.bind("<<ComboboxSelected>>", self.update_labels)

        # Tạo các Label và Entry để nhập kích thước tương ứng
        ttk.Label(self.geometry_frame, text="Kích Thước 1:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.dimension_label1 = ttk.Label(self.geometry_frame, text="Kích Thước 1:")
        self.dimension_label1.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.dimension_entry1 = ttk.Entry(self.geometry_frame)
        self.dimension_entry1.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

        # Các Label và Entry cho Kích Thước 2 (hoặc Bán Kính) và Kích Thước 3 (cho Hình Tam Giác)
        self.dimension_label2 = ttk.Label(self.geometry_frame, text="Kích Thước 2:")
        self.dimension_entry2 = ttk.Entry(self.geometry_frame)
        self.dimension_label3 = ttk.Label(self.geometry_frame, text="Kích Thước 3:")
        self.dimension_entry3 = ttk.Entry(self.geometry_frame)

        # Tạo một Button để tính toán diện tích và chu vi
        ttk.Button(self.geometry_frame, text="Tính Toán", command=self.calculate).grid(row=4, column=0, columnspan=2, pady=10)

    def update_labels(self, event):
        selected_shape = self.shape_var.get()
        if selected_shape == "Hình Vuông":
            self.dimension_label1["text"] = "Kích Thước:"
            self.dimension_label2.grid_forget()
            self.dimension_entry2.grid_forget()
            self.dimension_label3.grid_forget()
            self.dimension_entry3.grid_forget()
        elif selected_shape == "Hình Tròn":
            self.dimension_label1["text"] = "Bán Kính:"
            self.dimension_label2.grid_forget()
            self.dimension_entry2.grid_forget()
            self.dimension_label3.grid_forget()
            self.dimension_entry3.grid_forget()
        elif selected_shape == "Hình Tam Giác":
            self.dimension_label1["text"] = "Kích Thước 1:"
            self.dimension_label2.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
            self.dimension_entry2.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)
            self.dimension_label3.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
            self.dimension_entry3.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)
        else:
            self.dimension_label1["text"] = "Kích Thước 1:"
            self.dimension_label2.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
            self.dimension_entry2.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)
            self.dimension_label3.grid_forget()
            self.dimension_entry3.grid_forget()

    def calculate(self):
        shape = self.shape_var.get()
        dimension1 = self.dimension_entry1.get()
        dimension2 = self.dimension_entry2.get()
        dimension3 = self.dimension_entry3.get()

        try:
            dimension1 = float(dimension1)
            dimension2 = float(dimension2)
            dimension3 = float(dimension3)
        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập số cho kích thước.")
            return

        if shape == "Hình Vuông":
            area = dimension1 ** 2
            perimeter = 4 * dimension1
        elif shape == "Hình Chữ Nhật":
            area = dimension1 * dimension2
            perimeter = 2 * (dimension1 + dimension2)
        elif shape == "Hình Tròn":
            area = math.pi * (dimension1 ** 2)
            perimeter = 2 * math.pi * dimension1
        elif shape == "Hình Tam Giác":
            s = (dimension1 + dimension2 + dimension3) / 2
            area = math.sqrt(s * (s - dimension1) * (s - dimension2) * (s - dimension3))
            perimeter = dimension1 + dimension2 + dimension3
        else:
            messagebox.showerror("Lỗi", "Hình học không được hỗ trợ.")
            return

        result_text = f"Diện tích {shape}: {area:.2f}\nChu vi {shape}: {perimeter:.2f}"
        messagebox.showinfo("Kết Quả", result_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = GeometryCalculator(root)
    root.mainloop()
