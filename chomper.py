class Form():
    def __init__(self, question="",answer="", wrong_answer1='',wrong_answer2='', wrong_answer3=''):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
class FormView():
    def __init__(self, frm_model, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.frm_model = frm_model
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        def change(self, frm_model):
            self.frm_model = frm_model
        def show(self):
            self.question.setText(self.frm_model.question)
            self.answer.setText(self.frm_model.answer)
            self.wrong_answer1.setText(self.frm_model.wrong_answer1)
            self.wrong_answer2.setText(self.frm_model.wrong_answer2)
            self.wrong_answer3.setText(self.frm_model.wrong_answer3)