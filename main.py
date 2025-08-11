# from random import choices
# import subprocess
# import platform

# words = []
# with open('words.txt', 'r', encoding='utf-8') as file:
#     for line in file:
#         words.append(line.strip())

# word_count = input('12 or 24?')
# random_words = ""
# if word_count == '12': random_words = ' '.join(choices(words, k=12))
# elif word_count == '24': random_words = ' '.join(choices(words, k=24))
# else: raise ValueError("Invalid Input!")

# # Copying to clipboard based on each platform (Windows, Linux, Mac)
# system = platform.system()
# if system == "Windows":
#     subprocess.run('clip', text=True, input=random_words)
# elif system == "Darwin":
#     subprocess.run('pbcopy', text=True, input=random_words)
# elif system == "Linux":
#     subprocess.run(['xclip', '-selection', 'clipboard'], text=True, input=random_words)

# print('Copied to clipboard!')
# print(random_words)

import tkinter as tk
from tkinter import ttk, messagebox
from random import choices
import subprocess
import platform

class WordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Word Generator")
        self.root.geometry("400x300")
        
        try:
            self.words = []
            with open('words.txt', 'r', encoding='utf-8') as file:
                for line in file:
                    self.words.append(line.strip())
        except FileNotFoundError:
            messagebox.showerror("Error", "words.txt not found! Ensure the file is in the correct directory.")
            self.root.destroy()
            return

        self.label = ttk.Label(root, text="Select number of words:")
        self.label.pack(pady=10)

        self.word_count_var = tk.StringVar(value="12")
        self.word_count_menu = ttk.Combobox(root, textvariable=self.word_count_var, values=["12", "24"], state="readonly")
        self.word_count_menu.pack(pady=5)

        self.generate_button = ttk.Button(root, text="Generate", command=self.generate_words)
        self.generate_button.pack(pady=10)

        self.text_area = tk.Text(root, height=4, width=40, wrap="word")
        self.text_area.pack(pady=10)
        self.text_area.config(state="disabled")

        self.copy_button = ttk.Button(root, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_button.pack(pady=5)

        self.footer_label = ttk.Label(root, text="made by Ehsan (telegram: @bnshee_irl)", font=("Arial", 8))
        self.footer_label.pack(pady=22)

        self.random_words = ""

    def generate_words(self):
        word_count = self.word_count_var.get()
        if word_count not in ["12", "24"]:
            messagebox.showerror("Error", "Select either 12 or 24!")
            return
        
        self.random_words = ' '.join(choices(self.words, k=int(word_count)))
        self.text_area.config(state="normal")
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, self.random_words)
        self.text_area.config(state="disabled")

    def copy_to_clipboard(self):
        if not self.random_words:
            messagebox.showwarning("Warning", "Generate words first!")
            return
        
        system = platform.system()
        try:
            if system == "Windows":
                subprocess.run('clip', text=True, input=self.random_words)
            elif system == "Darwin":
                subprocess.run('pbcopy', text=True, input=self.random_words)
            elif system == "Linux":
                subprocess.run(['xclip', '-selection', 'clipboard'], text=True, input=self.random_words)
            messagebox.showinfo("Success", "Words copied to clipboard!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = WordGeneratorApp(root)
    root.mainloop()