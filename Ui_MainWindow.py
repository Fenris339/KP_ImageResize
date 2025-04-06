# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1243, 708)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_5.addItem(spacerItem, 1, 1, 1, 1)
        self.btnFilesOrDirectory = QtWidgets.QPushButton(parent=self.frame)
        self.btnFilesOrDirectory.setObjectName("btnFilesOrDirectory")
        self.gridLayout_5.addWidget(self.btnFilesOrDirectory, 1, 0, 1, 1)
        self.tblImages = QtWidgets.QTableView(parent=self.frame)
        self.tblImages.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.tblImages.setProperty("showDropIndicator", False)
        self.tblImages.setDragDropOverwriteMode(False)
        self.tblImages.setAlternatingRowColors(True)
        self.tblImages.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.tblImages.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tblImages.setGridStyle(QtCore.Qt.PenStyle.SolidLine)
        self.tblImages.setObjectName("tblImages")
        self.gridLayout_5.addWidget(self.tblImages, 0, 0, 1, 2)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame_4 = QtWidgets.QFrame(parent=self.frame_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_4 = QtWidgets.QLabel(parent=self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 1)
        self.edtDirectionHeight = QtWidgets.QSpinBox(parent=self.frame_4)
        self.edtDirectionHeight.setMaximum(3000)
        self.edtDirectionHeight.setObjectName("edtDirectionHeight")
        self.gridLayout_3.addWidget(self.edtDirectionHeight, 0, 1, 1, 1)
        self.edtDirectionWidth = QtWidgets.QSpinBox(parent=self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edtDirectionWidth.sizePolicy().hasHeightForWidth())
        self.edtDirectionWidth.setSizePolicy(sizePolicy)
        self.edtDirectionWidth.setMaximum(3000)
        self.edtDirectionWidth.setObjectName("edtDirectionWidth")
        self.gridLayout_3.addWidget(self.edtDirectionWidth, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame_4, 4, 1, 1, 1)
        self.frame_3 = QtWidgets.QFrame(parent=self.frame_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(parent=self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.edtSourceWidth = QtWidgets.QLineEdit(parent=self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edtSourceWidth.sizePolicy().hasHeightForWidth())
        self.edtSourceWidth.setSizePolicy(sizePolicy)
        self.edtSourceWidth.setReadOnly(True)
        self.edtSourceWidth.setObjectName("edtSourceWidth")
        self.gridLayout_2.addWidget(self.edtSourceWidth, 1, 1, 1, 1)
        self.edtSourceHeight = QtWidgets.QLineEdit(parent=self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edtSourceHeight.sizePolicy().hasHeightForWidth())
        self.edtSourceHeight.setSizePolicy(sizePolicy)
        self.edtSourceHeight.setReadOnly(True)
        self.edtSourceHeight.setObjectName("edtSourceHeight")
        self.gridLayout_2.addWidget(self.edtSourceHeight, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.frame_3, 4, 0, 1, 1)
        self.imgView = QtWidgets.QGraphicsView(parent=self.frame_2)
        self.imgView.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.imgView.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.imgView.setLineWidth(1)
        self.imgView.setInteractive(False)
        self.imgView.setObjectName("imgView")
        self.gridLayout_4.addWidget(self.imgView, 0, 0, 1, 3)
        self.progressBar = QtWidgets.QProgressBar(parent=self.frame_2)
        self.progressBar.setEnabled(False)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_4.addWidget(self.progressBar, 7, 0, 1, 3)
        self.label_5 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 3, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        self.gridLayout_4.addItem(spacerItem1, 6, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 3, 1, 1, 1)
        self.btnSave = QtWidgets.QPushButton(parent=self.frame_2)
        self.btnSave.setEnabled(False)
        self.btnSave.setObjectName("btnSave")
        self.gridLayout_4.addWidget(self.btnSave, 8, 1, 1, 1)
        self.btnSaveDirectionSize = QtWidgets.QPushButton(parent=self.frame_2)
        self.btnSaveDirectionSize.setObjectName("btnSaveDirectionSize")
        self.gridLayout_4.addWidget(self.btnSaveDirectionSize, 5, 1, 1, 1)
        self.chkDirectionSizeToAll = QtWidgets.QCheckBox(parent=self.frame_2)
        self.chkDirectionSizeToAll.setObjectName("chkDirectionSizeToAll")
        self.gridLayout_4.addWidget(self.chkDirectionSizeToAll, 3, 2, 3, 1)
        self.gridLayout.addWidget(self.frame_2, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1243, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.chkDirectionSizeToAll.toggled['bool'].connect(self.progressBar.setEnabled) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnFilesOrDirectory.setText(_translate("MainWindow", "Выбрать изображения/директорию"))
        self.label_4.setText(_translate("MainWindow", "Ширина:"))
        self.label_3.setText(_translate("MainWindow", "Высота:"))
        self.label.setText(_translate("MainWindow", "Высота:"))
        self.label_2.setText(_translate("MainWindow", "Ширина:"))
        self.label_5.setText(_translate("MainWindow", "Исходный размер:"))
        self.label_6.setText(_translate("MainWindow", "Необходимый размер:"))
        self.btnSave.setText(_translate("MainWindow", "Сохранить все изменения"))
        self.btnSaveDirectionSize.setText(_translate("MainWindow", "Задать размер"))
        self.chkDirectionSizeToAll.setText(_translate("MainWindow", "Задать единный размер для всех"))
