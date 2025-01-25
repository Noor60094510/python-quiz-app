import tkinter as tk
from tkinter import messagebox
import random
import json

# Define a list of quiz questions
questions = [
    {
        "topic": "Loops",
        "question": "What will be the output of this Python code?",
        "code": "for i in range(3):\n    print(i)",
        "options": ["0 1 2", "1 2 3", "0 1 2 3", "1 2"],
        "answer": 1  # Correct option index (1-based)
    },
    {
        "topic": "Lists",
        "question": "Which method is used to add an element to the end of a list?",
        "code": "",
        "options": ["append()", "insert()", "extend()", "add()"],
        "answer": 1
    },
    {
        "topic": "Strings",
        "question": "What will be the output of this Python code?",
        "code": "'Python'.upper()",
        "options": ["PYTHON", "python", "None", "Error"],
        "answer": 1
    },
    {
        "topic": "Dictionaries",
        "question": "Which method is used to get the value associated with a key in a dictionary?",
        "code": "",
        "options": ["get()", "keys()", "values()", "items()"],
        "answer": 1
    },
    {
        "topic": "Functions",
        "question": "What does the 'return' keyword do in Python?",
        "code": "",
        "options": [
            "Stops a function and returns a value",
            "Defines a new function",
            "Returns all variables in the function",
            "Exits the program"
        ],
        "answer": 1
    },
    {
        "topic": "Conditional Statements",
        "question": "What will be the output of this code?",
        "code": "x = 5\nif x > 3:\n    print('Greater')",
        "options": ["Greater", "Error", "None", "3"],
        "answer": 1
    },
    {
        "topic": "Modules",
        "question": "Which Python keyword is used to import a module?",
        "code": "",
        "options": ["import", "module", "include", "load"],
        "answer": 1
    },
    {
        "topic": "Loops",
        "question": "What is the purpose of the 'break' statement in a loop?",
        "code": "",
        "options": [
            "To exit the loop prematurely",
            "To restart the loop",
            "To skip an iteration",
            "To pause the loop"
        ],
        "answer": 1
    },
    {
        "topic": "Lists",
        "question": "What will be the output of this Python code?",
        "code": "my_list = [1, 2, 3]\nprint(my_list[1])",
        "options": ["1", "2", "3", "IndexError"],
        "answer": 2
    },
    {
        "topic": "Sets",
        "question": "Which of the following is true about sets in Python?",
        "code": "",
        "options": [
            "They are unordered collections of unique elements",
            "They allow duplicate elements",
            "They are immutable",
            "They are always sorted"
        ],
        "answer": 1
    },
    {
        "topic": "Classes",
        "question": "What is '__init__' used for in a Python class?",
        "code": "",
        "options": [
            "To initialize an object",
            "To delete an object",
            "To define a method",
            "To inherit another class"
        ],
        "answer": 1
    },
    {
        "topic": "File Handling",
        "question": "What mode should you use to write to a file in Python?",
        "code": "",
        "options": ["'w'", "'r'", "'x'", "'a'"],
        "answer": 1
    },
    {
        "topic": "Error Handling",
        "question": "What is the purpose of a 'try-except' block in Python?",
        "code": "",
        "options": [
            "To handle exceptions",
            "To create a loop",
            "To define a function",
            "To define a variable"
        ],
        "answer": 1
    }
]


class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Quiz Generator")
        self.root.geometry("500x600")

        self.score = 0  # Initialize score
        self.completed_questions = []  # Track completed questions

        # Load progress if available
        self.load_progress()

        # Input field
        self.topic_label = tk.Label(root, text="Enter Topic:")
        self.topic_label.pack(pady=5)

        self.topic_entry = tk.Entry(root, width=40)
        self.topic_entry.pack(pady=5)

        self.generate_button = tk.Button(root, text="Generate Python Question", command=self.generate_question)
        self.generate_button.pack(pady=10)

        # Display section
        self.topic_display = tk.Label(root, text="", font=("Arial", 12, "bold"))
        self.topic_display.pack(pady=5)

        self.question_display = tk.Label(root, text="", wraplength=400, justify="left")
        self.question_display.pack(pady=5)

        self.code_display = tk.Label(root, text="", fg="blue", justify="left")
        self.code_display.pack(pady=5)

        # Answer options
        self.options_var = tk.IntVar()
        self.options_buttons = []

        # Submit button
        self.submit_button = tk.Button(root, text="Submit", state="disabled")
        self.submit_button.pack(pady=10)

        # Feedback
        self.feedback_label = tk.Label(root, text="", font=("Arial", 10))
        self.feedback_label.pack(pady=5)

        # Score display
        self.score_label = tk.Label(root, text=f"Score: {self.score}", font=("Arial", 12))
        self.score_label.pack(pady=5)

    def generate_question(self):
        topic = self.topic_entry.get().strip()
        if not topic:
            messagebox.showerror("Error", "Please enter a topic!")
            return

        # Filter questions by topic
        available_questions = [q for q in questions if q["topic"].lower() == topic.lower() and q["question"] not in self.completed_questions]
        if not available_questions:
            messagebox.showerror("Error", f"No more questions available for topic '{topic}'")
            return

        # Randomly select a question
        self.current_question = random.choice(available_questions)
        self.display_question(self.current_question)

    def display_question(self, question):
        self.topic_display.config(text=f"Topic: {question['topic']}")
        self.question_display.config(text=question["question"])
        self.code_display.config(text=question.get("code", ""))

        # Clear previous options
        for button in self.options_buttons:
            button.destroy()
        self.options_buttons = []

        # Display new options
        self.options_var.set(0)
        for idx, option in enumerate(question["options"], start=1):
            rb = tk.Radiobutton(
                self.root, text=option, variable=self.options_var, value=idx, anchor="w", justify="left"
            )
            rb.pack(anchor="w")
            self.options_buttons.append(rb)

        # Enable the submit button
        self.submit_button.config(state="normal", command=self.check_answer)

    def check_answer(self):
        selected_option = self.options_var.get()
        if selected_option == 0:
            messagebox.showwarning("Warning", "Please select an answer!")
            return

        correct_answer = self.current_question["answer"]
        if selected_option == correct_answer:
            self.score += 1  # Update score
            self.feedback_label.config(text="Correct! Well done!", fg="green")
        else:
            self.feedback_label.config(text="Incorrect. Try again.", fg="red")

        # Update score display
        self.score_label.config(text=f"Score: {self.score}")

        # Mark the question as completed
        self.completed_questions.append(self.current_question["question"])

        # Save progress
        self.save_progress()

        # Disable submit button until a new question is generated
        self.submit_button.config(state="disabled")

    def save_progress(self):
        data = {
            "score": self.score,
            "completed_questions": self.completed_questions
        }
        with open("progress.json", "w") as file:
            json.dump(data, file)

    def load_progress(self):
        try:
            with open("progress.json", "r") as file:
                data = json.load(file)
                self.score = data.get("score", 0)
                self.completed_questions = data.get("completed_questions", [])
        except FileNotFoundError:
            pass  # No progress file found, start fresh


# Main application setup
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
