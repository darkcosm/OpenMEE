# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'preferences_dlg.ui'
#
# Created: Fri Oct 11 16:53:24 2013
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(396, 412)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(112, 220, 188))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(112, 220, 188))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(112, 220, 188))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        Dialog.setPalette(palette)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_8.addWidget(self.label)
        self.digits_spinBox = QtGui.QSpinBox(Dialog)
        self.digits_spinBox.setMaximum(10)
        self.digits_spinBox.setProperty("value", 3)
        self.digits_spinBox.setObjectName(_fromUtf8("digits_spinBox"))
        self.horizontalLayout_8.addWidget(self.digits_spinBox)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_6.addWidget(self.label_2)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_6.addWidget(self.label_3)
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 0, 1, 1, 1)
        self.default_bg = QtGui.QPushButton(self.groupBox)
        self.default_bg.setMinimumSize(QtCore.QSize(30, 25))
        self.default_bg.setMaximumSize(QtCore.QSize(30, 25))
        self.default_bg.setText(_fromUtf8(""))
        self.default_bg.setObjectName(_fromUtf8("default_bg"))
        self.gridLayout_2.addWidget(self.default_bg, 2, 1, 1, 1)
        self.colors_layout = QtGui.QVBoxLayout()
        self.colors_layout.setObjectName(_fromUtf8("colors_layout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_fg = QtGui.QPushButton(self.groupBox)
        self.label_fg.setMinimumSize(QtCore.QSize(30, 25))
        self.label_fg.setMaximumSize(QtCore.QSize(30, 25))
        self.label_fg.setStyleSheet(_fromUtf8("background-color: rgb(255, 0, 255);"))
        self.label_fg.setText(_fromUtf8(""))
        self.label_fg.setObjectName(_fromUtf8("label_fg"))
        self.horizontalLayout_3.addWidget(self.label_fg)
        self.label_bg = QtGui.QPushButton(self.groupBox)
        self.label_bg.setMinimumSize(QtCore.QSize(30, 25))
        self.label_bg.setMaximumSize(QtCore.QSize(30, 25))
        self.label_bg.setText(_fromUtf8(""))
        self.label_bg.setObjectName(_fromUtf8("label_bg"))
        self.horizontalLayout_3.addWidget(self.label_bg)
        self.colors_layout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.cat_fg = QtGui.QPushButton(self.groupBox)
        self.cat_fg.setMinimumSize(QtCore.QSize(30, 25))
        self.cat_fg.setMaximumSize(QtCore.QSize(30, 25))
        self.cat_fg.setText(_fromUtf8(""))
        self.cat_fg.setObjectName(_fromUtf8("cat_fg"))
        self.horizontalLayout.addWidget(self.cat_fg)
        self.cat_bg = QtGui.QPushButton(self.groupBox)
        self.cat_bg.setMinimumSize(QtCore.QSize(30, 25))
        self.cat_bg.setMaximumSize(QtCore.QSize(30, 25))
        self.cat_bg.setText(_fromUtf8(""))
        self.cat_bg.setObjectName(_fromUtf8("cat_bg"))
        self.horizontalLayout.addWidget(self.cat_bg)
        self.colors_layout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.count_fg = QtGui.QPushButton(self.groupBox)
        self.count_fg.setMinimumSize(QtCore.QSize(30, 25))
        self.count_fg.setMaximumSize(QtCore.QSize(30, 25))
        self.count_fg.setText(_fromUtf8(""))
        self.count_fg.setObjectName(_fromUtf8("count_fg"))
        self.horizontalLayout_2.addWidget(self.count_fg)
        self.count_bg = QtGui.QPushButton(self.groupBox)
        self.count_bg.setMinimumSize(QtCore.QSize(30, 25))
        self.count_bg.setMaximumSize(QtCore.QSize(30, 25))
        self.count_bg.setText(_fromUtf8(""))
        self.count_bg.setObjectName(_fromUtf8("count_bg"))
        self.horizontalLayout_2.addWidget(self.count_bg)
        self.colors_layout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.cont_fg = QtGui.QPushButton(self.groupBox)
        self.cont_fg.setMinimumSize(QtCore.QSize(30, 25))
        self.cont_fg.setMaximumSize(QtCore.QSize(30, 25))
        self.cont_fg.setText(_fromUtf8(""))
        self.cont_fg.setObjectName(_fromUtf8("cont_fg"))
        self.horizontalLayout_4.addWidget(self.cont_fg)
        self.cont_bg = QtGui.QPushButton(self.groupBox)
        self.cont_bg.setMinimumSize(QtCore.QSize(30, 25))
        self.cont_bg.setMaximumSize(QtCore.QSize(30, 25))
        self.cont_bg.setText(_fromUtf8(""))
        self.cont_bg.setObjectName(_fromUtf8("cont_bg"))
        self.horizontalLayout_4.addWidget(self.cont_bg)
        self.colors_layout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.calc_fg = QtGui.QPushButton(self.groupBox)
        self.calc_fg.setMinimumSize(QtCore.QSize(30, 25))
        self.calc_fg.setMaximumSize(QtCore.QSize(30, 25))
        self.calc_fg.setText(_fromUtf8(""))
        self.calc_fg.setObjectName(_fromUtf8("calc_fg"))
        self.horizontalLayout_5.addWidget(self.calc_fg)
        self.calc_bg = QtGui.QPushButton(self.groupBox)
        self.calc_bg.setMinimumSize(QtCore.QSize(30, 25))
        self.calc_bg.setMaximumSize(QtCore.QSize(30, 25))
        self.calc_bg.setText(_fromUtf8(""))
        self.calc_bg.setObjectName(_fromUtf8("calc_bg"))
        self.horizontalLayout_5.addWidget(self.calc_bg)
        self.colors_layout.addLayout(self.horizontalLayout_5)
        self.gridLayout_2.addLayout(self.colors_layout, 1, 1, 1, 1)
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_2.addWidget(self.label_9, 2, 0, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_12 = QtGui.QLabel(self.groupBox)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.verticalLayout_2.addWidget(self.label_12)
        self.label_14 = QtGui.QLabel(self.groupBox)
        self.label_14.setMinimumSize(QtCore.QSize(128, 0))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.verticalLayout_2.addWidget(self.label_14)
        self.label_11 = QtGui.QLabel(self.groupBox)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.verticalLayout_2.addWidget(self.label_11)
        self.label_13 = QtGui.QLabel(self.groupBox)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.verticalLayout_2.addWidget(self.label_13)
        self.label_10 = QtGui.QLabel(self.groupBox)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.verticalLayout_2.addWidget(self.label_10)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 1, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 2, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.choose_font_btn = QtGui.QPushButton(Dialog)
        self.choose_font_btn.setObjectName(_fromUtf8("choose_font_btn"))
        self.horizontalLayout_7.addWidget(self.choose_font_btn)
        self.font_preview_lbl = QtGui.QLabel(Dialog)
        self.font_preview_lbl.setObjectName(_fromUtf8("font_preview_lbl"))
        self.horizontalLayout_7.addWidget(self.font_preview_lbl)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Preferences", None))
        self.label.setText(_translate("Dialog", "# digits to display: ", None))
        self.groupBox.setTitle(_translate("Dialog", "Color Choices", None))
        self.label_2.setText(_translate("Dialog", "Foreground", None))
        self.label_3.setText(_translate("Dialog", "Background", None))
        self.label_9.setText(_translate("Dialog", "Default cell background:", None))
        self.label_12.setText(_translate("Dialog", "label", None))
        self.label_14.setText(_translate("Dialog", "Categorical Variable", None))
        self.label_11.setText(_translate("Dialog", "Count Variable", None))
        self.label_13.setText(_translate("Dialog", "Continuous Variable", None))
        self.label_10.setText(_translate("Dialog", "Effect Size/Variance", None))
        self.choose_font_btn.setText(_translate("Dialog", "Choose Font", None))
        self.font_preview_lbl.setText(_translate("Dialog", "Font preview area", None))

