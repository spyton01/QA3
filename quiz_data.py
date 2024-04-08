import tkinter as tk
from tkinter import ttk, messagebox
from quiz_data import initialize_quiz

class WindowOne:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Category Selection")

        self.selected_category = tk.StringVar()

        # Initialize quiz data
        self.quiz = initialize_quiz()

        # Populate category options from quiz data
        category_names = [topic.name for topic in self.quiz.topics]
        self.category_combo = ttk.Combobox(self.root, width=30, textvariable=self.selected_category)
        self.category_combo['values'] = category_names
        self.category_combo.pack(pady=20)

        self.start_button = ttk.Button(self.root, text="Start Quiz Now", command=self.start_quiz)
        self.start_button.pack(pady=10)

    def start_quiz(self):
        selected_category = self.selected_category.get()
        if selected_category:
            self.root.destroy()

            quiz_window = tk.Tk()
            quiz_window.title(f"Quiz: {selected_category}")
            quiz_window.geometry("600x400")

            # Find selected topic in the quiz data
            selected_topic = next((topic for topic in self.quiz.topics if topic.name == selected_category), None)
            if selected_topic:
                WindowTwo(quiz_window, selected_topic)

class WindowTwo:
    def __init__(self, root, topic):
        self.root = root
        self.topic = topic
        self.questions = topic.questions
        self.current_question_index = 0
        self.score = 0

        self.setup_ui()

    def setup_ui(self):
        self.question_label = ttk.Label(self.root, text="", wraplength=500)
        self.question_label.pack(pady=20)

        self.answer_var = tk.StringVar()
        self.answer_var.set("")

        self.answer_buttons = []
        for idx in range(len(self.questions[self.current_question_index].choices)):
            button = ttk.Radiobutton(self.root, text="", variable=self.answer_var, value="")
            self.answer_buttons.append(button)
            button.pack(pady=5, anchor=tk.CENTER)

        self.next_button = ttk.Button(self.root, text="Next", command=self.next_question)
        self.next_button.pack(pady=10)

        self.display_question()

    def display_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.question_label.config(text=f"Question {self.current_question_index + 1}: {question.text}")

            # Update answer buttons with choices
            for idx, choice_button in enumerate(self.answer_buttons):
                if idx < len(question.choices):
                    choice_button.config(text=question.choices[idx], value=question.choices[idx])
                else:
                    choice_button.pack_forget()  # Hide extra buttons if fewer choices

            self.answer_var.set("")  # Clear selection
        else:
            self.show_quiz_result()

    def next_question(self):
        user_answer = self.answer_var.get().strip().upper()
        if not user_answer:
            messagebox.showwarning("No Answer Selected", "Please select an answer before proceeding.")
        else:
            question = self.questions[self.current_question_index]
            if user_answer == question.answer.upper():
                self.score += 1

            self.current_question_index += 1
            self.display_question()

    def show_quiz_result(self):
        messagebox.showinfo("Quiz Completed", f"End of Quiz. You scored {self.score}/{len(self.questions)}")
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app_one = WindowOne(root)
    root.mainloop()