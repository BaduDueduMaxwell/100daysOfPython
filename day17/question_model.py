class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer

    def __str__(self):
        return f"{self.text}"

new_q = Question('add?', 'False')