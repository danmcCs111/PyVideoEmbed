import sys
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtWebEngineWidgets import QWebEngineView

videoWidth = 800
videoHeight = 450

isFull = False

argIt = 1

if("-f" == sys.argv[argIt] or "--fullscreen" == sys.argv[argIt]):
        isFull = True
        argIt += 1
        videoLink = sys.argv[argIt]
        argIt += 1
else:
        videoLink = sys.argv[argIt]
        argIt += 1

if(sys.argv.__len__() > argIt+1):
    videoWidth = int(sys.argv[argIt])
    argIt += 1
    videoHeight = int(sys.argv[argIt])
    argIt += 1

# Basic PyQt6 window setup
app = QApplication(sys.argv)
window = QMainWindow()

if(isFull):
    window.showFullScreen()
else:
    window.resize(videoWidth, videoHeight)
window.setWindowTitle("PyQt6 Video Embed")


# Initialize and configure QWebEngineView
browser = QWebEngineView()
browser.setUrl(QUrl(videoLink))

window.setCentralWidget(browser)
window.show()
sys.exit(app.exec())
