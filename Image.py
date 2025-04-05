import os

from PIL import Image
import numpy as np


class CImage:
    def __init__(self, path):
        self._path = path

        if self._path and os.path.exists(self._path):
            image = Image.open(path)
            self._fileName = self._path.split('/')[-1]
            self._sourceImageMatrix = np.array(image)
        else:
            self._sourceImageMatrix = None

        if self._sourceImageMatrix is not None:
            self._sourceHeight, self._sourceWidth, self._channels = self._sourceImageMatrix.shape

        self._destinationHeight = 0
        self._destinationWidth = 0

        self._imageIdent = True


    def getFileName(self):
        return self._fileName

    def getSourceSize(self):
        return self._sourceHeight, self._sourceWidth

    def getDestinationSize(self):
        return self._destinationHeight, self._destinationWidth

    def getFilePath(self):
        return self._path

    def setNeededSize(self, width, height):
        if (self._sourceWidth != width or self._sourceHeight != height) and (self._sourceWidth and self._sourceHeight):
            self._destinationWidth = width
            self._destinationHeight = height
            self._imageIdent = False


    def resize(self):
        if self._imageIdent:
            return

        scaleX = (self._sourceWidth - 1) / (self._destinationWidth - 1)
        scaleY = (self._sourceHeight - 1) / (self._destinationHeight - 1)

        self.destinationImageMatrix = np.empty((self._destinationHeight, self._destinationWidth, self._channels),
                                               dtype=self._sourceImageMatrix.dtype)

        for destinationY in range(self._destinationHeight):
            for destinationX in range(self._destinationWidth):
                sourceX = destinationX * scaleX
                sourceY = destinationY * scaleY

                sourceX_rounded = self.clamp(round(sourceX), 0, self._sourceWidth - 1)
                sourceY_rounded = self.clamp(round(sourceY), 0, self._sourceHeight - 1)

                self.destinationImageMatrix[destinationY, destinationX] = self._sourceImageMatrix[sourceY_rounded, sourceX_rounded]


    def saveImage(self):
        if self._imageIdent:
            return
        newImage = Image.fromarray(self.destinationImageMatrix)
        newImage.save(self._path)


    @staticmethod
    def clamp(value, minimum, maximum):
        return max(minimum, min(value, maximum))


