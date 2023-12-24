import sys

from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

def greet(name):
    if msgLabel.text():
        msgLabel.setText("")
    else:
        msgLabel.setText(f"Hello, {name}!")

app = QApplication([])
window = QWidget()
window.setWindowTitle("Signals and slots")
window.setGeometry(800, 500, 280, 80)
layout = QVBoxLayout()

button = QPushButton("Greet")
# noinspection PyUnresolvedReferences
button.clicked.connect(lambda: msgLabel.settext("") if msgLabel.text() else msgLabel.setText("Hello, Sir"))

layout.addWidget(button)
msgLabel = QLabel("")
layout.addWidget(msgLabel)
window.setLayout(layout)
window.show()
sys.exit(app.exec())