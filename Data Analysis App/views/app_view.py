import tkinter as tk
from tkinter import filedialog

def create_main_window(controller):
    window = tk.Tk()
    window.title("Data Analysis App")

    upload_btn = tk.Button(window, text="Upload File", command=controller.load_file)
    upload_btn.pack()
    
    display_area = tk.Text(window)
    display_area.pack()

    export_btn = tk.Button(window, text="Export Results", command=controller.export_data)
    export_btn.pack()

    return window, display_area
