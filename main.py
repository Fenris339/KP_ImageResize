from PyQt6 import QtCore
from Image import CImage


def main():
    testImage = CImage('C:/Users/fenri/PycharmProjects/KP_ImageResize/res/321.png')
    testImage.setNeededSize(250,75)
    testImage.resize()
    testImage.saveImage()
    print(testImage.getFileName())


if __name__ == '__main__':
    main()