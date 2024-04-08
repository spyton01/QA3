import tkinter as tk
from tkinter import ttk, messagebox
from dataclasses import dataclass
from typing import List

@dataclass
class QuizQuestion:
    question_id: int
    question_text: str
    answer_choices: List[str]
    correct_answer: str

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
            self.root.withdraw()  # Hide category selection window

            quiz_window = tk.Toplevel(self.root)
            quiz_window.title(f"Quiz: {selected_category}")
            quiz_window.geometry("600x400")

            # Retrieve questions based on selected category
            if selected_category == "OCM Logistic":
                questions = self.get_ocm_logistic_questions()
            elif selected_category == "Modern History":
                questions = self.get_modern_history_questions()
            elif selected_category == "Finance":
                questions = self.get_finance_questions()
            elif selected_category == "Business Analytics":
                questions = self.get_business_analytics_questions()
            elif selected_category == "Prog Logic":
                questions = self.get_prog_logic_questions()

            WindowTwo(quiz_window, selected_category, questions, self.root)

    def get_ocm_logistic_questions(self):
        return [
QuizQuestion(1, "What is the primary objective of Operation Logistic OCM?",
             ["A: Enhancing supply chain efficiency", "B: Implementing new technology solutions",
              "C: Streamlining operational processes"], "A"),

QuizQuestion(2, "Who is the key stakeholder responsible for driving change in Operation Logistic OCM?",
             ["A: Project Manager", "B: Operations Director", "C: Change Management Team"], "C"),

QuizQuestion(3, "Which factor is crucial for successful change management in Operation Logistic OCM?",
             ["A: Resistance to change", "B: Effective communication", "C: Status quo preservation"], "B"),

QuizQuestion(4, "What does OCM stand for in Operation Logistic OCM?",
             ["A: Organizational Change Model", "B: Operational Control Mechanism", "C: Organizational Change Management"], "C"),

QuizQuestion(5, "Which phase of change management involves assessing the impact of change?",
             ["A: Planning", "B: Execution", "C: Evaluation"], "A"),

QuizQuestion(6, "What is the purpose of a change management plan in Operation Logistic OCM?",
             ["A: Documenting current processes", "B: Managing resistance to change", "C: Generating project reports"], "B"),

QuizQuestion(7, "Which approach is effective for overcoming resistance to change?",
             ["A: Ignoring concerns", "B: Providing training and support", "C: Enforcing strict policies"], "B"),

QuizQuestion(8, "What role does leadership play in successful change management?",
             ["A: Minimizing stakeholder involvement", "B: Setting a clear vision", "C: Avoiding communication"], "B"),

QuizQuestion(9, "How can employees be engaged during Operation Logistic OCM?",
             ["A: Limiting transparency", "B: Encouraging participation", "C: Avoiding feedback"], "B"),

QuizQuestion(10, "Which step is essential for sustaining change after Operation Logistic OCM?",
              ["A: Reverting to old processes", "B: Continuous monitoring and improvement", "C: Halting communication"], "B")]

    def get_modern_history_questions(self):
        return [
QuizQuestion(1, "Which event marked the beginning of World War I?",
             ["A: Assassination of Archduke Franz Ferdinand", "B: Treaty of Versailles",
              "C: Battle of Stalingrad"], "A"),

QuizQuestion(2, "Who was the leader of the Soviet Union during the Cuban Missile Crisis?",
             ["A: Nikita Khrushchev", "B: Joseph Stalin", "C: Mikhail Gorbachev"], "A"),

QuizQuestion(3, "Which country was the first to launch a satellite into space?",
             ["A: United States", "B: Russia (Soviet Union)", "C: China"], "B"),

QuizQuestion(4, "Where did the Normandy landings (D-Day) take place during World War II?",
             ["A: Italy", "B: France", "C: Germany"], "B"),

QuizQuestion(5, "Which treaty officially ended World War I?",
             ["A: Treaty of Versailles", "B: Treaty of Trianon", "C: Treaty of Brest-Litovsk"], "A"),

QuizQuestion(6, "Who was the British Prime Minister at the beginning of World War II?",
             ["A: Winston Churchill", "B: Neville Chamberlain", "C: Clement Attlee"], "B"),

QuizQuestion(7, "Which battle is considered the turning point of the Pacific Theater during World War II?",
             ["A: Battle of Midway", "B: Battle of Iwo Jima", "C: Battle of Okinawa"], "A"),

QuizQuestion(8, "Which country was the first to use atomic bombs in warfare?",
             ["A: United States", "B: Germany", "C: Japan"], "A"),

QuizQuestion(9, "What was the name of the Allied invasion of Nazi-occupied Europe in 1944?",
             ["A: Operation Market Garden", "B: Operation Overlord", "C: Operation Barbarossa"], "B"),

QuizQuestion(10, "Who was the President of the United States at the end of World War II?",
              ["A: Franklin D. Roosevelt", "B: Harry S. Truman", "C: Dwight D. Eisenhower"], "B")]

    def get_finance_questions(self):
        return [
QuizQuestion(1, "What is the primary function of a central bank in a country's economy?",
             ["A: Regulating interest rates", "B: Issuing currency", "C: Conducting monetary policy"], "C"),

QuizQuestion(2, "Who is known as the 'Oracle of Omaha' in the world of finance?",
             ["A: Warren Buffett", "B: Bill Gates", "C: Elon Musk"], "A"),

QuizQuestion(3, "Which economic indicator measures the average price level of goods and services?",
             ["A: GDP (Gross Domestic Product)", "B: Inflation rate", "C: Unemployment rate"], "B"),

QuizQuestion(4, "What does GDP stand for in economics?",
             ["A: Gross Domestic Policy", "B: General Domestic Product", "C: Gross Domestic Product"], "C"),

QuizQuestion(5, "Which financial instrument represents ownership in a corporation?",
             ["A: Bond", "B: Stock", "C: Certificate of Deposit"], "B"),

QuizQuestion(6, "What is the term for a situation where prices increase, reducing the purchasing power of money?",
             ["A: Deflation", "B: Stagflation", "C: Inflation"], "C"),

QuizQuestion(7, "Which type of market structure is characterized by a large number of buyers and sellers?",
             ["A: Monopoly", "B: Oligopoly", "C: Perfect competition"], "C"),

QuizQuestion(8, "What is the key role of fiscal policy in economics?",
             ["A: Controlling the money supply", "B: Managing government spending and taxation", "C: Regulating financial institutions"], "B"),

QuizQuestion(9, "Which organization is responsible for regulating the stock market in the United States?",
             ["A: Federal Reserve", "B: Securities and Exchange Commission (SEC)", "C: International Monetary Fund (IMF)"], "B"),

QuizQuestion(10, "What term describes the total value of goods and services produced within a country in a year?",
              ["A: National income", "B: Gross National Product (GNP)", "C: Gross Domestic Product (GDP)"], "C")]

    def get_business_analytics_questions(self):
        return [
QuizQuestion(1, "What statistical method is used to identify patterns and relationships in large datasets?",
             ["A: Regression analysis", "B: Cluster analysis", "C: Time series analysis"], "B"),

QuizQuestion(2, "Which software tool is commonly used for data visualization and business intelligence?",
             ["A: Tableau", "B: Python", "C: Excel"], "A"),

QuizQuestion(3, "Which type of analysis is used to predict future values based on past observations?",
             ["A: Descriptive analysis", "B: Predictive analysis", "C: Prescriptive analysis"], "B"),

QuizQuestion(4, "What does SQL stand for in the context of databases?",
             ["A: Structured Query Language", "B: Statistical Query Logic", "C: Systematic Query Link"], "A"),

QuizQuestion(5, "Which programming language is widely used for data analysis and machine learning?",
             ["A: Java", "B: R", "C: C++"], "B"),

QuizQuestion(6, "What is the purpose of A/B testing in data analysis?",
             ["A: Exploring relationships between variables", "B: Testing different versions to determine the best performer", "C: Generating summary statistics"], "B"),

QuizQuestion(7, "Which term refers to the process of cleaning and preparing data for analysis?",
             ["A: Data visualization", "B: Data exploration", "C: Data wrangling"], "C"),

QuizQuestion(8, "What is the main objective of exploratory data analysis (EDA)?",
             ["A: Building predictive models", "B: Summarizing data distributions", "C: Conducting hypothesis testing"], "B"),

QuizQuestion(9, "Which technique is used to reduce the dimensionality of data while preserving important information?",
             ["A: Clustering", "B: Principal Component Analysis (PCA)", "C: Time series analysis"], "B"),

QuizQuestion(10, "Which method is used to measure the strength and direction of a linear relationship between two variables?",
              ["A: Classification", "B: Correlation analysis", "C: Decision tree analysis"], "B")]

    def get_prog_logic_questions(self):
        return [
QuizQuestion(1, "What is the fundamental concept in programming that involves breaking down a problem into smaller, more manageable parts?",
             ["A: Decomposition", "B: Abstraction", "C: Iteration"], "A"),

QuizQuestion(2, "Which data structure uses a last-in, first-out (LIFO) approach?",
             ["A: Queue", "B: Stack", "C: Linked List"], "B"),

QuizQuestion(3, "What is the term for a function calling itself within its own definition?",
             ["A: Recursion", "B: Iteration", "C: Abstraction"], "A"),

QuizQuestion(4, "Which sorting algorithm has an average time complexity of O(n log n)?",
             ["A: Bubble sort", "B: Merge sort", "C: Insertion sort"], "B"),

QuizQuestion(5, "In object-oriented programming, what is a blueprint for creating objects?",
             ["A: Interface", "B: Class", "C: Function"], "B"),

QuizQuestion(6, "Which programming language is known for its use in web development and building dynamic websites?",
             ["A: Java", "B: Python", "C: JavaScript"], "C"),

QuizQuestion(7, "What does CRUD stand for in the context of database operations?",
             ["A: Create, Read, Update, Delete", "B: Copy, Replace, Undo, Deploy", "C: Compile, Run, Debug, Execute"], "A"),

QuizQuestion(8, "What is the term for data that can only take on a limited number of possible values?",
             ["A: Continuous data", "B: Categorical data", "C: Ordinal data"], "B"),

QuizQuestion(9, "Which data structure organizes elements in a hierarchical order?",
             ["A: Array", "B: Binary tree", "C: Hash table"], "B"),

QuizQuestion(10, "What is the primary purpose of exception handling in programming?",
              ["A: Optimizing code performance", "B: Handling unexpected errors", "C: Improving code readability"], "B")]

