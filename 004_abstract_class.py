from abc import ABC, abstractmethod

# Define an abstract class
class Shape(ABC):  # Subclass ABC (Abstract Base Class)
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Create a concrete subclass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159265359 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14159265359 * self.radius

# Create a concrete subclass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Attempting to create an instance of the abstract class Shape will result in an error.
# shape = Shape()  # This will raise a TypeError: Can't instantiate abstract class Shape with abstract methods area, perimeter

# Create instances of concrete subclasses
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Calculate and print area and perimeter
print(f"Circle Area: {circle.area()}")
print(f"Circle Perimeter: {circle.perimeter()}")
print(f"Rectangle Area: {rectangle.area()}")
print(f"Rectangle Perimeter: {rectangle.perimeter()}")


# In Python, you can create an abstract class using the abc module. An abstract class is a class that cannot be instantiated and is meant to be subclassed. It may contain abstract methods, which are methods that have no implementation in the abstract class and must be implemented in any concrete subclass. 