# -*- coding: utf-8 -*-

import urllib.request
from html.parser import HTMLParser


class NarodStoryParser(HTMLParser):
    def __init__(self, site_name, id, *args, **kwargs):
        # фрагмент текста
        self.text = ''
        #индикатор, что текст нам нужен
        self.data_ok = False
        # имя сайта
        self.site_name = site_name
        #Номер страницы с историей
        self.id = id
        #Флаг последней строки в истории
        self.story_ended = False
        # вызываем __init__ родителя
        super().__init__(*args, **kwargs)
        # при инициализации "скармливаем" парсеру содержимое страницы
        self.feed(self.read_site_content())
        # записываем результат в файл
        self.write_to_file()

    def handle_starttag(self, tag, attrs):
        #print("Encountered a start tag:", tag)
        if (tag=='p') and not (self.story_ended):
            self.data_ok = True
        else:
            self.data_ok = False

    def handle_data(self, data):
        if ('Смотрите также' in data) :
            self.story_ended = True
        if (self.data_ok) and not self.story_ended and not ('читать' in data) :
            print(data)
            self.text = self.text + data

    def read_site_content(self):
        result=urllib.request.urlopen(self.site_name).read().decode("cp1251")
        return str(result)

    def write_to_file(self):
        # открываем файл
        f = open('..//Data//texts/new-story-'+str(self.id)+'.txt', 'w')
        # записываем текст в файл
        f.write(self.text)
        # закрываем файл
        f.close()


for page_id in list(range(5)):
    NarodStoryParser('http://narodstory.net/skazki-nosova.php?id='+str(page_id),page_id)
