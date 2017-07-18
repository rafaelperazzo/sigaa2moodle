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
from funcoes import *

def btnConverterClick():
    curso = str(ui.txtCurso.text())
    grupo = str(ui.txtGrupo.text())
        
    if str(ui.txtArquivo.text())!='' and curso!='' and grupo!='':
        fileName = QFileDialog.getSaveFileName(None, 'Salvar Como...', '','CSV (*.csv *.txt)')
        csv = str(fileName[0])
        html = file2string(str(ui.txtArquivo.text()))
        tabela = string2tabela(html,curso,"student",grupo)
        tabela2csv(tabela,csv)
        ui.statusbar.showMessage('SUCESSO!',5000)
    else:
        ui.statusbar.showMessage('FALHA!!',5000)

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

window.show()
sys.exit(app.exec_())