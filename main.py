# Импортирование класса, позволяющего создавать виджеты (формы, кнопочки)
from PyQt5 import QtWidgets

# QApplication - позволяет создать приложение в принципе
# QMainWindow - позволяет создать окно: само приложение может иметь множество окон 
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Это - название программы")
        # Отступ от левого-верхнего угла 
        self.setGeometry(300, 250, 350, 200)

        # Скрытый атрибут - текст
        self.new_text = QtWidgets.QLabel(self)


        # Вилжеты/Объекты нужно размещать до того, как будет показано окно и после того, как настроим основное окно
        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText("Это базовая надпись")
        # Отступ от левого-вверхнего угла самого окня
        self.main_text.move(100, 100)
        self.main_text.setFixedWidth(200)

        # Кнопка
        self.btn = QtWidgets.QPushButton(self)
        self.btn.move(70, 150)
        self.btn.setText("Нажми на меня")
        self.btn.setFixedWidth(200)
        # Присоединение к событию нажатие функцию add_label
        self.btn.clicked.connect(self.add_label)

    def add_label(self):
        self.new_text.setText("Вторая надпись")
        self.new_text.move(100, 50)
        self.new_text.setFixedWidth(200)


# Функция, которая будет вызываться при создании самого проекта
def application(): 
    app = QApplication(sys.argv)
    window = Window()

    # Окно до этого момента было скрыто
    window.show()
    # Обеспечение того, что программа будет завершаться корректно
    sys.exit(app.exec_())

# Если мы будем вызывать данный файл как основной:
if __name__ == "__main__":
    application()
