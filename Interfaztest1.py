import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QWidget

app = QApplication(sys.argv)

# 1. Carcasa exterior del reproductor
window = QWidget()
window.setWindowTitle("Py.P3 Player")
window.setFixedSize(360, 520)
window.setStyleSheet("background-color: #2c2f33;")

# 2. Marco de la pantalla LCD ámbar
screen = QLabel("Py.P3 Player\n\n[ Pantalla LCD ]", window)
screen.setGeometry(20, 20, 320, 230)
screen.setAlignment(Qt.AlignmentFlag.AlignCenter)
screen.setStyleSheet("""
    background-color: #b8e4ff;
    color: #2b1700;
    font-family: monospace;
    font-size: 15px;
    font-weight: bold;
    border: 5px solid #18191c;
    border-radius: 8px;
""")

window.show()
sys.exit(app.exec())