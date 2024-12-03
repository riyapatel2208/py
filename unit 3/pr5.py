class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length


# Example usage:
shape = Shape()
print("Area of Shape:", shape.area())

sqr=int(input("Enter a number to find square:"))
square = Square(sqr)
print("Area of Square:", square.area())