import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        
        self.window = tk.Tk()
        self.window.title("QuizApp")
        self.window.config(bg=THEME_COLOR, padx=20)

        self.quiz_score = tk.Label(text="Score: 0", bg=THEME_COLOR, fg='white', font=('Arial', 10))
        self.quiz_score.grid(row=0, column=1, pady=20, padx=20)
        
        self.canvas = tk.Canvas(width=300, height=250, bg='white')
        self.quiz_question = self.canvas.create_text(
            150,
            125,
            width=280, 
            text="Question goes here", 
            fill = THEME_COLOR,
            font=('Arial', 16, 'italic')
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        true_image = tk.PhotoImage(file="images/true.png")
        self.button_true = tk.Button(image=true_image, command=self.answer_true)
        self.button_true.grid(row=2, column=0, pady=20)

        false_image = tk.PhotoImage(file="images/false.png")
        self.button_false = tk.Button(image=false_image, command=self.answer_false)
        self.button_false.grid(row=2, column=1, pady=20)

        self.get_next_question()

        self.window.mainloop()
    

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions:
            self.quiz_score.config(text = f"Score: {self.quiz.score}/{self.quiz.question_number}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quiz_question, text=q_text)
        else:
            self.canvas.itemconfig(self.quiz_question, text="You finished.")
            self.button_true.config(state='disabled')
            self.button_false.config(state='disabled')


    def answer_true(self):
        self.give_feedback(self.quiz.check_answer('True'))
    
    def answer_false(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)
