# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculate.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from utils import *
from matrix import matrix_3x3
import numpy as np


class UiMainWindow:
    """
    Класс отображающий окно с уравнениями.
    """
    def setupUi(self, MainWindow):
        """
        Метод оформляющий окно элементами ввода.
        :param MainWindow:
        :return:
        """
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(510, 332)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(510, 332))
        MainWindow.setMaximumSize(QtCore.QSize(510, 332))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(510, 280))
        self.centralwidget.setMaximumSize(QtCore.QSize(510, 291))
        self.centralwidget.setMouseTracking(True)
        self.centralwidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.centralwidget.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.centralwidget.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 511, 301))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setHorizontalSpacing(22)
        self.gridLayout.setVerticalSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 5, 0, 1, 7)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 0, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 10, 0, 1, 7)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_10.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_10.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout.addWidget(self.lineEdit_10, 2, 4, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_8.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_8.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout.addWidget(self.lineEdit_8, 1, 0, 1, 1)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_12.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_12.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.gridLayout.addWidget(self.lineEdit_12, 2, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 0, 4, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_7.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_7.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout.addWidget(self.lineEdit_7, 1, 2, 1, 1)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_11.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_11.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout.addWidget(self.lineEdit_11, 2, 2, 1, 1)
        self.lineEdit_1 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_1.sizePolicy().hasHeightForWidth())
        self.lineEdit_1.setSizePolicy(sizePolicy)
        self.lineEdit_1.setBaseSize(QtCore.QSize(0, 0))
        self.lineEdit_1.setAutoFillBackground(False)
        self.lineEdit_1.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.gridLayout.addWidget(self.lineEdit_1, 0, 6, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 11, 0, 1, 7)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 1, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_6.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 1, 4, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 5, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 7, 0, 1, 7)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 9, 0, 1, 7)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 8, 0, 1, 7)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 6, 0, 1, 7)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(100, 40))
        self.pushButton.setMaximumSize(QtCore.QSize(500, 40))
        self.pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 2, 1, 3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 0, 2, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 1, 6, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_9.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout.addWidget(self.lineEdit_9, 2, 6, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 5, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 5, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setMinimumSize(QtCore.QSize(2, 0))
        self.label_6.setLineWidth(0)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 510, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.action_3x3 = QtWidgets.QAction(MainWindow)
        self.action_3x3.setObjectName("action_3x3")
        self.menu.addAction(self.action_3x3)
        self.menubar.addAction(self.menu.menuAction())
        self.pushButton.clicked.connect(self.calculate)

        self.retranslate(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslate(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Калькулятор"))
        self.label_10.setText(_translate("MainWindow", "△ ="))
        self.lineEdit_4.setText(_translate("MainWindow", "4"))
        self.label_15.setText(_translate("MainWindow", "x2 ="))
        self.lineEdit_10.setText(_translate("MainWindow", "56"))
        self.lineEdit_8.setText(_translate("MainWindow", "8"))
        self.lineEdit_12.setText(_translate("MainWindow", "12"))
        self.lineEdit_2.setText(_translate("MainWindow", "2"))
        self.lineEdit_7.setText(_translate("MainWindow", "7"))
        self.lineEdit_11.setText(_translate("MainWindow", "11"))
        self.lineEdit_1.setText(_translate("MainWindow", "1"))
        self.label_16.setText(_translate("MainWindow", "x3 ="))
        self.label.setText(_translate("MainWindow", "* x3 ="))
        self.lineEdit_6.setText(_translate("MainWindow", "6"))
        self.label_5.setText(_translate("MainWindow", "* x2 +"))
        self.label_7.setText(_translate("MainWindow", "* x1 +"))
        self.label_12.setText(_translate("MainWindow", "△2 ="))
        self.label_14.setText(_translate("MainWindow", "x1 ="))
        self.label_13.setText(_translate("MainWindow", "△3 ="))
        self.label_11.setText(_translate("MainWindow", "△1 ="))
        self.pushButton.setText(_translate("MainWindow", "Расчитать"))
        self.lineEdit_3.setText(_translate("MainWindow", "3"))
        self.lineEdit_5.setText(_translate("MainWindow", "5"))
        self.lineEdit_9.setText(_translate("MainWindow", "45"))
        self.label_2.setText(_translate("MainWindow", "* x2 +"))
        self.label_4.setText(_translate("MainWindow", "* x1 +"))
        self.label_8.setText(_translate("MainWindow", "* x2 +"))
        self.label_3.setText(_translate("MainWindow", " * x1 +"))
        self.label_9.setText(_translate("MainWindow", "* x3 ="))
        self.label_6.setText(_translate("MainWindow", "* x3 ="))
        self.menu.setTitle(_translate("MainWindow", "Режим"))
        self.action_3x3.setText(_translate("MainWindow", "Режим матрицы 3x3"))

    def calculate(self):
        """
        Логика уравнений.
        :return:
        """
        lineedits = {"lineedit_1": self.lineEdit_1,
                     "lineedit_2": self.lineEdit_2,
                     "lineedit_3": self.lineEdit_3,
                     "lineedit_4": self.lineEdit_4,
                     "lineEdit_5": self.lineEdit_5,
                     "lineEdit_6": self.lineEdit_6,
                     "lineEdit_7": self.lineEdit_7,
                     "lineEdit_8": self.lineEdit_8,
                     "lineEdit_9": self.lineEdit_9,
                     "lineEdit_10": self.lineEdit_10,
                     "lineEdit_11": self.lineEdit_11,
                     "lineEdit_12": self.lineEdit_12}
        # Преобразует в строку value, потом в число.
        value_to_int = bypass_list([value.text() for name, value in lineedits.items()])

        a1 = value_to_int[:4]  # Строка верхняя
        a2 = value_to_int[4:8]  # Строка посередине
        a3 = value_to_int[8:12]  # Строка нижняя

        matrix = np.array([a1, a2, a3])  # Многоуровневый список

        # Записывается результат матрицы
        determinant = [matrix_3x3(matrix)]

        for i in range(3):
            list1, list2, list3 = a1.copy(), a2.copy(), a3.copy()  # Копируются строки
            # Идет замена каждого элемента для расчетов.
            list1[i] = list1[3]
            list2[i] = list2[3]
            list3[i] = list3[3]

            matrix = np.array([list1, list2, list3])  # Многоуровневый список

            # Записывается результат матриц
            determinant.append(matrix_3x3(matrix))

        # Сравнение и вычисление x1, x2, x3
        if determinant[0] > 0 or determinant[0] < 0:
            x1 = determinant[1]/determinant[0]
            x2 = determinant[2]/determinant[0]
            x3 = determinant[3]/determinant[0]

            self.label_10.setText(f"△ = {determinant[0]}")
            self.label_11.setText(f"△1 = {determinant[1]}")
            self.label_12.setText(f"△2 = {determinant[2]}")
            self.label_13.setText(f"△3 = {determinant[3]}")
            self.label_14.setText(f"x1 = {x1}")
            self.label_15.setText(f"x2 = {x2}")    
            self.label_16.setText(f"x3 = {x3}")
        else:
            self.label_10.setText(f"△= {determinant[0]}")
            self.label_11.setText("△1 = ")
            self.label_12.setText("△2 = ")
            self.label_13.setText("△3 = ")
            self.label_14.setText("x1 = ")
            self.label_15.setText("x2 = ")
            self.label_16.setText("x3 = ")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())