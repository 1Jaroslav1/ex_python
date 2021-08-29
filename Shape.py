from abc import ABC, abstractmethod
from math import pi, sqrt

def len_between_points(point_1, point_2):
    return sqrt((point_1[0] - point_2[0])**2 + (point_1[1] - point_2[1])**2)

class Shape(ABC):
    def __init__(self, Ftype):
        super().__init__()
        self._Ftype = Ftype

    def get_Ftype(self):
        return self._Ftype
    
    def set_Ftype(self, new_Ftype):
        self._Ftype = new_Ftype
    
    @abstractmethod
    def calcArea(self):
        pass

    @abstractmethod
    def calcPerimeter(self):
        pass
    
    @abstractmethod
    def checkCrossing(self, object):
        pass


class Circle(Shape):
    def __init__(self, center_x, center_y, radius):
        super().__init__("circle")
        self._center_x = center_x
        self._center_y = center_y
        self._radius = radius
    
    # Getters and setters
    def get_center_x(self):
        return self._center_x
    
    def set_center_x(self, new_center_x):
        self._center_x = new_center_x
    
    def get_center_y(self):
        return self._center_y
    
    def set_center_y(self, new_center_y):
        self._center_y = new_center_y

    def get_radius(self):
        return self._radius
    
    def set_radius(self, new_radius):
        self._radius = new_radius
    #=============================================

    def calcArea(self):
        return pi * (self._radius ** 2)

    def calcPerimeter(self):
        return 2 * pi * self._radius

    def checkCrossing(self, object):
        if object.get_Ftype() == "circle":
            length = len_between_points([object.get_center_x(), object.get_center_y()], [self._center_x, self._center_y])
            return length < (object.get_radius() + self._radius)
        elif object.get_Ftype() == "rectangle":
            d_points = object.get_diagonals_points()
            x1, y1 = d_points[0]
            x2, y2 = d_points[1]

            xn = max(x1, min(self._center_x, x2))
            yn = max(y1, min(self._center_y, y2))

            return len_between_points([xn, yn], [self._center_x, self._center_y]) < self._radius
        elif object.get_Ftype() == "triangle":
            pass


class Rectangle(Shape):
    def __init__(self, d_point1, d_point2):
        super().__init__("rectangle")
        self._d_point1 = d_point1
        self._d_point2 = d_point2

    def get_diagonals_points(self):
        return [self._d_point1, self._d_point2]
    
    def set_d_point1(self, new_d_point1):
        self._d_point1 = new_d_point1

    def set_d_point2(self, new_d_point2):
        self._d_point2 = new_d_point2

    def get_center(self):
        return [(self._d_point1[0] - self._d_point2[0])/2, (self._d_point1[1] - self._d_point2[1])/2]
    
    def get_width(self):
        return abs(self._d_point1[0] - self._d_point2[0])
    
    def get_height(self):
        return abs(self._d_point1[1] - self._d_point2[1])

    def calcArea(self):
        x = abs(self._d_point1[0] - self._d_point2[0])
        y = abs(self._d_point1[1] - self._d_point2[1])

        return x * y

    def calcPerimeter(self):
        x = abs(self._d_point1[0] - self._d_point2[0])
        y = abs(self._d_point1[1] - self._d_point2[1])

        return 2*(x + y)

    def checkCrossing(self, object):
        if object.get_Ftype() == "circle":
            x1, y1 = self._d_point1
            x2, y2 = self._d_point2

            xn = max(x1, min(object._center_x, x2))
            yn = max(y1, min(object._center_y, y2))

            return len_between_points([xn, yn], [object.get_center_x(), object.get_center_y()]) < object.get_radius()
        
        elif object.get_Ftype() == "rectangle":
            center1 = self.get_center()
            center2 = object.get_center()

            return abs(center1[0] - center2[0]) < object.get_width() + self.get_width() or abs(center1[1] - center2[1]) < object.get_height() + self.get_height()

        elif object.get_Ftype() == "triangle":
           pass

class Triangle(Shape):
    def __init__(self, point_1, point_2, point_3):
        super().__init__("triangle")
        self._point_1 = point_1
        self._point_2 = point_2
        self._point_3 = point_3

    # Getters and setters
    def get_point1(self):
        return self._point_1
    
    def get_point2(self):
        return self._point_2
    
    def get_point3(self):
        return self._point_3
    
    def set_point1(self, new_point_1):
        self._point_1 = new_point_1
    
    def set_point2(self, new_point_2):
        self._point_2 = new_point_2
    
    def set_point3(self, new_point_3):
        self._point_3 = new_point_3

    def get_side(self):
        return self._side
    
    def set_side(self, new_side):
        self._side = new_side
    #===============================================

    def calcArea(self):
        return abs((self._point_1[0] * (self._point_2[1] - self._point_3[1]) + self._point_2[0] * (self._point_3[1] - self._point_1[1]) + self._point_3[0] * (self._point_1[1] - self._point_2[1]))/2)
    
    def calcPerimeter(self):
        return len_between_points(self._point_1, self._point_2) + len_between_points(self._point_1, self._point_3) + len_between_points(self._point_3, self._point_2)
    
    def checkCrossing(self, object):
        if object.get_Ftype() == "circle":
            pass

        elif object.get_Ftype() == "rectangle":
            pass

        elif object.get_Ftype() == "triangle":
            pass

