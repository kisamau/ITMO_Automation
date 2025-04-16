class Rectangle:
    def __init__(self):
        self.width = 9
        self.height = 15
class Area(Rectangle):
    def __init__(self):
        super().__init__()
        self.ar = self.width * self.height
ar_rectangle = Area()
print('площадь прямоугольника: ',ar_rectangle.ar)
class Perimetr(Rectangle):
    def __init__(self):
        super().__init__()
        self.p = 2 * (self.width + self.height)
p_rectangle = Perimetr()
print('периметр прямоугольника: ',p_rectangle.p)

print('\n')

class Triangle:
    def __init__(self):
        self.a = 15
        self.b = 24
        self.c = 15
class Area(Triangle):
    def __init__(self):
        super().__init__()
        self.h1 = self.b / 2
        self.h2 = self.a ** 2 - self.h1 ** 2
        self.h = self.h2 ** (0.5)
        self.ar = 0.5 * self.b * self.h
ar_triangle = Area()
print('площадь равнобедренного треугольника: ',ar_triangle.ar)
class Perimetr(Triangle):
    def __init__(self):
        super().__init__()
        self.p = 2 * self.a + self.b
p_triangle = Perimetr()
print('периметр равнобедренного треугольника: ',p_triangle.p)

print('\n')

class Circle:
    def __init__(self):
        self.pi = 3.14
        self.r = 7
class Area(Circle):
    def __init__(self):
        super().__init__()
        self.ar = self.pi * (self.r ** 2)
ar_circle = Area()
print('площадь круга: ',ar_circle.ar)
class Perimetr(Circle):
    def __init__(self):
        super().__init__()
        self.p = 2 * self.pi * self.r
p_circle = Perimetr()
print('периметр круга: ',p_circle.p)

print('\n')

class Square:
    def __init__(self):
        self.width = 5
class Area(Square):
    def __init__(self):
        super().__init__()
        self.ar = self.width ** 2
ar_square = Area()
print('площадь квадрата: ', ar_square.ar)
class Perimetr(Square):
    def __init__(self):
        super().__init__()
        self.p = 4 * self.width
p_square = Perimetr()
print('периметр квадрата: ', p_square.p)

print('\n')
# задание 2
class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def addition(self):
        result = self.a + self.b
        print(f"Сложение: {self.a} + {self.b} = {result}")
    def multiplication(self):
        result = self.a * self.b
        print(f"Умножение: {self.a} * {self.b} = {result}")
    def division(self):
        if self.b != 0:
            result = self.a / self.b
            print(f"Деление: {self.a} / {self.b} = {result}")
        else:
            print("Ошибка: Деление на ноль!")
    def subtraction(self):
        result = self.a - self.b
        print(f"Вычитание: {self.a} - {self.b} = {result}")
math_operation = Math(7, 0)
math_operation.addition()
math_operation.subtraction()
math_operation.multiplication()
math_operation.division()

print('\n')
# задание 3
class Button:
    def __init__(self,text):
        self.text = text
        self.type = 'кнопка'
        self.loc = ''
    def click(self):
        return 'Клик по кнопке {}'.format(self.text)
text_box = Button('Text Box')
check_box = Button('Check Box')
radio_button = Button('Radio Button')
web_tables = Button('Web Tables')
buttons = Button('Buttons')
links = Button('Links')
br_links = Button('Broken Links - Images')
up_do = Button('Upload and Download')
dyn_prop = Button('Dynamic Properties')
print(text_box.text)
print(check_box.text)
print(radio_button.text)
print(web_tables.text)
print(buttons.text)
print(links.text)
print(br_links.text)
print(up_do.text)
print(dyn_prop.text)
print('---')
print(text_box.click())
print(check_box.click())
print(radio_button.click())
print(web_tables.click())
print(buttons.click())
print(links.click())
print(br_links.click())
print(up_do.click())
print(dyn_prop.click())