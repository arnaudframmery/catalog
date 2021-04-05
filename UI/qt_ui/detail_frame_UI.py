# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'detail_frame.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from UI.widget.button import Button


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(866, 437)
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.return_button = Button(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.return_button.sizePolicy().hasHeightForWidth())
        self.return_button.setSizePolicy(sizePolicy)
        self.return_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.return_button.setAutoDefault(False)
        self.return_button.setDefault(False)
        self.return_button.setFlat(False)
        self.return_button.setObjectName("return_button")
        self.horizontalLayout.addWidget(self.return_button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(Form)
        self.label.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.line_edit_label = QtWidgets.QLineEdit(Form)
        self.line_edit_label.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_edit_label.sizePolicy().hasHeightForWidth())
        self.line_edit_label.setSizePolicy(sizePolicy)
        self.line_edit_label.setAlignment(QtCore.Qt.AlignCenter)
        self.line_edit_label.setObjectName("line_edit_label")
        self.horizontalLayout.addWidget(self.line_edit_label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.cancel_button = Button(Form)
        self.cancel_button.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancel_button.sizePolicy().hasHeightForWidth())
        self.cancel_button.setSizePolicy(sizePolicy)
        self.cancel_button.setCheckable(False)
        self.cancel_button.setAutoExclusive(False)
        self.cancel_button.setAutoDefault(False)
        self.cancel_button.setDefault(False)
        self.cancel_button.setFlat(False)
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout.addWidget(self.cancel_button)
        self.modify_layout_button = Button(Form)
        self.modify_layout_button.setObjectName("modify_layout_button")
        self.horizontalLayout.addWidget(self.modify_layout_button)
        self.modify_button = Button(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modify_button.sizePolicy().hasHeightForWidth())
        self.modify_button.setSizePolicy(sizePolicy)
        self.modify_button.setObjectName("modify_button")
        self.horizontalLayout.addWidget(self.modify_button)
        self.delete_button = Button(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delete_button.sizePolicy().hasHeightForWidth())
        self.delete_button.setSizePolicy(sizePolicy)
        self.delete_button.setObjectName("delete_button")
        self.horizontalLayout.addWidget(self.delete_button)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.return_button.setText(_translate("Form", "Return"))
        self.label.setText(_translate("Form", "TextLabel"))
        self.cancel_button.setText(_translate("Form", "Cancel"))
        self.modify_layout_button.setText(_translate("Form", "Tile Management"))
        self.modify_button.setText(_translate("Form", "Modify"))
        self.delete_button.setText(_translate("Form", "Delete"))
