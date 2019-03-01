#
#
#   This problem implements the Two_points class from the Paper Exam
#
#
#
#   TODO: Read the supplied Point class to understand its function
#
#
#
###############################################################################
# NOTE: For ALL of the methods that you implement, the method is allowed
# to have additional side effects as needed by it and/or other methods.
###############################################################################
class Point(object):
    """Point in 2-D space"""
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def __repr__(self):
        return"Point({},{})".format(self.x, self.y)


    def funny_move(self,n):
        if n % 2 == 0:
            self.x = n
        else:
            self.x = self.x + n
        self.y = 2*self.y

class Two_points(object):
    def __init__(self,pt1,pt2):
        self.p1=pt1
        self.p2=pt2

    def swap_y(self):
        temp = self.p1.y
        self.p1.y = self.p2.y
        self.p2.y = temp

##############################################################################
def main():
    point1=Point(10,20)
    print(point1)
    point2 = Point(30,40)
    print(point2)
    point3 = Point(50,60)
    print(point3)
    point4 = Point(70,80)
    print(point4)
    tp1 = Two_points(point1,point3)
    tp2 = Two_points(point2,point4)
    print(tp1.p1)
    print(tp1.p2)
    tp1.swap_y()
    print(tp1.p1)
    print(tp1.p2)


main()
