import tkinter as tk
from tkinter import filedialog
from PIL import Image
from pytesseract import pytesseract
import pyttsx3
import os

class Reader:
    def __init__(self, master):
        self.master = master
        self.master.title("Photo Reader")

        # Create a menu bar
        menubar = tk.Menu(self.master)
        self.master.config(menu=menubar)

        # Create a File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Exit", command=self.exit_app)
        menubar.add_cascade(label="File", menu=file_menu)

        # Create a Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        menubar.add_cascade(label="Help", menu=help_menu)

        # Create new feature of text reader
        new_menu = tk.Menu(menubar, tearoff=0)
        new_menu.add_command(label="Speaker", command=self.new)
        menubar.add_cascade(label="More", menu=new_menu)

        # Set initial status text
        self.status_text = tk.StringVar()
        self.status_text.set("No file selected")
        self.status_label = tk.Label(self.master, textvariable=self.status_text)
        self.status_label.pack(side=tk.BOTTOM, padx=5, pady=5)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.status_text.set("Selected file: " + os.path.basename(file_path))
            # Perform further processing with the selected file, e.g., OCR using pytesseract.
            image_path = file_path
            img = Image.open(image_path)
            path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
            pytesseract.tesseract_cmd = path_to_tesseract
            text = pytesseract.image_to_string(img)
            a = text[:-1]
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id)
            engine.say(a)
            engine.runAndWait()


    def exit_app(self):
        self.master.destroy()

    def show_about(self):
        about_text = "Photo Reader App\nVersion 1.0\n\nThis app is developed by Er. Harsh Raj, this app allows you to open an image file and extract text from it."
        tk.messagebox.showinfo("About", about_text)

    def new(self):
        def spkf():
            text = e1.get()
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id)
            engine.say(text)
            engine.runAndWait()

        l1 = tk.Label(self.master,text = "Enter anything to listen:")
        l1.pack()
        e1 = tk.Entry(self.master,width=20)
        e1.pack()
        b1 = tk.Button(self.master,text = "Speak", command = spkf)
        b1.pack()
        self.master.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("250x100")
    reader = Reader(root)
    root.mainloop()
