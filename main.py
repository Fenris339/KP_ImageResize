from PyQt6 import QtCore
from image import CImage

def getImages():
    pass


def main():
    testImage = CImage('./res/icon.ico')
    testImage.testPrint()


if __name__ == '__main__':
    main()