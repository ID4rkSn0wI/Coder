from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(633, 522)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("background-color: rgb(27, 29, 35);\n"
"color: #FFF;\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setStyleSheet("QTabWidget {    \n"
"    background-color: rgb(27, 29, 35);\n"
"    color: #FFF;\n"
"}\n"
"QTabWidget::pane {\n"
"  border: 1px solid  rgb(34, 36, 44);\n"
"  top:-1px; \n"
"  background: rgb(245, 245, 245);\n"
"} \n"
"\n"
"QTabBar::tab {\n"
"  background: rgb(34, 36, 44); \n"
"  border: 2px solid rgb(37, 39, 48);\n"
"  color: #FFF;\n"
"  padding: 7px;\n"
"} \n"
"\n"
"QTabBar::tab:selected { \n"
"  background: rgb(34, 36, 44);\n"
"  color: #FFF;\n"
"  margin-bottom: -1px;\n"
"  border: 2px solid rgb(48, 50, 62);\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.encryptButton = QtWidgets.QPushButton(self.tab)
        self.encryptButton.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.encryptButton.setFont(font)
        self.encryptButton.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 10px;\n"
"    color: #FFF;\n"
"    padding-right: 10px;\n"
"    padding-left: 10px;\n"
"    background-color: rgb(34, 36, 44);\n"
"}\n"
"QPushButton:hover {\n"
"    border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QPushButton:focus {\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"    background-color: rgb(43, 45, 46);\n"
"}")
        self.encryptButton.setObjectName("encryptButton")
        self.gridLayout_4.addWidget(self.encryptButton, 0, 1, 1, 1)
        self.key = QtWidgets.QLineEdit(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.key.sizePolicy().hasHeightForWidth())
        self.key.setSizePolicy(sizePolicy)
        self.key.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.key.setFont(font)
        self.key.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 20px;\n"
"    color: #FFF;\n"
"    padding-right: 20px;\n"
"    padding-left: 20px;\n"
"    background-color: rgb(34, 36, 44);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"    background-color: rgb(43, 45, 46);\n"
"}")
        self.key.setObjectName("key")
        self.gridLayout_4.addWidget(self.key, 2, 0, 1, 1)
        self.message = QtWidgets.QLineEdit(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.message.sizePolicy().hasHeightForWidth())
        self.message.setSizePolicy(sizePolicy)
        self.message.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.message.setFont(font)
        self.message.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 20px;\n"
"    color: #FFF;\n"
"    padding-right: 20px;\n"
"    padding-left: 20px;\n"
"    background-color: rgb(34, 36, 44);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"    background-color: rgb(43, 45, 46);\n"
"}")
        self.message.setObjectName("message")
        self.gridLayout_4.addWidget(self.message, 0, 0, 1, 1)
        self.result = QtWidgets.QLineEdit(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.result.sizePolicy().hasHeightForWidth())
        self.result.setSizePolicy(sizePolicy)
        self.result.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.result.setFont(font)
        self.result.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 20px;\n"
"    color: #FFF;\n"
"    padding-right: 20px;\n"
"    padding-left: 20px;\n"
"    background-color: rgb(34, 36, 44);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"    background-color: rgb(43, 45, 46);\n"
"}")
        self.result.setReadOnly(True)
        self.result.setObjectName("result")
        self.gridLayout_4.addWidget(self.result, 4, 0, 1, 2)
        self.decryptButton = QtWidgets.QPushButton(self.tab)
        self.decryptButton.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.decryptButton.setFont(font)
        self.decryptButton.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 10px;\n"
"    color: #FFF;\n"
"    padding-right: 10px;\n"
"    padding-left: 10px;\n"
"    background-color: rgb(34, 36, 44);\n"
"}\n"
"QPushButton:hover {\n"
"    border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QPushButton:focus {\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"    background-color: rgb(43, 45, 46);\n"
"}")
        self.decryptButton.setObjectName("decryptButton")
        self.gridLayout_4.addWidget(self.decryptButton, 2, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_4.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_4.addItem(spacerItem1, 3, 0, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_4)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem2, 1, 0, 1, 1)
        self.encryptButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.encryptButton_2.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.encryptButton_2.setFont(font)
        self.encryptButton_2.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 10px;\n"
