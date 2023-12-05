import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageEnhance

class ImageEnhancementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Enhancement")

        # Tạo nút để chọn ảnh
        self.select_image_button = tk.Button(root, text="Chọn ảnh", command=self.select_image)
        self.select_image_button.pack(pady=10)

        # Hiển thị ảnh gốc
        self.original_image_label = tk.Label(root, text="Ảnh gốc")
        self.original_image_label.pack()

        # Hiển thị ảnh sau khi tăng cường chất lượng
        self.enhanced_image_label = tk.Label(root, text="Ảnh tăng cường chất lượng")
        self.enhanced_image_label.pack()

    def select_image(self):
        file_path = filedialog.askopenfilename(title="Chọn ảnh", filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])

        if file_path:
            original_image = Image.open(file_path)

            # Hiển thị ảnh gốc
            self.display_image(original_image, self.original_image_label)

            # Tăng cường chất lượng ảnh
            enhanced_image = self.enhance_image(original_image)

            # Hiển thị ảnh sau khi tăng cường chất lượng
            self.display_image(enhanced_image, self.enhanced_image_label)

    def enhance_image(self, image):
        # Tăng cường độ sáng của ảnh
        enhancer = ImageEnhance.Brightness(image)
        enhanced_image = enhancer.enhance(1.5)  # 1.5 là hệ số tăng cường độ sáng, có thể điều chỉnh

        return enhanced_image

    def display_image(self, image, label):
        # Chuyển đổi ảnh thành định dạng hình ảnh mà Tkinter có thể hiểu
        tk_image = ImageTk.PhotoImage(image)

        # Hiển thị ảnh trong label
        label.config(image=tk_image)
        label.image = tk_image  # Giữ tham chiếu đến hình ảnh để tránh bị thu hồi bởi garbage collector

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEnhancementApp(root)
    root.mainloop()