class WindowTwo:
    def __init__(self, root, category, questions, main_window):
        self.root = root
        self.category = category
        self.questions = questions
        self.main_window = main_window  # Reference to the main category selection window

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
            question = self.questions[self.current_question_index]
            self.question_label.config(text=f"Question {question.question_id}: {question.question_text}")

            # Set answer values for each Radiobutton
            for idx, button in enumerate(self.answer_buttons):
                if idx < len(question.answer_choices):
                    button['text'] = question.answer_choices[idx]

            # Clear previous selection
            self.answer_var.set("")
        else:
            self.show_quiz_result()

    def next_question(self):
        if self.answer_var.get().strip() == "":
            # Display a message informing the user to select an answer
            messagebox.showwarning("No Answer Selected", "Please select an answer before proceeding.")
        else:
            question = self.questions[self.current_question_index]
            user_answer = self.answer_var.get().strip()

            if user_answer == question.correct_answer:
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
        # Create a "Go Back" button
        go_back_button = ttk.Button(self.root, text="Go Back to Categories", command=self.go_back)
        go_back_button.pack(pady=10)

        messagebox.showinfo("Quiz Completed", f"End of Quiz. You scored {self.score}/{len(self.questions)}")

    def go_back(self):
        self.root.destroy()  # Close the quiz window
        self.main_window.deiconify()  # Show the main category selection window (WindowOne)

if __name__ == "__main__":
    root = tk.Tk()
    app_one = WindowOne(root)
    root.mainloop()