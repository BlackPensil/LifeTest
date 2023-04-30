# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
# from random import randint
#
# # Создание окна
# app = QApplication([])
# main_win = QWidget()
# main_win.move(900, 70)
# main_win.resize(400, 200)
#
# # Название окна
# main_win.setWindowTitle('Определитель победителя')
#
# #main_win.hide()
#
# # Виджеты
# winner = QLabel('?')
# button = QPushButton('Сгенерировать')
# text = QLabel('Нажми, чтобы узнать победителя')
# v_line = QVBoxLayout()
#
# # Добавление виджетов в линии эти
# v_line.addWidget(button, alignment = Qt.AlignCenter)
# v_line.addWidget(text, alignment = Qt.AlignCenter)
# v_line.addWidget(winner, alignment = Qt.AlignCenter)
#
# # Отрисовка линий с виджетами
# main_win.setLayout(v_line)
#
# def show_winner():
#     number = randint(0, 99)
#     winner.setText(str(number))
#     text.setText('Победитель:')
#
# button.clicked.connect(show_winner)
# main_win.show()
# app.exec_()
#
#
#
#
#
#
#  ДОДЕЛАТЬ У7M1
#
#
#
#
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton
#
# app = QApplication([])
# main = QWidget()
# main.move(900, 70)
# main.resize(400, 200)
#
# main.setWindowTitle('Тест')
#
# question = QLabel('В каком году?')
# btn_answer1 = QRadioButton('2013')
# btn_answer2 = QRadioButton('2010')
# btn_answer3 = QRadioButton('2016')
# btn_answer4 = QRadioButton('2019')
# victory_win = QMessageBox()
# victory_win.setText('Верно!')
#
# layoutH1 = QHBoxLayout()
# layoutH2 = QHBoxLayout()
# layoutH3 = QHBoxLayout()
#
# layoutH1.addWidget(question, alignment = Qt.AlignCenter)
# layoutH2.addWidget(btn_answer1, alignment = Qt.AlignCenter)
# layoutH2.addWidget(btn_answer2, alignment = Qt.AlignCenter)
# layoutH3.addWidget(btn_answer3, alignment = Qt.AlignCenter)
# layoutH3.addWidget(btn_answer4, alignment = Qt.AlignCenter)
#
# layout_main = QVBoxLayout()
#
# layout_main.addLayout(layoutH1)
# layout_main.addLayout(layoutH2)
# layout_main.addLayout(layoutH3)
# main.setLayout(layout_main)
#
# def show_win():
#     pass
# def show_lose():
#     pass
#
# btn_answer3.clicked.connect(show_win)
# btn_answer1.clicked.connect(show_lose)
# btn_answer2.clicked.connect(show_lose)
# btn_answer4.clicked.connect(show_lose)
#
# main.show()
# app.exec_()
# victory_win.exec_()
#
#
#
# НОВЫЙ ПРОЕКТ
#
#
