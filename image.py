import PIL
imageType = []

class CImage:
    def __init__(self, path):
        self.path = path
        self.imageType = None
        self.sourceHeight = None
        self.sourceWidth = None
        self.neededHeight = None
        self.neededWidth = None

    def setSourceSize(self, width, height):
        self.neededWidth = width
        self.neededHeight = height

    def setNeededSize(self, width, height):
        self.neededWidth = width
        self.neededHeight = height

    def setImageType(self, imageType):
        self.imageType = imageType

    def saveImage(self):
        pass

    def resize(self):
        pass
