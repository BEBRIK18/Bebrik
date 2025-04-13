from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from random import shuffle

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    text1.setText(q.question)
    result.setText(q.right_answer)
    show_question()

def check_answer():
    if answers[0].isChecked():
        show_result('Правильно')
    else :
        show_result('Неправильно')


def test_button():
    if pbtn.text() == 'Ответить':
        check_answer()
    if pbtn.text() == 'Следующий вопрос':
        next_question()

def show_result(res):
    qgb.hide()
    qgb2.show()
    problem.setText(res)
    pbtn.setText('Следующий вопрос')
    pbtn.clicked.connect(show_question)
    
def show_question():
    qgb2.hide()
    qgb.show()
    pbtn.setText('Ответить')
    rbtn_1.setText('Вариант 1')
    rbtn_2.setText('Вариант 2')
    rbtn_3.setText('Вариант 3')
    rbtn_4.setText('Вариант 4')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
    

def next_question():
    win.cur_question += 1
    if win.cur_question == len(questions_list):
        win.cur_question = 0
        now_ask = questions_list[win.cur_question]
        ask(now_ask)



questions_list = []
q1 = Question('Какой национальный не существует?', 'Энцы', 'Чулымцы', 'Смурфы', 'Алеунты')
q2 = Question('Государственный язык Португалии',
 'Португальский', 'Английский', 'Испанский', 'Французский')
questions_list.append(q1)

app = QApplication([])
win = QWidget()
win.resize(600, 400)
 
win.cur_question = -1

bl_main = QVBoxLayout()
bl = QHBoxLayout()
bl_gb = QVBoxLayout()
bl_gb2 = QHBoxLayout()
gb1 = QHBoxLayout()
gb2 = QHBoxLayout()
 
#создание виджетов
text1 = QLabel('Какой национальный не существует?')
qgb = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Чулымцы')
rbtn_3 = QRadioButton('Смурфы')
rbtn_4 = QRadioButton('Алеунты')
pbtn = QPushButton('Ответить')

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

#создание виджетов для второго групбокса
question = QLabel('вопрос?')
result = QLabel('')
problem = QLabel('Неверно!?')
qgb2 = QGroupBox('Результат')

#добавление на направляющие
bl_main.addWidget(text1, alignment=Qt.AlignCenter)
bl_main.addWidget(qgb)
bl_main.addLayout(bl)
bl_gb.addLayout(gb1)
bl_gb.addLayout(gb2)
gb1.addWidget(rbtn_1)
gb1.addWidget(rbtn_2)
gb2.addWidget(rbtn_3)
gb2.addWidget(rbtn_4)
bl_gb2.addWidget(result)
bl_gb2.addWidget(problem)

bl_main.addWidget(pbtn, alignment=Qt.AlignCenter)

#добавление группы кнопок
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
 
qgb.setLayout(bl_gb)
bl.addWidget(qgb2)
qgb2.setLayout(bl_gb2)
qgb2.hide()

win.setLayout(bl_main)

pbtn.clicked.connect(test_button)
next_question()

win.show()
app.exec_()

print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')