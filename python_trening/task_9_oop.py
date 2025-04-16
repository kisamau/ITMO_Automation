class Button:
    def __init__(self, text, link):
        self.text = text
        self.link = link
# создание экземпляра класса
home = Button('welcome home','/home')
catalog_msk = Button('catalog','/msk/catalog')
# получение доступа к атрибутам
print(home.text)
print('кнопка ' + home.text + ' имеет ссылку ' + home.link)
print('\n')
print(catalog_msk.text)
print('кнопка ' + catalog_msk.text + ' имеет ссылку ' + catalog_msk.link)


class Button_Two:
    def __init__(self, text, link, loc):
        self.text = text
        self.link = link
        self.loc = loc
    def click(self):
        return 'клик по локатору - {}'.format(self.loc)
# создаем экземпляры класса
home_two = Button_Two('домой','/home','button#home')
# вызываем метод
print(home_two.click())