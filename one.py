import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

class WindowOne:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Category Selection")

        self.selected_category = tk.StringVar()

        ttk.Label(self.root, text="Select Category:").pack(pady=20)
        self.category_combo = ttk.Combobox(self.root, width=30, textvariable=self.selected_category)
        self.category_combo['values'] = ["OCM Logistic", "Modern History", "Finance", "Business Analytics", "Prog Logic"]
        self.category_combo.pack(pady=10)

        self.start_button = ttk.Button(self.root, text="Start Quiz Now", command=self.start_quiz)
        self.start_button.pack(pady=10)

    def start_quiz(self):
        selected_category = self.selected_category.get()
        if selected_category:
            self.root.destroy()

            quiz_window = tk.Tk()
            quiz_window.title(f"Quiz: {selected_category}")
            quiz_window.geometry("600x400")

            WindowTwo(quiz_window, selected_category)

class WindowTwo:
    def __init__(self, root, category):
        self.root = root
        self.category = category

        self.conn = sqlite3.connect('QuestionsAnswer1.db')
        self.cursor = self.conn.cursor()

        self.cursor.execute(f"SELECT * FROM {self.category.replace(' ', '_')}")
        self.questions = self.cursor.fetchall()
        self.current_question_index = 0
        self.score = 0  # Initialize score counter

        self.setup_ui()

    def setup_ui(self):
        self.question_label = ttk.Label(self.root, text="", wraplength=500)
        self.question_label.pack(pady=20)

        self.answer_var = tk.StringVar()
        self.answer_var.set("")  # Initialize answer variable

        self.answer_buttons = []  # List to store Radiobuttons

        # Display answer choices (A, B, C) with corresponding values
        answer_choices = ["A", "B", "C"]
        for idx, choice in enumerate(answer_choices):
            button = ttk.Radiobutton(self.root, text=choice, variable=self.answer_var, value=choice)
            self.answer_buttons.append(button)
            button.pack(pady=5, anchor=tk.CENTER)  # Center the Radiobuttons horizontally

        self.next_button = ttk.Button(self.root, text="Next", command=self.next_question)
        self.next_button.pack(pady=10)

        self.display_question()

    def display_question(self):
        if self.current_question_index < len(self.questions):
            question_id, question_text, correct_answer = self.questions[self.current_question_index]
            self.question_label.config(text=f"Question {question_id}: {question_text}")

            # Set answer values for each Radiobutton
            for idx, choice in enumerate(["A", "B", "C"]):
                self.answer_buttons[idx]['value'] = choice
                self.answer_buttons[idx]['command'] = lambda c=choice: self.answer_var.set(c)  # Set command to set answer_var

            # Clear previous selection
            self.answer_var.set("")
        else:
            self.show_quiz_result()

    def next_question(self):
        question_id, question_text, correct_answer = self.questions[self.current_question_index]
        user_answer = self.answer_var.get().strip().upper()

        if user_answer == correct_answer:
            self.score += 1  # Increment score if answer is correct

        self.current_question_index += 1

        if self.current_question_index < len(self.questions):
            self.display_question()
        else:
            # Show submit button and disable next button on last question
            self.next_button.config(state=tk.DISABLED)  # Disable next button
            self.submit_button = ttk.Button(self.root, text="Submit", command=self.show_quiz_result)
            self.submit_button.pack(pady=10)

    def show_quiz_result(self):
        messagebox.showinfo("Quiz Completed", f"End of Quiz. You scored {self.score}/{len(self.questions)}")
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app_one = WindowOne(root)
    root.mainloop()