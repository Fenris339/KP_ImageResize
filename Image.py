import os

from PIL import Image
import numpy as np


class CImage:
    def __init__(self, path):
        self.path = path

        if self.path and os.path.exists(self.path):
            image = Image.open(path)
            self._fileName = self.path.split('/')[-1]
            self._sourceImageMatrix = np.array(image)
        else:
            self._sourceImageMatrix = None

        if self._sourceImageMatrix is not None:
            self._sourceHeight, self._sourceWidth, self._channels = self._sourceImageMatrix.shape

        self.destinationHeight = 0
        self.destinationWidth = 0

        self.imageIdent = True


    def getFileName(self):
        return self._fileName


    def setNeededSize(self, width, height):
        if (self._sourceWidth != width or self._sourceHeight != height) and (self._sourceWidth and self._sourceHeight):
            self.destinationWidth = width
            self.destinationHeight = height
            self.imageIdent = False


    def resize(self):
        if self.imageIdent:
            return

        scaleX = (self._sourceWidth - 1) / (self.destinationWidth - 1)
        scaleY = (self._sourceHeight - 1) / (self.destinationHeight - 1)

        self.destinationImageMatrix = np.empty((self.destinationHeight, self.destinationWidth, self._channels),
                                               dtype=self._sourceImageMatrix.dtype)

        for destinationY in range(self.destinationHeight):
            for destinationX in range(self.destinationWidth):
                sourceX = destinationX * scaleX
                sourceY = destinationY * scaleY

                sourceX_rounded = self.clamp(round(sourceX), 0, self._sourceWidth - 1)
                sourceY_rounded = self.clamp(round(sourceY), 0, self._sourceHeight - 1)

                self.destinationImageMatrix[destinationY, destinationX] = self._sourceImageMatrix[sourceY_rounded, sourceX_rounded]


    def saveImage(self):
        if self.imageIdent:
            return
        newImage = Image.fromarray(self.destinationImageMatrix)
        newImage.save(self.path)


    @staticmethod
    def clamp(value, minimum, maximum):
        return max(minimum, min(value, maximum))


