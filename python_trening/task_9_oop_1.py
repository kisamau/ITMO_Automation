class Input:
    def __init__(self, loc, text):
        self.loc = loc
        self.text = text
search = Input('input#search','поиск')
print(search.loc,search.text)

class Button:
    def __init__(self, loc, text):
        self.loc = loc
        self.text = text
registration = Button('button#registration','регистрация')
print(registration.loc,registration.text)

class Title:
    def __init__(self, loc, text):
        self.loc = loc
        self.text = text
header = Title('title#header','зоомагазин')
print(header.loc,header.text)

class Link:
    def __init__(self, loc, text):
        self.loc = loc
        self.text = text
address = Link('link#address','/home/zoo_world')
print(address.loc,address.text)