"    color: #FFF;\n"
"    padding-right: 10px;\n"
"    padding-left: 10px;\n"
"    background-color: rgb(34, 36, 44);\n"
"}\n"
"QPushButton:hover {\n"
"    border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QPushButton:focus {\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"    background-color: rgb(43, 45, 46);\n"
"}")
        self.encryptButton_2.setObjectName("encryptButton_2")
        self.gridLayout_3.addWidget(self.encryptButton_2, 0, 1, 1, 1)
        self.message_2 = QtWidgets.QLineEdit(self.tab_2)
        self.message_2.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.message_2.setFont(font)
        self.message_2.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 20px;\n"
"    color: #FFF;\n"
"    padding-right: 20px;\n"
"    padding-left: 20px;\n"
"    background-color: rgb(34, 36, 44);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"    background-color: rgb(43, 45, 46);\n"
"}")
        self.message_2.setObjectName("message_2")
        self.gridLayout_3.addWidget(self.message_2, 0, 0, 1, 1)
        self.result_2 = QtWidgets.QLineEdit(self.tab_2)
        self.result_2.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.result_2.setFont(font)
        self.result_2.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 20px;\n"
"    color: #FFF;\n"
"    padding-right: 20px;\n"
"    padding-left: 20px;\n"
"    background-color: rgb(34, 36, 44);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"    background-color: rgb(43, 45, 46);\n"
"}")
        self.result_2.setReadOnly(True)
        self.result_2.setObjectName("result_2")
        self.gridLayout_3.addWidget(self.result_2, 4, 0, 1, 2)
        self.decryptButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.decryptButton_2.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.decryptButton_2.setFont(font)
        self.decryptButton_2.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 10px;\n"
"    color: #FFF;\n"
"    padding-right: 10px;\n"
"    padding-left: 10px;\n"
"    background-color: rgb(34, 36, 44);\n"
"}\n"
"QPushButton:hover {\n"
"    border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QPushButton:focus {\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"    background-color: rgb(43, 45, 46);\n"
"}")
        self.decryptButton_2.setObjectName("decryptButton_2")
        self.gridLayout_3.addWidget(self.decryptButton_2, 2, 1, 1, 1)
        self.shift = QtWidgets.QLineEdit(self.tab_2)
        self.shift.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.shift.setFont(font)
        self.shift.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 20px;\n"
"    color: #FFF;\n"
"    padding-right: 20px;\n"
"    padding-left: 20px;\n"
"    background-color: rgb(34, 36, 44);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"    background-color: rgb(43, 45, 46);\n"
"}")
        self.shift.setObjectName("shift")
        self.gridLayout_3.addWidget(self.shift, 2, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem3, 3, 0, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_3)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem4, 1, 0, 1, 1)
        self.result_3 = QtWidgets.QLineEdit(self.tab_3)
        self.result_3.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.result_3.setFont(font)
        self.result_3.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 20px;\n"
"    color: #FFF;\n"
"    padding-right: 20px;\n"
"    padding-left: 20px;\n"
"    background-color: rgb(34, 36, 44);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"    background-color: rgb(43, 45, 46);\n"
"}")
        self.result_3.setReadOnly(True)
        self.result_3.setObjectName("result_3")
        self.gridLayout_2.addWidget(self.result_3, 4, 0, 1, 2)
        self.shift_2 = QtWidgets.QLineEdit(self.tab_3)
        self.shift_2.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.shift_2.setFont(font)
        self.shift_2.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 20px;\n"
