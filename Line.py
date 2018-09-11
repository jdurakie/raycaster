class Line(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return(str(self.start) + ' -> ' + str(self.end))

    # V1
    # def vectorize(self):
    #     #returns direction vector from origin
    #     try:
    #         return mathhelp.subtractPoint(self.end, self.start)
    #     except IndexError:
    #         print("Invalid line!")
    #         print(self)
    #         exit()

    # V2
    def vectorize(self):
        #Duplicate code of mathhelp.subtractPoint, here to avoid excessive function calls
        lx, ly, lz = self.end
        rx, ry, rz = self.start
        return (lx - rx, ly - ry, lz - rz)