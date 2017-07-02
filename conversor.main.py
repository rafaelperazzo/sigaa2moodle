#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 13:59:52 2017

@author: rafael
"""

import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QFileDialog
from PyQt5.QtGui import QIcon
#from ui_imagedialog import Ui_ImageDialog
from conversor import *

def btnConverterClick():
    fileName = QFileDialog.getSaveFileName(None, 'Salvar Como...', '','CSV (*.csv *.txt)')
    ui.statusbar.showMessage('Arquivo convertido com sucesso!',5000)

def selecionarArquivo():
    fname = QFileDialog.getOpenFileName(None, 'Selecionar Arquivo', 
   '',"HTML (*.htm *.html)")
    ui.txtArquivo.setText(str(fname[0]))

app = QApplication(sys.argv)
window = QMainWindow()
ui = Ui_mainWindow()
ui.setupUi(window)
ui.btnSelecionar.clicked.connect(selecionarArquivo)
ui.btnConverter.clicked.connect(btnConverterClick)
ui.txtArquivo
window.show()
sys.exit(app.exec_())