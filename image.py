import os

from PIL import Image
import numpy as np


class CImage:
    def __init__(self, path):
        self.path = path

        if self.path and os.path.exists(self.path) and Image.isImageType(self.path):
            image = Image.open(path)
            self.sourceImageMatrix = np.array(image)
        else:
            self.sourceImageMatrix = None

        if self.sourceImageMatrix is not None:
            self.sourceHeight, self.sourceWidth, self.test = self.sourceImageMatrix.shape
        else:
            self.sourceHeight, self.sourceWidth = None, None

        self.destinationHeight = None
        self.destinationWidth = None


    def setNeededSize(self, width, height):
        self.destinationWidth = width
        self.destinationHeight = height


    def saveImage(self):
        newImage = Image.fromarray(self.sourceImageMatrix)
        newImage.save(self.path)


    def resize(self):
        scaleX = (self.sourceWidth - 1) / (self.destinationWidth - 1)
        scaleY = (self.sourceHeight - 1) / (self.destinationHeight - 1)

        self.destinationImageMatrix = np.array()

        for dst_x in range(0, self.destinationWidth - 1):
            for dst_y in range(0, self.destinationHeight - 1):

                sourceX = dst_x * scaleX
                sourceY = dst_y * scaleY


                sourceX_rounded = self.clamp(round(sourceX), 0, self.sourceWidth - 1)
                sourceY_rounded = self.clamp(round(sourceY), 0, self.sourceHeight - 1)


                self.destinationImageMatrix[dst_x][dst_y] = self.sourceImageMatrix[sourceX_rounded][sourceY_rounded]


    @staticmethod
    def clamp(value, minimum, maximum):
        return max(minimum, min(value, maximum))


    def testPrint(self):
        print(f"Высота: {self.sourceHeight}\nШирина: {self.sourceWidth}")
