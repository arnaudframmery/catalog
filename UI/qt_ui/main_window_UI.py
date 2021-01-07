# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CatalogUI(object):
    def setupUi(self, CatalogUI):
        CatalogUI.setObjectName("CatalogUI")
        CatalogUI.resize(798, 531)
        self.centralwidget = QtWidgets.QWidget(CatalogUI)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        CatalogUI.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CatalogUI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 798, 21))
        self.menubar.setObjectName("menubar")
        CatalogUI.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CatalogUI)
        self.statusbar.setObjectName("statusbar")
        CatalogUI.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(CatalogUI)
        self.toolBar.setObjectName("toolBar")
        CatalogUI.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action_add_catalog = QtWidgets.QAction(CatalogUI)
        self.action_add_catalog.setObjectName("action_add_catalog")
        self.action_remove_catalog = QtWidgets.QAction(CatalogUI)
        self.action_remove_catalog.setObjectName("action_remove_catalog")
        self.toolBar.addAction(self.action_add_catalog)
        self.toolBar.addAction(self.action_remove_catalog)

        self.retranslateUi(CatalogUI)
        QtCore.QMetaObject.connectSlotsByName(CatalogUI)

    def retranslateUi(self, CatalogUI):
        _translate = QtCore.QCoreApplication.translate
        CatalogUI.setWindowTitle(_translate("CatalogUI", "CatalogUI"))
        self.toolBar.setWindowTitle(_translate("CatalogUI", "toolBar"))
        self.action_add_catalog.setText(_translate("CatalogUI", "add"))
        self.action_add_catalog.setToolTip(_translate("CatalogUI", "add new catalog"))
        self.action_remove_catalog.setText(_translate("CatalogUI", "remove"))
        self.action_remove_catalog.setToolTip(_translate("CatalogUI", "remove a catalog"))

