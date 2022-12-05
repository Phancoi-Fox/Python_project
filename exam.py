from abc import ABCMeta, abstractclassmethod

while True:
    n = int(input())
    if 0 <= n <= 20:
        break

class Shape:
    __metaclass__ = ABCMeta
    def __init__(self, shapeType):
        self.shapeType = shapeType

    def area(self):
        pass
    def perimeter():
        pass

class Rectangle(Shape):
    def __init__(self, length, breadth):
        Shape.__init__(self, "Rectangle")
        self.__length = length
        self.breadth = breadth
    def getLength(self):
        return self.__length
    def area(self):
        return self.__length * self.breadth
    def perimeter(self):
        return 2 * (self.__length + self.breadth)
class Circle(Shape):
    pi = 3.14
    def __init__(self, radius):
        Shape.__init__(self, radius)
        self.radius = radius
    def area(self):
        return round(Circle.pi * (self. radius ** 2), 2)
    def perimeter(self):
        return round(2 * Circle.pi * self. radius, 2)

class Delta(Shape):
    def __init__(self, height, area1):
        Shape.__init__(self, "Delta")
        self.height = height
        self.area1 = area1
    def area(self):
        return round(self.height * self.area1 / 2)

class Delta1(Shape):
    def __init__(self, ra, rb, rc):
        Shape.__init__(self, "Delta1")
        self.ra = ra
        self.rb = rb
        self.rc = rc
    def perimeter(self):
        return self.ra + self.rb + self.rc
    
class Trape(Shape):
    def __init__(self, leng, small, large):
        Shape.__init__(self, "Trape")
        self.leng = leng
        self.small = small
        self.large = large
    def area(self):
        return self.leng + self.small + self.large

class Trape1(Shape):
    def __init__(self, rat, rbt, rct, rdt):
        Shape.__init__(self, "Trape1")
        self.rat = rat
        self.rbt = rbt
        self.rct = rct
        self.rdt = rdt
    def perimeter(self):
        return self.rat + self.rbt + self.rct + self.rdt

lst = []
lst_primeter = []
lst_circles = []
lst_delta = []
lst_trape = []
lst_rectangles = []
lst_print = []

for i in range(1, n + 1):
    display = input(str(i) + " ")
    if "Rectangle" in display:
        display1 = display.split()
        if len(display1) == 3:     
            lst_rectangles.append(display)
            rectangle = Rectangle(length = int(display1[-2]), breadth = int(display1[-1]))
            lst.append(rectangle.area())
            lst_primeter.append(rectangle.perimeter())
        else: break
    if "Circle" in display:
        display2 = display.split()
        if len(display2) == 2:
            lst_circles.append(display)
            circle = Circle(radius = int(display2[-1]))
            lst.append(circle.area())
            lst_primeter.append(circle.perimeter())
        else: break
        
    if "Delta" in display:
        display3 = display.split()
        if len(display3) == 3 or len(display3) == 4:
            lst_delta.append(display)
        else: break
        if len(display3) == 4:
            delta = Delta1(ra = int(display3[-3]), rb = int(display3[-2]), rc = int(display3[-1]))
            lst_primeter.append(delta.perimeter())
        if len(display3) == 3:
            delta1 = Delta(height = int(display3[-1]), area1 = int(display3[-2]))
            lst.append(delta1.area())
    if "Trape" in display:
        display4 = display.split()
        if len(display4) == 5 or len(display4) == 4:
            lst_trape.append(display)
        else: break
        if len(display4) == 5:
            trape = Trape1(rat = int(display4[-1]), rbt = int(display4[-2]), rct = int(display4[-3]), rdt = int(display4[-4]))
            lst_primeter.append(trape.perimeter())
        if len(display4) == 4:
            trape1 = Trape(leng = int(display4[-1]), small = int(display4[-2]), large = int(display4[-3]))
            lst.append(trape1.area())         
        
q = int(input())

for c in range(1, q + 1):
    cmd = input()
    cmd1 = cmd.split()
    if "display Area" in cmd:
        if int(cmd1[-1]) > n:
            break
        else:
            for k in range(len(lst) + 1):
                if k == int(cmd1[-1]):
                    lst_print.append(lst[k-1])
                else: continue
    elif "display Diameter" in cmd:
        if int(cmd1[-1]) > n:
            break
        else:
            for h in range(len(lst_primeter) + 1):
                if h == int(cmd1[-1]):
                    lst_print.append(lst_primeter[h-1])
                else: continue
    elif "listAll Circle" in cmd:
        for a in lst_circles:
            lst_print.append(a)
    elif "listAll Rectangle" in cmd:
        for b in lst_rectangles:
            lst_print.append(b)
    elif "listAll Delta" in cmd:
        for x in lst_delta:
            lst_print.append(x)
    elif "listAll Trape" in cmd:
        for y in lst_trape:
            lst_print.append(y)
for d in lst_print:
    print(d)                 
