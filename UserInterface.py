import os

from PyQt6.QtWidgets import (
    QApplication, QDialog, QVBoxLayout,
    QPushButton, QFileDialog, QMainWindow, QGraphicsScene, QGraphicsPixmapItem, QMessageBox
)
from PyQt6.QtCore import QModelIndex, Qt, QAbstractTableModel, QObject, pyqtSignal, QThread
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
        self._saveState = CDirtyManager()
        self._saveState.dirtyChanged.connect(self.btnSave.setEnabled)
        self.btnFilesOrDirectory.clicked.connect(self.selectFilesOrDirectory)
        self.btnSaveDirectionSize.clicked.connect(self.saveDirectionSize)


    def saveDirectionSize(self):

        def on_processing_finished(result, row):
            if True in result:
                self._saveState.dirty = True
                self.updateImgView(image[row])
            self.tblImages.viewport().update()

        selectedIndexes = self.tblImages.selectedIndexes()
        if not selectedIndexes:
            return QMessageBox.information(self, "Внимание!", "Сначала необходимо добавить изображения!")
        index = selectedIndexes[0]
        if index.isValid():
            row = index.row()
            image = self.tblImages.model().getImage()
            destinationWidth = self.edtDirectionWidth.value()
            destinationHeight = self.edtDirectionHeight.value()
            if destinationWidth and destinationHeight:
                result = []
                if self.chkDirectionSizeToAll.checkState() == Qt.CheckState.Unchecked:
                    image[row].setNeededSize(destinationWidth, destinationHeight)
                    image[row].resize()
                    result.append(image[row].resize())
                    on_processing_finished(result, row)
                else:
                    self.worker = CImageProcessor('resizer', image, destinationWidth, destinationHeight, row)
                    self.worker.progressChanged.connect(self.progressBar.setValue)
                    self.worker.processingFinished.connect(on_processing_finished)
                    self.worker.start()
            else:
                QMessageBox.information(self, "Внимание!", "Не задана необходимая высота или ширина!")

    def updateImgView(self, image):
        for item in self.scene.items():
            self.scene.removeItem(item)
        pixmap = QPixmap.fromImage(image.qImage)
        pixmapItem = QGraphicsPixmapItem(pixmap)
        self.scene.addItem(pixmapItem)
        image_width = pixmap.width()
        image_height = pixmap.height()
        self.scene.setSceneRect(0, 0, image_width, image_height)


    def on_selection_changed(self, selected, deselected):
        index = selected.indexes()[0]
        if index.isValid():
            row = index.row()

            image = self.tblImages.model().getImage(row)
            self.updateImgView(image)

            sourceHeight, sourceWidth = image.sourceSize
            self.edtSourceWidth.setText(str(sourceWidth))
            self.edtSourceHeight.setText(str(sourceHeight))

            destinationHeight, destinationWidth = image.destinationSize
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
        self._saveState.dirty = False


class CImageProcessor(QThread):
    progressChanged = pyqtSignal(int)
    processingFinished = pyqtSignal(list, int)

    def __init__(self, type, images, width=None, height=None, row=None):
        super().__init__()
        self.type = type
        self.images = images
        self.width = width
        self.height = height
        self.row = row
        self._result = []

    def run(self):
        if self.type == 'saver':
            self.saver()
        elif self.type == 'resizer':
            self.resizer()

    def saver(self):
        pass

    def resizer(self):
        total = len(self.images)
        for i, img in enumerate(self.images):
            img.setNeededSize(self.width, self.height)
            self._result.append(img.resize())

            percent = int((i + 1) * 100 / total)
            self.progressChanged.emit(percent)

        self.processingFinished.emit(self.result, self.startRow)

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value

    @property
    def startRow(self):
        return self.row


class CDirtyManager(QObject):
    dirtyChanged = pyqtSignal(bool)

    def __init__(self):
        super().__init__()
        self._dirty = False

    @property
    def dirty(self):
        return self._dirty

    @dirty.setter
    def dirty(self, value: bool):
        if self._dirty != value:
            self._dirty = value
            self.dirtyChanged.emit(value)


class CImageTableModel(QAbstractTableModel):
    def __init__(self, images: list, parent=None):
        super().__init__(parent)
        self._images = images
        self._headers = ["Имя", "Исх. Размер", "Необх. Размер", "Изображение"]

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
                return image.fileName
            if column == 1:
                h, w = image.sourceSize
                return f"Высота: {h}\nШирина: {w}"
            if column == 2:
                h, w = image.destinationSize
                return f"Высота: {h}\nШирина: {w}"

        if role == Qt.ItemDataRole.DecorationRole:
            if column == 3:
                pixmap = image.sourcePixmap
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
        self.resize(300,50)

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