from abc import ABC, abstractmethod
import math #for π value

#Abstract Base Class
class Area(ABC):
    @abstractmethod
    def print_area(self):
        pass
        
    def calc_rectangle_area(self, length, breadth):
        pass 

    def calc_circle_area(self, radius):
        pass

    def calc_square_area(self, side):
        pass
# Inheritance 
class Rectangle(Area):   
  # overriding
    def calc_rectangle_area(self, length, breadth):
        self.length = length
        self.breadth = breadth
        self.result = self.length * self.breadth
        
    def print_area(self):
        print(f"Area of Rectangle: {self.result}")

class Circle(Area):
    def calc_circle_area(self, radius):
        self.radius = radius
        self.result = math.pi * (self.radius ** 2)

    def print_area(self):
        print(f"Area of Circle: {self.result:.2f}")
        
        
class Square(Area):
        def calc_square_area(self, side):
        	self.side = side
        	self.result = self.side ** 2
        	
        def print_area(self):
        	print(f"Area of Square: {self.result}")

#Object Creation
rect = Rectangle()
rect.calc_rectangle_area(10, 5)
rect.print_area()

circ = Circle()
circ.calc_circle_area(7)
circ.print_area()

sqr = Square()
sqr.calc_square_area(7)
sqr.print_area()
