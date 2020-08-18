from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox

from PIL.ImageQt import ImageQt
import os
from tkinter import *
from PIL import Image, ImageDraw, ImageFont, ImageTk


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1226, 693)

        self.img_cnt = 1
        self.coverimg_path = ''
        self.fontfile_path = ''

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.InputFrame = QtWidgets.QFrame(self.centralwidget)
        self.InputFrame.setGeometry(QtCore.QRect(10, 10, 241, 200))
        self.InputFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.InputFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.InputFrame.setObjectName("InputFrame")
        self.formLayout = QtWidgets.QFormLayout(self.InputFrame)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.InputFrame)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.img_button = QtWidgets.QPushButton(self.InputFrame)
        self.img_button.setObjectName("img_button")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.img_button)

        self.img_button.clicked.connect(self.askcoverimage) # connect for input file

        self.label_20 = QtWidgets.QLabel(self.InputFrame)
        self.label_20.setObjectName("label_20")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_20)
        self.fontfile_button = QtWidgets.QPushButton(self.InputFrame)
        self.fontfile_button.setObjectName("fontfile_button")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.fontfile_button)

        self.fontfile_button.clicked.connect(self.askfontfile)  # on click connect to method for font file

        self.label1 = QtWidgets.QLabel(self.InputFrame)
        self.label1.setObjectName("label1")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label1)
        self.name = QtWidgets.QLineEdit(self.InputFrame)
        self.name.setObjectName("name")
        self.name.setPlaceholderText("StudentName")

        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.name)
        self.name_2 = QtWidgets.QLabel(self.InputFrame)
        self.name_2.setObjectName("name_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.name_2)
        self.roll = QtWidgets.QLineEdit(self.InputFrame)
        self.roll.setObjectName("roll")
        self.roll.setPlaceholderText("Roll No")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.roll)
        self.name_3 = QtWidgets.QLabel(self.InputFrame)
        self.name_3.setObjectName("name_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.name_3)
        self.title = QtWidgets.QLineEdit(self.InputFrame)
        self.title.setObjectName("title")
        self.title.setPlaceholderText("e.g. Practical No - 1")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.title)
        self.name_5 = QtWidgets.QLabel(self.InputFrame)
        self.name_5.setObjectName("name_5")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.name_5)
        self.pgno = QtWidgets.QLineEdit(self.InputFrame)
        self.pgno.setObjectName("pgno")
        self.pgno.setPlaceholderText("e.g. 1")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.pgno)
        self.name_4 = QtWidgets.QLabel(self.InputFrame)
        self.name_4.setObjectName("name_4")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.name_4)
        
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 200, 241, 281))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.titlex = QtWidgets.QSpinBox(self.groupBox)
        self.titlex.setMaximum(9999)
        self.titlex.setObjectName("titlex")
        self.horizontalLayout.addWidget(self.titlex)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.titley = QtWidgets.QSpinBox(self.groupBox)
        self.titley.setMaximum(9999)
        self.titley.setObjectName("titley")
        self.horizontalLayout.addWidget(self.titley)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line_4 = QtWidgets.QFrame(self.groupBox)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout.addWidget(self.line_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.namex = QtWidgets.QSpinBox(self.groupBox)
        self.namex.setMaximum(9999)
        self.namex.setObjectName("namex")
        self.horizontalLayout_2.addWidget(self.namex)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.namey = QtWidgets.QSpinBox(self.groupBox)
        self.namey.setMaximum(9999)
        self.namey.setObjectName("namey")
        self.horizontalLayout_2.addWidget(self.namey)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.line_3 = QtWidgets.QFrame(self.groupBox)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_3.addWidget(self.label_9)
        self.rollx = QtWidgets.QSpinBox(self.groupBox)
        self.rollx.setMaximum(9999)
        self.rollx.setObjectName("rollx")
        self.horizontalLayout_3.addWidget(self.rollx)
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_3.addWidget(self.label_10)
        self.rolly = QtWidgets.QSpinBox(self.groupBox)
        self.rolly.setMaximum(9999)
        self.rolly.setObjectName("rolly")
        self.horizontalLayout_3.addWidget(self.rolly)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.line_2 = QtWidgets.QFrame(self.groupBox)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_4.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_4.addWidget(self.label_12)
        self.pgx = QtWidgets.QSpinBox(self.groupBox)
        self.pgx.setMaximum(9999)
        self.pgx.setObjectName("pgx")
        self.horizontalLayout_4.addWidget(self.pgx)
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_4.addWidget(self.label_13)
        self.pgy = QtWidgets.QSpinBox(self.groupBox)
        self.pgy.setMaximum(9999)
        self.pgy.setObjectName("pgy")
        self.horizontalLayout_4.addWidget(self.pgy)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_5.addWidget(self.label_14)
        self.label_15 = QtWidgets.QLabel(self.groupBox)
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_5.addWidget(self.label_15)
        self.mt = QtWidgets.QSpinBox(self.groupBox)
        self.mt.setMaximum(9999)
        self.mt.setObjectName("mt")
        self.horizontalLayout_5.addWidget(self.mt)
        self.label_16 = QtWidgets.QLabel(self.groupBox)
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_5.addWidget(self.label_16)
        self.mb = QtWidgets.QSpinBox(self.groupBox)
        self.mb.setMaximum(9999)
        self.mb.setObjectName("mb")
        self.horizontalLayout_5.addWidget(self.mb)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.line_5 = QtWidgets.QFrame(self.groupBox)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout.addWidget(self.line_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_17 = QtWidgets.QLabel(self.groupBox)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_6.addWidget(self.label_17)
        self.label_18 = QtWidgets.QLabel(self.groupBox)
        self.label_18.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_6.addWidget(self.label_18)
        self.ml = QtWidgets.QSpinBox(self.groupBox)
        self.ml.setMaximum(9999)
        self.ml.setObjectName("ml")
        self.horizontalLayout_6.addWidget(self.ml)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.line_6 = QtWidgets.QFrame(self.groupBox)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.verticalLayout.addWidget(self.line_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")

        self.label_19 = QtWidgets.QLabel(self.groupBox)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_7.addWidget(self.label_19)

        self.lineoffset = QtWidgets.QSpinBox(self.groupBox)
        self.lineoffset.setMaximum(9999)
        self.lineoffset.setObjectName("lineoffset")
        self.horizontalLayout_7.addWidget(self.lineoffset)


        self.horizontalLayout_55 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_55.setObjectName("horizontalLayout_55")

        self.label_22 = QtWidgets.QLabel(self.groupBox)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_55.addWidget(self.label_22)

        self.fontsize = QtWidgets.QSpinBox(self.groupBox)
        self.fontsize.setMaximum(9999)
        self.fontsize.setObjectName("fontsize")
        self.horizontalLayout_55.addWidget(self.fontsize)


        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.verticalLayout.addLayout(self.horizontalLayout_55)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(270, 10, 621, 621))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 3262, 4442))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gen_img = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.gen_img.setText("")

        #self.gen_img.setPixmap(QtGui.QPixmap("E:/Users/sonu/Downloads/backcover.jpg"))

        self.gen_img.setMaximumSize(QtCore.QSize(570, 773))
        self.gen_img.setBaseSize(QtCore.QSize(565, 650))

        self.gen_img.setScaledContents(True)
        self.gen_img.setAlignment(QtCore.Qt.AlignCenter)
        self.gen_img.setObjectName("gen_img")
        self.verticalLayout_2.addWidget(self.gen_img)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(910, 10, 301, 61))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.generateimg_button = QtWidgets.QPushButton(self.groupBox_2)
        self.generateimg_button.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.generateimg_button.setObjectName("generateimg_button")
        self.verticalLayout_3.addWidget(self.generateimg_button)

        self.generateimg_button.clicked.connect(self.generate_page)

        self.pdf_area = QtWidgets.QScrollArea(self.centralwidget)
        self.pdf_area.setGeometry(QtCore.QRect(909, 109, 301, 511))
        self.pdf_area.setWidgetResizable(True)
        self.pdf_area.setObjectName("pdf_area")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 299, 509))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.content = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_2)
        self.content.setObjectName("content")
        self.verticalLayout_4.addWidget(self.content)
        self.pdf_area.setWidget(self.scrollAreaWidgetContents_2)


        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(914, 70, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("background-color: rgb(65, 65, 65);\n"
"color: rgb(255, 255, 255);")
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
       
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1226, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # set default values of margins and alignments
        self.titlex.setValue(800)
        self.titley.setValue(340)

        self.namex.setValue(2000)
        self.namey.setValue(100)

        self.rollx.setValue(2000)
        self.rolly.setValue(200)

        self.pgx.setValue(3000)
        self.pgy.setValue(100)

        self.mt.setValue(486)
        self.mb.setValue(270)
        self.ml.setValue(519)

        self.lineoffset.setValue(18)
        self.fontsize.setValue(120)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Cover Image"))
        self.img_button.setText(_translate("MainWindow", "Select"))
        self.label_20.setText(_translate("MainWindow", "Font file"))
        self.fontfile_button.setText(_translate("MainWindow", "Select"))
        self.label1.setText(_translate("MainWindow", "You Name"))
        self.name_2.setText(_translate("MainWindow", "Roll No"))
        self.name_3.setText(_translate("MainWindow", "Page Title"))
        self.name_5.setText(_translate("MainWindow", "Page No"))
        self.groupBox.setTitle(_translate("MainWindow", "Position/ Alignment"))
        self.label.setText(_translate("MainWindow", "Title"))
        self.label_3.setText(_translate("MainWindow", "x:"))
        self.label_4.setText(_translate("MainWindow", "Y:"))
        self.label_5.setText(_translate("MainWindow", "Name"))
        self.label_6.setText(_translate("MainWindow", "x:"))
        self.label_7.setText(_translate("MainWindow", "Y:"))
        self.label_8.setText(_translate("MainWindow", "Roll No"))
        self.label_9.setText(_translate("MainWindow", "x:"))
        self.label_10.setText(_translate("MainWindow", "Y:"))
        self.label_11.setText(_translate("MainWindow", "Page No"))
        self.label_12.setText(_translate("MainWindow", "x:"))
        self.label_13.setText(_translate("MainWindow", "Y:"))
        self.label_14.setText(_translate("MainWindow", "Margins"))
        self.label_15.setText(_translate("MainWindow", "top"))
        self.label_16.setText(_translate("MainWindow", "bottom"))
        self.label_17.setText(_translate("MainWindow", "Margin"))
        self.label_18.setText(_translate("MainWindow", "left"))
        self.label_19.setText(_translate("MainWindow", "Line offset"))
        self.label_22.setText(_translate("MainWindow", "Font Size"))
        self.label_23.setText(_translate("MainWindow", "CONTENT"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Build"))
        self.generateimg_button.setText(_translate("MainWindow", "Generate Page"))


    def text_wrap(self, text, font, max_width):
        lines = []

        if font.getsize(text)[0]  <= max_width:
            lines.append(text)
        else:
            words = text.split(' ')
            i = 0
            while i < len(words):
                line = ''
                while i < len(words) and font.getsize(line + words[i])[0] <= max_width:
                    line = line + words[i]+ " "
                    i += 1
                if not line:
                    line = words[i]
                    i += 1
                lines.append(line)
        return lines

    def textToHand(self, name, roll, title, content, pg):

        img = Image.open(self.coverimg_path)
        font = ImageFont.truetype(self.fontfile_path,size = self.fontsize.value())

        color = 'rgb(0, 0, 0)'
        #Create draw object
        draw = ImageDraw.Draw(img)

        # Title of page
        (x ,y) = (self.titlex.value(),self.titley.value())
        draw.text((x, y), title, fill=color, font=font)

        # name and roll no
        (x ,y) = (self.namex.value(),self.namey.value())
        draw.text((x, y), name, fill=color, font=font)
        (x ,y) = (self.rollx.value(),self.rolly.value())
        draw.text((x, y), roll, fill=color, font=font)

        # page no
        (x ,y) = (self.pgx.value(),self.pgy.value())
        draw.text((x, y), pg, fill=color, font=font)

        l_margin = self.ml.value()
        text = content
        lines = self.text_wrap(text, font, img.size[0]- l_margin)
        line_height = font.getsize('hg')[1]
        t_margin = self.mt.value()
        for line in lines:
            draw.text((l_margin,t_margin), line, fill=color, font=font)
            t_margin += self.lineoffset.value()
            t_margin = t_margin + line_height
            if t_margin >= img.size[1] - self.mb.value():
                break 

        img_name = name+roll+'pg'+pg+'.jpg'
        if img_name == '':
            img_name = 'temp1'
        img.save(img_name)
        self.gen_img.setPixmap(QtGui.QPixmap(img_name))
   

    def generate_page(self):
        name = self.name.text()
        roll = self.roll.text()
        title = self.title.text()
        pgno = self.pgno.text()
        content = self.content.toPlainText()
        # content1 = content.get()
        if self.coverimg_path!='' and self.fontfile_path!='':
            self.textToHand(name, roll, title, content, pgno)
            img_name = 'gimg'+str(self.img_cnt)+'.jpg'

    def askcoverimage(self):
        path, _ = QFileDialog.getOpenFileName(None, "Select cover page")
        if path != '':
            self.coverimg_path = path

    def askfontfile(self):
        path, _ = QFileDialog.getOpenFileName(None, "Select custom font")
        if path != '':
            self.fontfile_path = path



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
