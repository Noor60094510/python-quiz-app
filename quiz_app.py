# quiz_app.py

# Define a list of quiz questions
import tkinter as tk
from tkinter import messagebox

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
    }
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Quiz Generator")
        self.root.geometry("500x600")

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

    def generate_question(self):
        topic = self.topic_entry.get().strip()
        if not topic:
            messagebox.showerror("Error", "Please enter a topic!")
            return

        # Filter questions by topic
        filtered_questions = [q for q in questions if q["topic"].lower() == topic.lower()]
        if not filtered_questions:
            messagebox.showerror("Error", f"No questions found for topic '{topic}'")
            return

        # Display the first question
        self.current_question = filtered_questions[0]
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
            self.feedback_label.config(text="Correct! Well done!", fg="green")
        else:
            self.feedback_label.config(text="Incorrect. Try again.", fg="red")


# Main application setup
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()

