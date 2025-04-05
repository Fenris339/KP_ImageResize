from PyQt6 import QtCore
from Image import CImage


def main():
    testImage = CImage('C:/Users/fenri/PycharmProjects/KP_ImageResize/res/321.png')
    testImage.setNeededSize(300,300)
    testImage.resize()
    testImage.saveImage()
    testImage.testPrint()


if __name__ == '__main__':
    main()