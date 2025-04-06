import os
import re

from PIL import Image, ImageQt
import numpy as np
from PIL.ImageCms import profileToProfile


class CImage:
    def __init__(self, path):
        self._path = path

        if self._path and os.path.exists(self._path):
            self._sourceImage = Image.open(self._path)
            self._image = self._sourceImage
            self._fileName = re.split(r'[\\/]', self._path)[-1]
            self._sourceImageMatrix = np.array(self._sourceImage)
        else:
            self._sourceImageMatrix = None

        if self._sourceImageMatrix is not None:
            self._sourceHeight, self._sourceWidth, self._channels = self._sourceImageMatrix.shape
            self._sourceQImage = ImageQt.ImageQt(self._sourceImage)
            self._sourcePixmap = ImageQt.QPixmap.fromImage(ImageQt.QImage(self._sourceQImage))
            self._qImage = self._sourceQImage
            self._pixmap = self._sourcePixmap

        self._destinationHeight = 0
        self._destinationWidth = 0

        self._imageIdent = True


    @property
    def image(self):
        return self._image

    @property
    def sourceImage(self):
        return self._sourceImage

    @property
    def pixmap(self):
        return self._pixmap

    @property
    def qImage(self):
        return self._qImage

    @property
    def sourcePixmap(self):
        return self._sourcePixmap

    @property
    def sourceQImage(self):
        return self._sourceQImage

    @property
    def fileName(self):
        return self._fileName

    @property
    def sourceSize(self):
        return self._sourceHeight, self._sourceWidth

    @property
    def destinationSize(self):
        return self._destinationHeight, self._destinationWidth


    def setNeededSize(self, width, height):
        if (self._sourceWidth != width or self._sourceHeight != height) and (self._sourceWidth and self._sourceHeight):
            self._destinationWidth = width
            self._destinationHeight = height
            self._imageIdent = False


    def resize(self):
        if self._imageIdent:
            return False

        scaleX = (self._sourceWidth - 1) / (self._destinationWidth - (1 if self._destinationWidth>1 else 0))
        scaleY = (self._sourceHeight - 1) / (self._destinationHeight - (1 if self._destinationHeight>1 else 0))

        self.destinationImageMatrix = np.empty((self._destinationHeight, self._destinationWidth, self._channels),
                                               dtype=self._sourceImageMatrix.dtype)

        for destinationY in range(self._destinationHeight):
            for destinationX in range(self._destinationWidth):
                sourceX = destinationX * scaleX
                sourceY = destinationY * scaleY

                sourceX_rounded = self.clamp(round(sourceX), 0, self._sourceWidth - 1)
                sourceY_rounded = self.clamp(round(sourceY), 0, self._sourceHeight - 1)

                self.destinationImageMatrix[destinationY, destinationX] = self._sourceImageMatrix[sourceY_rounded, sourceX_rounded]

        self._image = Image.fromarray(self.destinationImageMatrix)
        self._qImage = ImageQt.ImageQt(self._image)
        self._pixmap = ImageQt.QPixmap.fromImage(ImageQt.QImage(self._qImage))

        return True


    def saveImage(self):
        if self._imageIdent:
            return
        newImage = Image.fromarray(self.destinationImageMatrix)
        newImage.save(self._path)


    @staticmethod
    def clamp(value, minimum, maximum):
        return max(minimum, min(value, maximum))


