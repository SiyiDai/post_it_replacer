# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/load_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoadDialog(object):
    def setupUi(self, LoadDialog):
        LoadDialog.setObjectName("LoadDialog")
        LoadDialog.resize(712, 157)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LoadDialog.sizePolicy().hasHeightForWidth())
        LoadDialog.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QtWidgets.QGridLayout(LoadDialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.buttonBox = QtWidgets.QDialogButtonBox(LoadDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok
        )
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.select_original_video_button = QtWidgets.QPushButton(LoadDialog)
        self.select_original_video_button.setObjectName("select_original_video_button")
        self.gridLayout.addWidget(self.select_original_video_button, 3, 2, 1, 1)
        self.original_picture_line_edit = QtWidgets.QLineEdit(LoadDialog)
        self.original_picture_line_edit.setText("")
        self.original_picture_line_edit.setObjectName("original_picture_line_edit")
        self.gridLayout.addWidget(self.original_picture_line_edit, 2, 1, 1, 1)
        self.replace_image_line_edit = QtWidgets.QLineEdit(LoadDialog)
        self.replace_image_line_edit.setObjectName("replace_image_line_edit")
        self.gridLayout.addWidget(self.replace_image_line_edit, 0, 1, 1, 1)
        self.select_original_picture_button = QtWidgets.QPushButton(LoadDialog)
        self.select_original_picture_button.setObjectName(
            "select_original_picture_button"
        )
        self.gridLayout.addWidget(self.select_original_picture_button, 2, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(LoadDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.select_replace_image_button = QtWidgets.QPushButton(LoadDialog)
        self.select_replace_image_button.setObjectName("select_replace_image_button")
        self.gridLayout.addWidget(self.select_replace_image_button, 0, 2, 1, 1)
        self.original_video_line_edit = QtWidgets.QLineEdit(LoadDialog)
        self.original_video_line_edit.setObjectName("original_video_line_edit")
        self.gridLayout.addWidget(self.original_video_line_edit, 3, 1, 1, 1)
        self.line_2 = QtWidgets.QFrame(LoadDialog)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 1, 0, 1, 3)
        self.label_8 = QtWidgets.QLabel(LoadDialog)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(LoadDialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(LoadDialog)
        self.buttonBox.accepted.connect(LoadDialog.accept)
        self.buttonBox.rejected.connect(LoadDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(LoadDialog)

    def retranslateUi(self, LoadDialog):
        _translate = QtCore.QCoreApplication.translate
        LoadDialog.setWindowTitle(_translate("LoadDialog", "Dialog"))
        self.select_original_video_button.setText(_translate("LoadDialog", "select"))
        self.select_original_picture_button.setText(_translate("LoadDialog", "select"))
        self.label_2.setText(_translate("LoadDialog", "Original Picture:"))
        self.select_replace_image_button.setText(_translate("LoadDialog", "select"))
        self.label_8.setText(_translate("LoadDialog", "Original Video:"))
        self.label_5.setText(_translate("LoadDialog", "Replace Image:"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    LoadDialog = QtWidgets.QDialog()
    ui = Ui_LoadDialog()
    ui.setupUi(LoadDialog)
    LoadDialog.show()
    sys.exit(app.exec_())
