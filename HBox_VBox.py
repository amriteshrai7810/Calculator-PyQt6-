# HBox
import sys

from PyQt6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QPushButton,
    QWidget,
)

app = QApplication([])
window = QWidget()
window.setWindowTitle("QHBoxLayout")

layout = QHBoxLayout()
layout.addWidget(QPushButton("Left"))
layout.addWidget(QPushButton("Center"))
layout.addWidget(QPushButton("Right"))
window.setLayout(layout)

window.show()
sys.exit(app.exec())


# # VBox

# import sys
#
# from PyQt6.QtWidgets import (
#     QApplication,
#     QPushButton,
#     QVBoxLayout,
#     QWidget,
# )
#
# app = QApplication([])
# window = QWidget()
# window.setWindowTitle("QVBoxLayout")
#
# layout = QVBoxLayout()
# layout.addWidget(QPushButton("Top"))
# layout.addWidget(QPushButton("Center"))
# layout.addWidget(QPushButton("Bottom"))
# window.setLayout(layout)
#
# window.show()
# sys.exit(app.exec())

# # GridBox
# import sys
#
# from PyQt6.QtWidgets import (
#     QApplication,
#     QGridLayout,
#     QPushButton,
#     QWidget,
# )
#
# app = QApplication([])
# window = QWidget()
# window.setWindowTitle("QGridLayout")
#
# layout = QGridLayout()
# layout.addWidget(QPushButton("Button (0, 0)"), 0, 0)
# layout.addWidget(QPushButton("Button (0, 1)"), 0, 1)
# layout.addWidget(QPushButton("Button (0, 2)"), 0, 2)
# layout.addWidget(QPushButton("Button (1, 0)"), 1, 0)
# layout.addWidget(QPushButton("Button (1, 1)"), 1, 1)
# layout.addWidget(QPushButton("Button (1, 2)"), 1, 2)
# layout.addWidget(QPushButton("Button (2, 0)"), 2, 0)
# layout.addWidget(
#     QPushButton("Button (2, 1) + 2 Columns Span"), 2, 1, 1, 2
# )
# window.setLayout(layout)
#
# window.show()
# sys.exit(app.exec())


