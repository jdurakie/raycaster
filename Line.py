import mathhelp
class Line(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return(str(self.start) + ' -> ' + str(self.end))


    def vectorize(self):
        #returns direction vector from origin
        try:
            return mathhelp.subtractPoint(self.end, self.start)
        except IndexError:
            print("Invalid line!")
            print(self)
            exit()
