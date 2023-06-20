# -*- coding: utf-8 -*-
# Date: 2023/6/20 19:45
# Author: Homer Kwok
import sys

import win32api
import win32con
import win32gui
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QMainWindow, QApplication, QGraphicsDropShadowEffect
from qfluentwidgets import InfoBar, InfoBarPosition

from untitled_ui import Ui_MainWindow


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)  # 加载UI

        # 定义状态实体
        self.status = False

        # 设置无边框窗口(注释这部分代码后显示正常)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        # self.setGraphicsEffect(
        #     QGraphicsDropShadowEffect(
        #         parent=self,
        #         blurRadius=20,
        #         xOffset=0,
        #         yOffset=0,
        #         color=QColor(0, 200, 0, 160)
        #     )
        # )

        # 创建信号与槽的连接
        self.pushButton_normal.clicked.connect(self.message_normal)
        self.pushButton_abnormal.clicked.connect(self.message_abnormal)

    def message_normal(self):
        InfoBar.success(
            title='无法连接服务器！',
            content='',
            orient=Qt.Vertical,
            isClosable=True,
            position=InfoBarPosition.TOP,
            duration=2000,
            parent=self
        )

    def message_abnormal(self):
        InfoBar.success(
            title='无法连接服务器！',
            content='',
            orient=Qt.Vertical,
            isClosable=True,
            position=InfoBarPosition.TOP,
            duration=2000,
            parent=self.frame
        )

    def mousePressEvent(self, QMouseEvent):
        """ 移动窗口 """
        hwnd = self.winId()
        win32gui.ReleaseCapture()
        win32api.SendMessage(hwnd, win32con.WM_SYSCOMMAND, win32con.SC_MOVE + win32con.HTCAPTION, 0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec())
