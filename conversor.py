# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'conversor.ui'
#
# Created by: PyQt5 UI code generator 5.8
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(374, 159)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.txtArquivo = QtWidgets.QLineEdit(self.centralwidget)
        self.txtArquivo.setEnabled(False)
        self.txtArquivo.setGeometry(QtCore.QRect(10, 40, 241, 25))
        self.txtArquivo.setObjectName("txtArquivo")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 331, 16))
        self.label.setObjectName("label")
        self.btnConverter = QtWidgets.QPushButton(self.centralwidget)
        self.btnConverter.setGeometry(QtCore.QRect(120, 70, 91, 27))
        self.btnConverter.setObjectName("btnConverter")
        self.btnSelecionar = QtWidgets.QPushButton(self.centralwidget)
        self.btnSelecionar.setGeometry(QtCore.QRect(260, 40, 91, 27))
        self.btnSelecionar.setObjectName("btnSelecionar")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 374, 25))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Conversor SIGAA para CSV"))
        self.label.setText(_translate("mainWindow", "Nome do Arquivo"))
        self.btnConverter.setText(_translate("mainWindow", "Converter"))
        self.btnSelecionar.setText(_translate("mainWindow", "Selecionar"))

