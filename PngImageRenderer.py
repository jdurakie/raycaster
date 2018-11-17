"""
Contains code that draws the screen to a real image
"""

from PIL import Image
from PIL import ImageDraw

class ImageRenderer(object):
    def __init__(self, size):
        """
        size: (x, y)
        filename: string
        """
        self.image = Image.new('RGB', size, (0, 0, 0))

    def point(self, location, color=(255, 0, 0)):
        draw = ImageDraw.Draw(self.image)
        draw.point([location], fill=color)
        del draw

    def line(self, start, end, color=(255, 0, 0)):
        draw = ImageDraw.Draw(self.image)
        draw.line((start[0], start[1], end[0], end[1]), fill=color)
        del draw

    def saveImage(self, filename):
        self.image.save(filename, 'PNG')


