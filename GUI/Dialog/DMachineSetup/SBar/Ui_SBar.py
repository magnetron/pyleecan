# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Raphael\Desktop\Git\PyManatee\pyleecan\GUI\Dialog\DMachineSetup\SBar\SBar.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SBar(object):
    def setupUi(self, SBar):
        SBar.setObjectName("SBar")
        SBar.resize(650, 550)
        SBar.setMinimumSize(QtCore.QSize(650, 550))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(SBar)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.g_bar = QtWidgets.QGroupBox(SBar)
        self.g_bar.setObjectName("g_bar")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.g_bar)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout.addItem(spacerItem)
        self.c_bar_type = QtWidgets.QComboBox(self.g_bar)
        self.c_bar_type.setMinimumSize(QtCore.QSize(100, 0))
        self.c_bar_type.setObjectName("c_bar_type")
        self.c_bar_type.addItem("")
        self.c_bar_type.addItem("")
        self.horizontalLayout.addWidget(self.c_bar_type)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.w_bar = QtWidgets.QWidget(self.g_bar)
        self.w_bar.setObjectName("w_bar")
        self.verticalLayout.addWidget(self.w_bar)
        self.verticalLayout_2.addWidget(self.g_bar)
        self.g_ring = QtWidgets.QGroupBox(SBar)
        self.g_ring.setObjectName("g_ring")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.g_ring)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.img_ring = QtWidgets.QLabel(self.g_ring)
        self.img_ring.setMaximumSize(QtCore.QSize(300, 300))
        self.img_ring.setText("")
        self.img_ring.setPixmap(
            QtGui.QPixmap(":/images/images/MachineSetup/Bar/Ring.PNG")
        )
        self.img_ring.setScaledContents(True)
        self.img_ring.setObjectName("img_ring")
        self.horizontalLayout_2.addWidget(self.img_ring)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lf_Lewout = FloatEdit(self.g_ring)
        self.lf_Lewout.setMinimumSize(QtCore.QSize(70, 0))
        self.lf_Lewout.setMaximumSize(QtCore.QSize(100, 20))
        self.lf_Lewout.setObjectName("lf_Lewout")
        self.gridLayout.addWidget(self.lf_Lewout, 2, 1, 1, 1)
        self.unit_Hscr = QtWidgets.QLabel(self.g_ring)
        self.unit_Hscr.setMinimumSize(QtCore.QSize(0, 0))
        self.unit_Hscr.setObjectName("unit_Hscr")
        self.gridLayout.addWidget(self.unit_Hscr, 0, 2, 1, 1)
        self.unit_Lscr = QtWidgets.QLabel(self.g_ring)
        self.unit_Lscr.setMinimumSize(QtCore.QSize(0, 0))
        self.unit_Lscr.setObjectName("unit_Lscr")
        self.gridLayout.addWidget(self.unit_Lscr, 1, 2, 1, 1)
        self.in_Hscr = QtWidgets.QLabel(self.g_ring)
        self.in_Hscr.setMinimumSize(QtCore.QSize(40, 0))
        self.in_Hscr.setObjectName("in_Hscr")
        self.gridLayout.addWidget(self.in_Hscr, 0, 0, 1, 1)
        self.lf_Hscr = FloatEdit(self.g_ring)
        self.lf_Hscr.setMinimumSize(QtCore.QSize(70, 0))
        self.lf_Hscr.setMaximumSize(QtCore.QSize(100, 20))
        self.lf_Hscr.setObjectName("lf_Hscr")
        self.gridLayout.addWidget(self.lf_Hscr, 0, 1, 1, 1)
        self.lf_Lscr = FloatEdit(self.g_ring)
        self.lf_Lscr.setMinimumSize(QtCore.QSize(70, 0))
        self.lf_Lscr.setMaximumSize(QtCore.QSize(100, 20))
        self.lf_Lscr.setObjectName("lf_Lscr")
        self.gridLayout.addWidget(self.lf_Lscr, 1, 1, 1, 1)
        self.unit_Lewout = QtWidgets.QLabel(self.g_ring)
        self.unit_Lewout.setMinimumSize(QtCore.QSize(0, 0))
        self.unit_Lewout.setObjectName("unit_Lewout")
        self.gridLayout.addWidget(self.unit_Lewout, 2, 2, 1, 1)
        self.in_Lewout = QtWidgets.QLabel(self.g_ring)
        self.in_Lewout.setMinimumSize(QtCore.QSize(40, 0))
        self.in_Lewout.setObjectName("in_Lewout")
        self.gridLayout.addWidget(self.in_Lewout, 2, 0, 1, 1)
        self.in_Lscr = QtWidgets.QLabel(self.g_ring)
        self.in_Lscr.setMinimumSize(QtCore.QSize(40, 0))
        self.in_Lscr.setObjectName("in_Lscr")
        self.gridLayout.addWidget(self.in_Lscr, 1, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.w_mat = WMatSelect(self.g_ring)
        self.w_mat.setObjectName("w_mat")
        self.verticalLayout_3.addWidget(self.w_mat)
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_2.addWidget(self.g_ring)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_3.addItem(spacerItem3)
        self.b_plot = QtWidgets.QPushButton(SBar)
        self.b_plot.setObjectName("b_plot")
        self.horizontalLayout_3.addWidget(self.b_plot)
        self.b_previous = QtWidgets.QPushButton(SBar)
        self.b_previous.setObjectName("b_previous")
        self.horizontalLayout_3.addWidget(self.b_previous)
        self.b_next = QtWidgets.QPushButton(SBar)
        self.b_next.setEnabled(True)
        self.b_next.setObjectName("b_next")
        self.horizontalLayout_3.addWidget(self.b_next)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.retranslateUi(SBar)
        QtCore.QMetaObject.connectSlotsByName(SBar)
        SBar.setTabOrder(self.lf_Hscr, self.lf_Lscr)
        SBar.setTabOrder(self.lf_Lscr, self.lf_Lewout)
        SBar.setTabOrder(self.lf_Lewout, self.b_previous)
        SBar.setTabOrder(self.b_previous, self.b_plot)
        SBar.setTabOrder(self.b_plot, self.c_bar_type)

    def retranslateUi(self, SBar):
        _translate = QtCore.QCoreApplication.translate
        SBar.setWindowTitle(_translate("SBar", "Form"))
        self.g_bar.setTitle(_translate("SBar", "Bar"))
        self.c_bar_type.setItemText(0, _translate("SBar", "Rectangular bar"))
        self.c_bar_type.setItemText(1, _translate("SBar", "Die cast bar"))
        self.g_ring.setTitle(_translate("SBar", "Short Circuit Ring"))
        self.unit_Hscr.setText(_translate("SBar", "m"))
        self.unit_Lscr.setText(_translate("SBar", "m"))
        self.in_Hscr.setText(_translate("SBar", "Hscr :"))
        self.unit_Lewout.setText(_translate("SBar", "m"))
        self.in_Lewout.setText(_translate("SBar", "Lewout :"))
        self.in_Lscr.setText(_translate("SBar", "Lscr :"))
        self.b_plot.setText(_translate("SBar", "Preview"))
        self.b_previous.setText(_translate("SBar", "Previous"))
        self.b_next.setText(_translate("SBar", "Save"))


from pyleecan.GUI.Dialog.DMatLib.WMatSelect.WMatSelect import WMatSelect
from pyleecan.GUI.Tools.FloatEdit import FloatEdit
from pyleecan.GUI.Resources import pyleecan_rc