"    color: #FFF;\n"
"    padding-right: 20px;\n"
"    padding-left: 20px;\n"
"    background-color: rgb(34, 36, 44);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"    background-color: rgb(43, 45, 46);\n"
"}")
        self.shift_2.setObjectName("shift_2")
        self.gridLayout_2.addWidget(self.shift_2, 2, 0, 1, 1)
        self.encryptButton_3 = QtWidgets.QPushButton(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.encryptButton_3.sizePolicy().hasHeightForWidth())
        self.encryptButton_3.setSizePolicy(sizePolicy)
        self.encryptButton_3.setMinimumSize(QtCore.QSize(30, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.encryptButton_3.setFont(font)
        self.encryptButton_3.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 10px;\n"
"    color: #FFF;\n"
"    padding-right: 10px;\n"
"    padding-left: 10px;\n"
"    background-color: rgb(34, 36, 44);\n"
"}\n"
"QPushButton:hover {\n"
"    border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QPushButton:focus {\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"    background-color: rgb(43, 45, 46);\n"
"}")
        self.encryptButton_3.setObjectName("encryptButton_3")
        self.gridLayout_2.addWidget(self.encryptButton_3, 0, 1, 1, 1)
        self.decryptButton_3 = QtWidgets.QPushButton(self.tab_3)
        self.decryptButton_3.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.decryptButton_3.setFont(font)
        self.decryptButton_3.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 10px;\n"
"    color: #FFF;\n"
"    padding-right: 10px;\n"
"    padding-left: 10px;\n"
"    background-color: rgb(34, 36, 44);\n"
"}\n"
"QPushButton:hover {\n"
"    border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QPushButton:focus {\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"    background-color: rgb(43, 45, 46);\n"
"}")
        self.decryptButton_3.setObjectName("decryptButton_3")
        self.gridLayout_2.addWidget(self.decryptButton_3, 2, 1, 1, 1)
        self.message_3 = QtWidgets.QLineEdit(self.tab_3)
        self.message_3.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.message_3.setFont(font)
        self.message_3.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 20px;\n"
"    color: #FFF;\n"
"    padding-right: 20px;\n"
"    padding-left: 20px;\n"
"    background-color: rgb(34, 36, 44);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"    background-color: rgb(43, 45, 46);\n"
"}")
        self.message_3.setObjectName("message_3")
        self.gridLayout_2.addWidget(self.message_3, 0, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem5, 3, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.message_4 = QtWidgets.QLineEdit(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.message_4.sizePolicy().hasHeightForWidth())
        self.message_4.setSizePolicy(sizePolicy)
        self.message_4.setMinimumSize(QtCore.QSize(0, 110))
        self.message_4.setMaximumSize(QtCore.QSize(16777215, 110))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.message_4.setFont(font)
        self.message_4.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 20px;\n"
"    color: #FFF;\n"
"    padding-right: 20px;\n"
"    padding-left: 20px;\n"
"    background-color: rgb(34, 36, 44);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"    background-color: rgb(43, 45, 46);\n"
"}")
        self.message_4.setObjectName("message_4")
        self.horizontalLayout.addWidget(self.message_4, 0, QtCore.Qt.AlignVCenter)
        spacerItem6 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.encryptButton_4 = QtWidgets.QPushButton(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.encryptButton_4.sizePolicy().hasHeightForWidth())
        self.encryptButton_4.setSizePolicy(sizePolicy)
        self.encryptButton_4.setMinimumSize(QtCore.QSize(0, 50))
        self.encryptButton_4.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.encryptButton_4.setFont(font)
        self.encryptButton_4.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 10px;\n"
"    color: #FFF;\n"
"    padding-right: 10px;\n"
"    padding-left: 10px;\n"
"    background-color: rgb(34, 36, 44);\n"
"}\n"
"QPushButton:hover {\n"
"    border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QPushButton:focus {\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"    background-color: rgb(43, 45, 46);\n"
"}")
        self.encryptButton_4.setObjectName("encryptButton_4")
        self.verticalLayout_7.addWidget(self.encryptButton_4, 0, QtCore.Qt.AlignBottom)
        spacerItem7 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_7.addItem(spacerItem7)
        self.decryptButton_4 = QtWidgets.QPushButton(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.decryptButton_4.sizePolicy().hasHeightForWidth())
        self.decryptButton_4.setSizePolicy(sizePolicy)
        self.decryptButton_4.setMinimumSize(QtCore.QSize(0, 50))
        self.decryptButton_4.setMaximumSize(QtCore.QSize(16777215, 50))
        self.decryptButton_4.setBaseSize(QtCore.QSize(0, 10))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.decryptButton_4.setFont(font)
        self.decryptButton_4.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 10px;\n"
