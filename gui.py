import tkinter as tk
from tkinter import filedialog
import subprocess
import sys

class CustomUI:
    def __init__(self, master):
        self.master = master
        master.title("Custom UI for ChatGPT")

        self.label_query = tk.Label(master, text="Enter your query:")
        self.label_query.pack()

        self.query_entry = tk.Entry(master)
        self.query_entry.pack()

        self.browse_button = tk.Button(master, text="Browse Data File", command=self.browse_data_file)
        self.browse_button.pack()

        self.run_button = tk.Button(master, text="Run", command=self.run_script)
        self.run_button.pack()

        self.label_output = tk.Label(master, text="Output:")
        self.label_output.pack()

        self.output_text = tk.Text(master, height=10, width=50)
        self.output_text.pack()

    def browse_data_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            self.data_file_path = file_path
            print(f"Selected data file: {file_path}")

    def run_script(self):
        if not hasattr(self, 'data_file_path'):
            print("Please select a data file first.")
            return

        query = self.query_entry.get()
        if not query:
            print("Please enter a query.")
            return

        # Use sys.executable to get the path to the Python executable
        python_executable = sys.executable
        script_path = r"C:\Users\Subhang Ladha\OneDrive\Desktop\local gpt\chatgpt.py"  # Replace with the actual path
        script_command = [python_executable, script_path, query]

        try:
            output = subprocess.check_output(script_command, shell=False, text=True)

            # Update the Text widget with the output
            self.output_text.delete(1.0, tk.END)  # Clear previous content
            self.output_text.insert(tk.END, output)
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    ui = CustomUI(root)
    root.mainloop()
