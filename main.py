from math import pi

class Color:

    def __init__(self, R, G, B):
        self.__color = R+G+B

    def __repr__(self):
        return self.__color

class Rectangle:

    def __init__(self, color=1, x=1, y=1,):
        self.__height = y
        self.__width = x
        self.__color = color
        self.__area = x*y

    def get_data(self):
        return [self.__height, self.__width, self.__color, self.__area]

    def __repr__(self):
        return "\
\n\
Прямоугольник:\n\
Длина: {}\n\
Ширина: {}\n\
Цвет: {}\n\
Площадь: {}\n\
".format(self.__width, self.__height, self.__color, self.__area)

class Circle:

    def __init__(self, R, color):
        self.__radius = R
        self.__color = color
        self.__area = pi * R * R

    def __repr__(self):
        return "\
\n\
Круг:\n\
Радиус: {}\n\
Цвет: {}\n\
Площадь: {}\n\
".format(self.__radius, self.__color, self.__area)

class Square(Rectangle):

    def __repr__(self):
        data = super().get_data()
        self.__width = data[1]
        self.__color = data[2]
        self.__area = self.__width ** 2
        return "\
Квадрат:\n\
Сторона: {}\n\
Цвет: {}\n\
Площадь: {}\n\
".format(self.__width, self.__color, self.__area)

def main():
    rectangle = Rectangle(Color("11","22","31"), 10, 20)
    print(rectangle)
    circle = Circle(8, Color("12","34","96"))
    print(circle)
    square = Square(Color("25", "67", "58"), 10)
    print(square)

if __name__ == '__main__':
    main()