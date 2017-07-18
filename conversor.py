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
        mainWindow.resize(452, 210)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.txtArquivo = QtWidgets.QLineEdit(self.centralwidget)
        self.txtArquivo.setEnabled(False)
        self.txtArquivo.setGeometry(QtCore.QRect(10, 40, 301, 25))
        self.txtArquivo.setObjectName("txtArquivo")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 331, 16))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btnConverter = QtWidgets.QPushButton(self.centralwidget)
        self.btnConverter.setGeometry(QtCore.QRect(140, 130, 131, 27))
        self.btnConverter.setObjectName("btnConverter")
        self.btnSelecionar = QtWidgets.QPushButton(self.centralwidget)
        self.btnSelecionar.setGeometry(QtCore.QRect(320, 40, 91, 21))
        self.btnSelecionar.setObjectName("btnSelecionar")
        self.txtCurso = QtWidgets.QLineEdit(self.centralwidget)
        self.txtCurso.setGeometry(QtCore.QRect(10, 90, 211, 25))
        self.txtCurso.setObjectName("txtCurso")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(230, 70, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.txtGrupo = QtWidgets.QLineEdit(self.centralwidget)
        self.txtGrupo.setGeometry(QtCore.QRect(230, 90, 181, 25))
        self.txtGrupo.setObjectName("txtGrupo")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 452, 25))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)
        mainWindow.setTabOrder(self.txtArquivo, self.btnSelecionar)
        mainWindow.setTabOrder(self.btnSelecionar, self.txtCurso)
        mainWindow.setTabOrder(self.txtCurso, self.txtGrupo)
        mainWindow.setTabOrder(self.txtGrupo, self.btnConverter)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Conversor SIGAA para CSV"))
        self.label.setText(_translate("mainWindow", "HTML dos participantes"))
        self.btnConverter.setText(_translate("mainWindow", "Converter"))
        self.btnSelecionar.setText(_translate("mainWindow", "Selecionar"))
        self.label_3.setText(_translate("mainWindow", "ID do curso"))
        self.label_4.setText(_translate("mainWindow", "Grupo dos participantes"))

