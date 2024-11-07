import tkinter as tk
from tkinter import filedialog  # Add this import for filedialog functionality
from services import file_service
from models import data_handler

class AppController:
    def __init__(self, display_area):
        self.display_area = display_area
        self.data = None

    def load_file(self):
        # Use filedialog to open a file selection dialog
        file_path = filedialog.askopenfilename()
         # Add logic here to handle file loading and display
        if file_path:
            data = file_service.load_data(file_path)
            self.display_area.insert("1.0", str(data))  # Display the data
        self.show_summary()

    def show_summary(self):
        summary = data_handler.summarize_data(self.data)
        self.display_area.insert(tk.END, str(summary))

    def export_data(self):
        with open("summary.txt", "w") as f:
            f.write(str(self.display_area.get("1.0", tk.END)))
