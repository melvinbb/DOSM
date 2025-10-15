import sys
import random
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QPushButton)
from PyQt6.QtCore import Qt


class RandomNumberGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Генератор случайных чисел")
        self.label = QLabel("Нажмите кнопку, чтобы сгенерировать число")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.button = QPushButton("Сгенерировать")
        self.button.clicked.connect(self.generate_random_number)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def generate_random_number(self):
        random_number = random.randint(1, 100)
        self.label.setText(f"Случайное число: {random_number}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RandomNumberGenerator()
    window.show()
    sys.exit(app.exec())
