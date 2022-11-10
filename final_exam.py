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
lst = []
lst_primeter = []
lst_circles = []
lst_rectangles = []
lst_print = []

for i in range(1, n + 1):
    display = input(str(i) + " ")
    if "Rectangle" in display: 
        lst_rectangles.append(display)
        display1 = display.split()
        rectangle = Rectangle(length = int(display1[-2]), breadth = int(display1[-1]))
        lst.append(rectangle.area())
        lst_primeter.append(rectangle.perimeter())
        
    if "Circle" in display:
        lst_circles.append(display)
        display2 = display.split()
        circle = Circle(radius = int(display2[-1]))
        lst.append(circle.area())
        lst_primeter.append(circle.perimeter())
        
        
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
for d in lst_print:
    print(d)                 
