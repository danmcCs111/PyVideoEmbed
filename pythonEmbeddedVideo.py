import sys
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtWebEngineWidgets import QWebEngineView

videoLink = sys.argv[1]

# Basic PyQt6 window setup
app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("PyQt6 Video Embed")
window.resize(800, 450)

# Initialize and configure QWebEngineView
browser = QWebEngineView()
browser.setUrl(QUrl(videoLink))

window.setCentralWidget(browser)
window.show()
sys.exit(app.exec())
