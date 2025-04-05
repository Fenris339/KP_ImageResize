import os

from PIL import Image
import numpy as np


class CImage:
    def __init__(self, path):
        self.path = path

        if self.path and os.path.exists(self.path):
            image = Image.open(path)
            self.sourceImageMatrix = np.array(image)
        else:
            self.sourceImageMatrix = None

        if self.sourceImageMatrix is not None:
            self.sourceHeight, self.sourceWidth, self.channels = self.sourceImageMatrix.shape

        self.destinationHeight = 0
        self.destinationWidth = 0

        self.imageIdent = True


    def setNeededSize(self, width, height):
        if (self.sourceWidth != width or self.sourceHeight != height) and (self.sourceWidth and self.sourceHeight):
            self.destinationWidth = width
            self.destinationHeight = height
            self.imageIdent = False


    def saveImage(self):
        if self.imageIdent:
            return
        newImage = Image.fromarray(self.destinationImageMatrix)
        newImage.save(self.path)


    def resize(self):
        if self.imageIdent:
            return

        scaleX = (self.sourceWidth - 1) / (self.destinationWidth - 1)
        scaleY = (self.sourceHeight - 1) / (self.destinationHeight - 1)

        self.destinationImageMatrix = np.empty((self.destinationHeight, self.destinationWidth, self.channels),
                                               dtype=self.sourceImageMatrix.dtype)

        for destinationY in range(self.destinationHeight):
            for destinationX in range(self.destinationWidth):
                sourceX = destinationX * scaleX
                sourceY = destinationY * scaleY

                sourceX_rounded = self.clamp(round(sourceX), 0, self.sourceWidth - 1)
                sourceY_rounded = self.clamp(round(sourceY), 0, self.sourceHeight - 1)

                self.destinationImageMatrix[destinationY, destinationX] = self.sourceImageMatrix[sourceY_rounded, sourceX_rounded]


    @staticmethod
    def clamp(value, minimum, maximum):
        return max(minimum, min(value, maximum))


    def testPrint(self):
        print(f"Высота: {self.sourceHeight}\nШирина: {self.sourceWidth}")
