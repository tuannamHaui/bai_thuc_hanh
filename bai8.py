import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageEdgeDetectionApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Image Edge Detection App")

        self.frame = tk.Frame(self.master)
        self.frame.pack(padx=10, pady=10)

        self.label_original = tk.Label(self.frame)
        self.label_original.pack(side=tk.LEFT, padx=10)

        self.label_edges = tk.Label(self.frame)
        self.label_edges.pack(side=tk.LEFT, padx=10)

        self.btn_open = tk.Button(self.master, text="Open Image", command=self.open_image)
        self.btn_open.pack(pady=5)

        self.btn_detect_edges = tk.Button(self.master, text="Detect Edges", command=self.detect_edges)
        self.btn_detect_edges.pack(pady=5)

        self.image_path = ""
        self.image = None
        self.edges = None
        self.display_original = False

    def open_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Images", "*.png;*.jpg;*.bmp;*.jpeg")])
        if file_path:
            self.image_path = file_path
            self.image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
            self.display_image()

    def display_image(self):
        if self.image is not None:
            if self.display_original:
                image_original = Image.fromarray(self.image)
                image_original = ImageTk.PhotoImage(image_original)
                self.label_original.configure(image=image_original)
                self.label_original.image = image_original
            else:
                self.label_original.configure(image=None)

    def detect_edges(self):
        if self.image is not None:
            # Apply Canny Edge Detection
            self.edges = cv2.Canny(self.image, 50, 150)

            # Display the original and edge-detected images
            self.display_original = True
            self.display_image()
            self.display_edges()

    def display_edges(self):
        if self.edges is not None:
            image_edges = Image.fromarray(self.edges)
            image_edges = ImageTk.PhotoImage(image_edges)
            self.label_edges.configure(image=image_edges)
            self.label_edges.image = image_edges

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEdgeDetectionApp(root)
    root.geometry("800x400")
    root.mainloop()
