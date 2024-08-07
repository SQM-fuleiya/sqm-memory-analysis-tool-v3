# !TODO 基于vol3制作的内存镜像分析工具。给自己玩切勿商用
# -*- coding: utf-8 -*-
# !/usr/bin/python3
# SQM的内存镜像分析工具
# v1.2

import os
from PySide6.QtCore import Signal
from PySide6.QtGui import  QDragEnterEvent , QDropEvent 
from PySide6.QtWidgets import QApplication , QWidget 
from main_ui import Ui_main_wandows
import multiprocessing
import function 

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()           # 初始化父类
        self.ui = Ui_main_wandows()  # 实例化UI类
        self.ui.setupUi(self)        # 设置UI
        self.setAcceptDrops(True)    # 设置 input_echo 窗口可以接受拖拽放入文件
        self.ui.start_but.clicked.connect(lambda : function.start(self))      # 开始执行   
        self.ui.file_dump.clicked.connect(lambda : function.转储文件(self))    # 文件导出
        self.ui.tiqu_but.clicked.connect(lambda : function.进程导出(self))     # 进程导出
        self.ui.mem_but.clicked.connect(lambda : function.内存导出(self))      # 内存导出
        self.ui.sd_but.clicked.connect(lambda : function.手动分析())           # 手动分析

    # 鼠标托放到程序后接受文件名
    def dragEnterEvent(self, a0:QDragEnterEvent) -> None:  
        if a0.mimeData().hasUrls() : # 判断有没有接受到文件路径,有的话保存文件路径，没有的话忽略
            a0.accept()             # 接受文件内容 ，a0 里面保存有文件的路径
        else:
            a0.ignore()    # 忽略文件内容

    # 鼠标释放事件，并执行一些操作
    def dropEvent(self, a0: QDropEvent) -> None:
        if a0.mimeData().hasUrls():
            self.ui.filepath_line.clear()
            for 路径 in a0.mimeData().urls():
                function.file_name = 路径.toLocalFile()
                function.file_path = os.path.split(路径.toLocalFile())[0]+'/'
                self.ui.filepath_line.setText(function.file_name)
        print(function.file_name )
        print(function.file_path)

if __name__ == "__main__":
    app = QApplication()
    windows = MainWindow()
    multiprocessing.freeze_support()
    windows.show()
    app.exec()

