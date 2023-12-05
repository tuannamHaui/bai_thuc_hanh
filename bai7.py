import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageSmoothingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Image Smoothing App")

        self.frame = tk.Frame(self.master)
        self.frame.pack(padx=10, pady=10)

        self.label_original = tk.Label(self.frame)
        self.label_original.pack(side=tk.LEFT, padx=10)

        self.label_smoothed = tk.Label(self.frame)
        self.label_smoothed.pack(side=tk.LEFT, padx=10)

        self.btn_open = tk.Button(self.master, text="Open Image", command=self.open_image)
        self.btn_open.pack(pady=5)

        self.btn_smooth = tk.Button(self.master, text="Smooth Image", command=self.smooth_image)
        self.btn_smooth.pack(pady=5)

        self.image_path = ""
        self.image = None
        self.smoothed_image = None
        self.display_original = False

    def open_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Images", "*.png;*.jpg;*.bmp;*.jpeg")])
        if file_path:
            self.image_path = file_path
            self.image = cv2.imread(file_path)
            self.display_image()

    def display_image(self):
        if self.image is not None:
            if self.display_original:
                image_original = Image.fromarray(cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB))
                image_original = ImageTk.PhotoImage(image_original)
                self.label_original.configure(image=image_original)
                self.label_original.image = image_original
            else:
                self.label_original.configure(image=None)

    def smooth_image(self):
        if self.image is not None:
            # Apply smoothing (GaussianBlur)
            self.smoothed_image = cv2.GaussianBlur(self.image, (5, 5), 0)

            # Display the original and smoothed images
            self.display_original = True
            self.display_image()
            self.display_smoothed()

    def display_smoothed(self):
        if self.smoothed_image is not None:
            image_smoothed = Image.fromarray(cv2.cvtColor(self.smoothed_image, cv2.COLOR_BGR2RGB))
            image_smoothed = ImageTk.PhotoImage(image_smoothed)
            self.label_smoothed.configure(image=image_smoothed)
            self.label_smoothed.image = image_smoothed

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageSmoothingApp(root)
    root.geometry("800x400")
    root.mainloop()
