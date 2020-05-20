import sys
import os
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QFormLayout, QLineEdit, QPushButton, QWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QFont, QIntValidator
from PyQt5.QtCore import QTimer, QTime, Qt

class AppDemo(QWidget):
  def __init__(self):
    super().__init__()
    self.resize(500, 300)

    self.hours = 7
    self.minutes = 30
    self.seconds = 0

    fnt = QFont('Open Sans', 30, QFont.Bold)

    self.lbl = QLabel()
    self.lbl.setAlignment(Qt.AlignCenter)
    self.lbl.setFont(fnt)

    self.inputHours = QLineEdit(str(self.hours))
    self.inputMinutes = QLineEdit(str(self.minutes))
    self.inputSeconds = QLineEdit(str(self.seconds))

    self.onlyInt = QIntValidator()
    self.inputHours.setValidator(self.onlyInt)

    self.inputLink = QLineEdit()

    visitButton = QPushButton("Visit")
    visitButton.clicked.connect(self.visitButtonClicked)
    shutDownButton = QPushButton("ShutDown")
    shutDownButton.clicked.connect(self.shutDown)

    hbox = QHBoxLayout()
    hbox.addWidget(self.inputHours)
    hbox.addWidget(self.inputMinutes)
    hbox.addWidget(self.inputSeconds)

    hbox2 = QHBoxLayout()
    hbox2.addWidget(QLabel("Visit link:"))
    hbox2.addWidget(self.inputLink)

    hbox3 = QHBoxLayout()
    hbox3.addWidget(visitButton)
    hbox3.addWidget(shutDownButton)

    vbox = QVBoxLayout()
    vbox.addWidget(self.lbl)
    vbox.addLayout(hbox)
    vbox.addLayout(hbox2)
    vbox.addLayout(hbox3)

    self.setLayout(vbox)

    timer = QTimer(self)
    timer.timeout.connect(self.showTime)
    timer.start(1000) # update every second

    self.showTime()

  def shutDown(self):
    print("shut down")
    os.system('systemctl poweroff -i')

  def visitButtonClicked(self):
    site_url = self.inputLink.text() if len(self.inputLink.text()) else 'https://www.youtube.com/watch?v=BMONbjfPCxk?autoplay=true'
    os.system('google-chrome ' + site_url)

  def showTime(self):
    currentTime = QTime.currentTime()

    displayTxt = currentTime.toString('hh:mm:ss')

    alarmTime = QTime(
        int(self.inputHours.text()),
        int(self.inputMinutes.text()),
        int(self.inputSeconds.text()),
    )
    if 0 < currentTime.secsTo(alarmTime) < 2:
      self.visitButtonClicked()

    self.lbl.setText(displayTxt)
 
app = QApplication(sys.argv)
 
demo = AppDemo()
demo.show()
 
app.exit(app.exec_())