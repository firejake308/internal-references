# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer\previewer.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from aqt.qt import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1000, 720)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnBrowse = QPushButton(Dialog)
        self.btnBrowse.setAutoDefault(False)
        self.btnBrowse.setObjectName("btnBrowse")
        self.horizontalLayout.addWidget(self.btnBrowse)
        self.btnBacklinks = QPushButton(Dialog)
        self.btnBacklinks.setAutoDefault(False)
        self.btnBacklinks.setObjectName("btnBacklinks")
        self.horizontalLayout.addWidget(self.btnBacklinks)
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnClose = QPushButton(Dialog)
        self.btnClose.setObjectName("btnClose")
        self.horizontalLayout.addWidget(self.btnClose)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        self.btnClose.pressed.connect(Dialog.accept)
        QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.btnBrowse, self.btnBacklinks)
        Dialog.setTabOrder(self.btnBacklinks, self.btnClose)

    def retranslateUi(self, Dialog):
        _translate = QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Internal References Previewer"))
        self.btnBrowse.setToolTip(_translate("Dialog", "Show card in Browser (Alt+B)"))
        self.btnBrowse.setText(_translate("Dialog", "Open in &Browser"))
        self.btnBacklinks.setToolTip(_translate("Dialog", "Find notes linking to this card (Alt+L)"))
        self.btnBacklinks.setText(_translate("Dialog", "Show Back&links"))
        self.btnClose.setText(_translate("Dialog", "&Close"))
