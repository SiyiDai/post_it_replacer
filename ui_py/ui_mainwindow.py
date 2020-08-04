# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(904, 629)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding,
            QtWidgets.QSizePolicy.MinimumExpanding,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_10.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.replace_image_groupbox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.replace_image_groupbox.sizePolicy().hasHeightForWidth()
        )
        self.replace_image_groupbox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.replace_image_groupbox.setFont(font)
        self.replace_image_groupbox.setObjectName("replace_image_groupbox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.replace_image_groupbox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.replace_image_label = QtWidgets.QLabel(self.replace_image_groupbox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.replace_image_label.sizePolicy().hasHeightForWidth()
        )
        self.replace_image_label.setSizePolicy(sizePolicy)
        self.replace_image_label.setMinimumSize(QtCore.QSize(420, 240))
        self.replace_image_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.replace_image_label.setText("")
        self.replace_image_label.setScaledContents(True)
        self.replace_image_label.setObjectName("replace_image_label")
        self.gridLayout_2.addWidget(self.replace_image_label, 0, 0, 1, 1)
        self.horizontalLayout_3.addWidget(self.replace_image_groupbox)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.original_source_groupbox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.original_source_groupbox.setFont(font)
        self.original_source_groupbox.setObjectName("original_source_groupbox")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.original_source_groupbox)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.original_source_label = QtWidgets.QLabel(self.original_source_groupbox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.original_source_label.sizePolicy().hasHeightForWidth()
        )
        self.original_source_label.setSizePolicy(sizePolicy)
        self.original_source_label.setMinimumSize(QtCore.QSize(400, 240))
        self.original_source_label.setText("")
        self.original_source_label.setScaledContents(True)
        self.original_source_label.setObjectName("original_source_label")
        self.verticalLayout_4.addWidget(self.original_source_label)
        self.gridLayout_11.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.verticalLayout_5.addWidget(self.original_source_groupbox)
        self.gridLayout_10.addLayout(self.verticalLayout_5, 0, 1, 1, 1)
        self.replacement_result_groupbox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.replacement_result_groupbox.setFont(font)
        self.replacement_result_groupbox.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop
        )
        self.replacement_result_groupbox.setObjectName("replacement_result_groupbox")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.replacement_result_groupbox)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton_picture = QtWidgets.QRadioButton(
            self.replacement_result_groupbox
        )
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.radioButton_picture.setFont(font)
        self.radioButton_picture.setChecked(True)
        self.radioButton_picture.setObjectName("radioButton_picture")
        self.horizontalLayout_2.addWidget(self.radioButton_picture)
        self.radioButton_video = QtWidgets.QRadioButton(
            self.replacement_result_groupbox
        )
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.radioButton_video.setFont(font)
        self.radioButton_video.setObjectName("radioButton_video")
        self.horizontalLayout_2.addWidget(self.radioButton_video)
        self.radioButton_camera = QtWidgets.QRadioButton(
            self.replacement_result_groupbox
        )
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.radioButton_camera.sizePolicy().hasHeightForWidth()
        )
        self.radioButton_camera.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.radioButton_camera.setFont(font)
        self.radioButton_camera.setObjectName("radioButton_camera")
        self.horizontalLayout_2.addWidget(self.radioButton_camera)
        self.pushButton_replace = QtWidgets.QPushButton(
            self.replacement_result_groupbox
        )
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.pushButton_replace.setFont(font)
        self.pushButton_replace.setObjectName("pushButton_replace")
        self.horizontalLayout_2.addWidget(self.pushButton_replace)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.replacement_result_label = QtWidgets.QLabel(
            self.replacement_result_groupbox
        )
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.replacement_result_label.sizePolicy().hasHeightForWidth()
        )
        self.replacement_result_label.setSizePolicy(sizePolicy)
        self.replacement_result_label.setMinimumSize(QtCore.QSize(400, 240))
        self.replacement_result_label.setText("")
        self.replacement_result_label.setObjectName("replacement_result_label")
        self.gridLayout_9.addWidget(self.replacement_result_label, 3, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.post_it_color_label = QtWidgets.QLabel(self.replacement_result_groupbox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.post_it_color_label.sizePolicy().hasHeightForWidth()
        )
        self.post_it_color_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.post_it_color_label.setFont(font)
        self.post_it_color_label.setObjectName("post_it_color_label")
        self.horizontalLayout_4.addWidget(self.post_it_color_label)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_4.addItem(spacerItem)
        self.post_it_lineEdit = QtWidgets.QLineEdit(self.replacement_result_groupbox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.post_it_lineEdit.sizePolicy().hasHeightForWidth()
        )
        self.post_it_lineEdit.setSizePolicy(sizePolicy)
        self.post_it_lineEdit.setMaximumSize(QtCore.QSize(30, 16777215))
        self.post_it_lineEdit.setObjectName("post_it_lineEdit")
        self.horizontalLayout_4.addWidget(self.post_it_lineEdit)
        self.post_it_color_pushButton = QtWidgets.QPushButton(
            self.replacement_result_groupbox
        )
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.post_it_color_pushButton.sizePolicy().hasHeightForWidth()
        )
        self.post_it_color_pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.post_it_color_pushButton.setFont(font)
        self.post_it_color_pushButton.setObjectName("post_it_color_pushButton")
        self.horizontalLayout_4.addWidget(self.post_it_color_pushButton)
        self.gridLayout_9.addLayout(self.horizontalLayout_4, 4, 0, 1, 1)
        self.verticalLayout_7.addLayout(self.gridLayout_9)
        self.gridLayout_8.addLayout(self.verticalLayout_7, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Minimum,
            QtWidgets.QSizePolicy.MinimumExpanding,
        )
        self.gridLayout_8.addItem(spacerItem1, 1, 0, 1, 1)
        self.gridLayout_10.addWidget(self.replacement_result_groupbox, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 904, 25))
        self.menubar.setObjectName("menubar")
        self.menuMain = QtWidgets.QMenu(self.menubar)
        self.menuMain.setObjectName("menuMain")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoader = QtWidgets.QAction(MainWindow)
        self.actionLoader.setObjectName("actionLoader")
        self.menuMain.addSeparator()
        self.menuMain.addAction(self.actionLoader)
        self.menubar.addAction(self.menuMain.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Post-it Replace"))
        self.replace_image_groupbox.setTitle(_translate("MainWindow", "Replace Image"))
        self.original_source_groupbox.setTitle(
            _translate("MainWindow", "Original Source")
        )
        self.replacement_result_groupbox.setTitle(
            _translate("MainWindow", "Replacement Result")
        )
        self.radioButton_picture.setText(_translate("MainWindow", "Picture"))
        self.radioButton_video.setText(_translate("MainWindow", "Video"))
        self.radioButton_camera.setText(_translate("MainWindow", "Camera"))
        self.pushButton_replace.setText(_translate("MainWindow", "Replace"))
        self.post_it_color_label.setText(_translate("MainWindow", "Post-it Color:"))
        self.post_it_color_pushButton.setText(_translate("MainWindow", "Select"))
        self.menuMain.setTitle(_translate("MainWindow", "File"))
        self.actionLoader.setText(_translate("MainWindow", "Load..."))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