"    color: #FFF;\n"
"    padding-right: 10px;\n"
"    padding-left: 10px;\n"
"    background-color: rgb(34, 36, 44);\n"
"}\n"
"QPushButton:hover {\n"
"    border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QPushButton:focus {\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"    background-color: rgb(43, 45, 46);\n"
"}")
        self.decryptButton_4.setObjectName("decryptButton_4")
        self.verticalLayout_7.addWidget(self.decryptButton_4, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout.addLayout(self.verticalLayout_7)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.result_4 = QtWidgets.QLineEdit(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.result_4.sizePolicy().hasHeightForWidth())
        self.result_4.setSizePolicy(sizePolicy)
        self.result_4.setMinimumSize(QtCore.QSize(0, 110))
        self.result_4.setMaximumSize(QtCore.QSize(16777215, 110))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.result_4.setFont(font)
        self.result_4.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 20px;\n"
"    color: #FFF;\n"
"    padding-right: 20px;\n"
"    padding-left: 20px;\n"
"    background-color: rgb(34, 36, 44);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"    background-color: rgb(43, 45, 46);\n"
"}")
        self.result_4.setReadOnly(True)
        self.result_4.setObjectName("result_4")
        self.verticalLayout_8.addWidget(self.result_4, 0, QtCore.Qt.AlignVCenter)
        self.verticalLayout_6.addLayout(self.verticalLayout_8)
        self.verticalLayout_2.addLayout(self.verticalLayout_6)
        self.tabWidget.addTab(self.tab_4, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tabWidget, self.message)
        MainWindow.setTabOrder(self.message, self.result)
        MainWindow.setTabOrder(self.result, self.key)
        MainWindow.setTabOrder(self.key, self.encryptButton)
        MainWindow.setTabOrder(self.encryptButton, self.decryptButton)
        MainWindow.setTabOrder(self.decryptButton, self.decryptButton_2)
        MainWindow.setTabOrder(self.decryptButton_2, self.encryptButton_2)
        MainWindow.setTabOrder(self.encryptButton_2, self.result_2)
        MainWindow.setTabOrder(self.result_2, self.shift)
        MainWindow.setTabOrder(self.shift, self.message_2)
        MainWindow.setTabOrder(self.message_2, self.decryptButton_3)
        MainWindow.setTabOrder(self.decryptButton_3, self.message_3)
        MainWindow.setTabOrder(self.message_3, self.encryptButton_3)
        MainWindow.setTabOrder(self.encryptButton_3, self.result_3)
        MainWindow.setTabOrder(self.result_3, self.shift_2)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.encryptButton.setText(_translate("MainWindow", "Зашифровать"))
        self.key.setPlaceholderText(_translate("MainWindow", "Ключ"))
        self.message.setPlaceholderText(_translate("MainWindow", "Сообщение"))
        self.result.setPlaceholderText(_translate("MainWindow", "Вывод"))
        self.decryptButton.setText(_translate("MainWindow", "Расшифровать"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Вижинер"))
        self.encryptButton_2.setText(_translate("MainWindow", "Зашифровать"))
        self.message_2.setPlaceholderText(_translate("MainWindow", "Сообщение"))
        self.result_2.setPlaceholderText(_translate("MainWindow", "Вывод"))
        self.decryptButton_2.setText(_translate("MainWindow", "Расшифровать"))
        self.shift.setPlaceholderText(_translate("MainWindow", "Сдвиг"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Цезарь"))
        self.result_3.setPlaceholderText(_translate("MainWindow", "Вывод"))
        self.shift_2.setPlaceholderText(_translate("MainWindow", "Сдвиг"))
        self.encryptButton_3.setText(_translate("MainWindow", "Зашифровать"))
        self.decryptButton_3.setText(_translate("MainWindow", "Расшифровать"))
        self.message_3.setPlaceholderText(_translate("MainWindow", "Сообщение"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Полибей"))
        self.message_4.setPlaceholderText(_translate("MainWindow", "Сообщение"))
        self.encryptButton_4.setText(_translate("MainWindow", "Зашифровать"))
        self.decryptButton_4.setText(_translate("MainWindow", "Расшифровать"))
        self.result_4.setPlaceholderText(_translate("MainWindow", "Вывод"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Личный"))
