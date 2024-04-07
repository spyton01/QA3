import tkinter as tk
from tkinter import ttk

class WindowOne:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Category Selection")

        self.selected_category = tk.StringVar()

        # Create a label and ComboBox to select quiz category
        ttk.Label(self.root, text="Select Category:").pack(pady=10)
        self.category_combo = ttk.Combobox(self.root, width=30, textvariable=self.selected_category)
        self.category_combo['values'] = ["General Knowledge", "Science", "History", "Geography"]
        self.category_combo.pack(pady=10)

        # Create a button to start the quiz
        self.start_button = ttk.Button(self.root, text="Start Quiz Now", command=self.start_quiz)
        self.start_button.pack(pady=10)

    def start_quiz(self):
        selected_category = self.selected_category.get()
        self.root.destroy()  # Close the current window

        # Open the quiz window based on selected category
        quiz_window = tk.Tk()
        WindowTwo(quiz_window, selected_category)

class WindowTwo:
    def __init__(self, root, category):
        self.root = root
        self.root.title(f"Quiz: {category}")

        # Placeholder: Display quiz questions based on category
        ttk.Label(self.root, text=f"Quiz Category: {category}").pack(pady=10)
        ttk.Label(self.root, text="Question 1: What is the capital of France?").pack(pady=5)
        ttk.Label(self.root, text="A. London").pack()
        ttk.Label(self.root, text="B. Paris").pack()
        ttk.Label(self.root, text="C. Rome").pack()
        ttk.Label(self.root, text="D. Berlin").pack()

if __name__ == "__main__":
    # Create the main window (Category Selection)
    root = tk.Tk()
    app_one = WindowOne(root)

    # Start the Tkinter event loop
    root.mainloop()