# Импортирование класса, позволяющего создавать виджеты (формы, кнопочки)
from PyQt5 import QtWidgets

# QApplication - позволяет создать приложение в принципе
# QMainWindow - позволяет создать окно: само приложение может иметь множество окон 
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys


# Функция, которая будет вызываться при создании самого проекта
def application(): 
    app = QApplication(sys.argv)
    window = QMainWindow()

    window.setWindowTitle("Это - название программы")
    # Отступ от левого-верхнего угла 
    window.setGeometry(300, 250, 350, 200)

    # Окно до этого момента было скрыто
    window.show()
    # Обеспечение того, что программа будет завершаться корректно
    sys.exit(app.exec_())

# Если мы будем вызывать данный файл как основной:
if __name__ == "__main__":
    application()