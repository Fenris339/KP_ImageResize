import os

from PyQt6.QtWidgets import (
    QApplication, QDialog, QVBoxLayout,
    QPushButton, QFileDialog, QMainWindow, QGraphicsScene, QGraphicsPixmapItem, QMessageBox
)
from PyQt6.QtCore import QModelIndex, Qt, QAbstractTableModel
from PyQt6.QtGui import QIcon, QPixmap

from Image import CImage
from Ui_MainWindow import Ui_MainWindow


class CApp(QApplication):
    def __init__(self, argv):
        super(CApp, self).__init__(argv)

class CMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        QApplication.mainWindow = self
        self.setupUi(self)
        self.setWindowTitle("ImageResizer")
        self.setWindowIcon(QIcon("./res/icon.ico"))
        self.scene = QGraphicsScene(self)
        self.imgView.setScene(self.scene)
        self.modelImages = None
        self.btnSaveClicked = False
        self.btnFilesOrDirectory.clicked.connect(self.selectFilesOrDirectory)
        self.btnSaveDirectionSize.clicked.connect(self.saveDirectionSize)


    def saveDirectionSize(self):
        selectedIndexes = self.tblImages.selectedIndexes()
        if not selectedIndexes:
            return QMessageBox.information(self, "Внимание!", "Сначала необходимо добавить изображения!")
        index = selectedIndexes[0]
        if index.isValid():
            row = index.row()
            image = self.tblImages.model().getImage(row)
            destinationWidth = self.edtDirectionWidth.value()
            destinationHeight = self.edtDirectionHeight.value()
            if destinationWidth and destinationHeight:
                if self.chkDirectionSizeToAll.checkState() == Qt.CheckState.Unchecked:
                    image.setNeededSize(destinationWidth, destinationHeight)
                else:
                    imageList = self.tblImages.model().getImage()
                    for img in imageList:
                        img.setNeededSize(destinationWidth, destinationHeight)
                self.tblImages.viewport().update()
            else:
                QMessageBox.information(self, "Внимание!", "Не задана необходимая высота или ширина!")


    def on_selection_changed(self, selected, deselected):
        index = selected.indexes()[0]
        if index.isValid():
            row = index.row()

            for item in self.scene.items():
                self.scene.removeItem(item)
            image = self.tblImages.model().getImage(row)
            pixmap = QPixmap.fromImage(image.getQImage())
            pixmapItem = QGraphicsPixmapItem(pixmap)
            self.scene.addItem(pixmapItem)
            image_width = pixmap.width()
            image_height = pixmap.height()
            self.scene.setSceneRect(0, 0, image_width, image_height)

            sourceHeight, sourceWidth = image.getSourceSize()
            self.edtSourceWidth.setText(str(sourceWidth))
            self.edtSourceHeight.setText(str(sourceHeight))

            destinationHeight, destinationWidth = image.getDestinationSize()
            destinationWidth = sourceWidth if not destinationWidth else destinationWidth
            destinationHeight = sourceHeight if not destinationHeight else destinationHeight
            self.edtDirectionWidth.setValue(destinationWidth)
            self.edtDirectionHeight.setValue(destinationHeight)



    def selectFilesOrDirectory(self):
        dialog = CSelectFilesOrDirectoryDialog()
        dialog.exec()
        filesSelected = dialog.filesSelected
        selectedItems = dialog.selectedItems
        images = []
        if filesSelected is not None and filesSelected:
            for item in selectedItems:
                images.append(CImage(item))
        elif filesSelected is not None and not filesSelected:
            for file in os.scandir(selectedItems):
                if file.is_file():
                    images.append(CImage(file.path))
        else:
            return
        self.modelImages = CImageTableModel(images)
        self.tblImages.setModel(self.modelImages)
        self.tblImages.resizeColumnsToContents()
        self.tblImages.resizeRowsToContents()
        self.tblImages.selectionModel().selectionChanged.connect(self.on_selection_changed)
        self.tblImages.selectRow(0)


class CImageTableModel(QAbstractTableModel):
    def __init__(self, images: list, parent=None):
        super().__init__(parent)
        self._images = images
        self._headers = ["Имя", "Исх. Размер", "Необх. Размер","Изображение"]

    def getImage(self, row=None):
        return self._images[row] if row is not None else self._images

    def rowCount(self, parent=QModelIndex()):
        return len(self._images)

    def columnCount(self, parent=QModelIndex()):
        return len(self._headers)

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if not index.isValid():
            return None

        image = self._images[index.row()]
        column = index.column()

        if role == Qt.ItemDataRole.DisplayRole:
            if column == 0:
                return image.getFileName()
            if column == 1:
                h, w = image.getSourceSize()
                return f"Высота: {h}\nШирина: {w}"
            if column == 2:
                h, w = image.getDestinationSize()
                return f"Высота: {h}\nШирина: {w}"

        if role == Qt.ItemDataRole.DecorationRole:
            if column == 3:
                pixmap = image.getPixmap()
                return pixmap.scaled(128, 128, Qt.AspectRatioMode.KeepAspectRatio)

        if role == Qt.ItemDataRole.TextAlignmentRole:
            return Qt.AlignmentFlag.AlignCenter

        return None

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return self._headers[section]
            else:
                return str(section + 1)
        return None


class CSelectFilesOrDirectoryDialog(QDialog):
    def __init__(self, parent=None):
        super(CSelectFilesOrDirectoryDialog, self).__init__(parent)
        self.setWindowTitle("Выберите файлы или папку")
        self.resize(250,50)

        self._filesSelected = None
        self._selectedItems = None

        layout = QVBoxLayout(self)

        self.btnFiles = QPushButton("Выбрать файлы")
        self.btnFiles.clicked.connect(self.selectFiles)
        layout.addWidget(self.btnFiles)

        self.btnDirectory = QPushButton("Выбрать папку")
        self.btnDirectory.clicked.connect(self.selectDirectory)
        layout.addWidget(self.btnDirectory)

    @property
    def filesSelected(self):
        return self._filesSelected

    @property
    def selectedItems(self):
        return self._selectedItems

    def selectFiles(self):
        files, _ = QFileDialog.getOpenFileNames(self, "Выберите файлы", "", "Все файлы (*)")
        if files:
            self._filesSelected = True
            self._selectedItems = files
        self.close()

    def selectDirectory(self):
        folder = QFileDialog.getExistingDirectory(self, "Выберите папку")
        if folder:
            self._filesSelected = False
            self._selectedItems = folder
        self.close()