import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QVBoxLayout)


class Clicker(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Кликер")

        self.count = 0
        self.label = QLabel(f"Счёт: {self.count}")

        self.button = QPushButton("Клик!")
        self.button.clicked.connect(self.increment_count)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def increment_count(self):
        self.count += 1
        self.label.setText(f"Счёт: {self.count}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Clicker()
    window.show()
    sys.exit(app.exec())
