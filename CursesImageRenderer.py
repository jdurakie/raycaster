"""
Contains code that draws the screen to a Curses session
"""
import curses
import math
import colormanip

class ImageRenderer(object):
    def __init__(self, size):
        """
        size: (x, y)
        filename: string
        """
        self.screen = curses.initscr()
        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)
        avail, _ = curses.mousemask(1)
        self.screen.keypad(1)
        self.screen.nodelay(1)
        curses.start_color()
        self.screen.clear()

    def rgb_to_grayscale_char(self, color):
        average = (color[0] + color[1] + color[2]) / 3.0

        if average < 10:
            return ord(' ')
        elif average < 70:
            return ord('.')
        elif average < 140:
            return ord('o')
        elif average < 210:
            return ord('E')
        else:
            return ord('#')

    def rgb_to_grayscale_char_2(self, color):
        average = (color[0] + color[1] + color[2]) / 3.0
        shades = " .:-=+*#%@"
        #shades = ' .`^",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8\%B@$'
        grayscaleSegments = len(shades)
        segmentSize = 255 / grayscaleSegments
        shade = int(average // segmentSize)
        return shades[shade]

    def rgb_to_char(self, color):
        colorString = colormanip.getClosestColorName(color)
        closestColorChar = colorString[0]
        if closestColorChar == 'B':
            return ord(' ')
        else:
            return ord(closestColorChar)

    def point(self, location, color=(255, 0, 0)):
        char = self.rgb_to_grayscale_char_2(color)

        maxHeight, maxWidth = self.screen.getmaxyx()
        if location[0] > maxWidth or location[1] > maxHeight:
            return
        self.screen.addch(location[0], location[1], char)

    def saveImage(self, filename):
        self.screen.refresh()
