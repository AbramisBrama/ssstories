# -*- coding: utf-8 -*-

import urllib.request
from html.parser import HTMLParser

"""
This is a simple utility to parse web 1.0 site and fill local texts base with new source texts for reichization.
"""

class NarodStoryParser(HTMLParser):

    """
    This class is inherited from standart HTMLParser class and used specifically for parsing texts from http://narodstory.net/ site.
    """
    def __init__(self, site_name, id, *args, **kwargs):
        """
        This is a constructor for NarodStoryParser objects
        :param site_name: type - string. Whole web-address with parameters.
        :param id: type - integer. Current story id.
        :param args:
        :param kwargs:
        :return:
        """
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
        super().__init__(*args, **kwargs)
        # при инициализации "скармливаем" парсеру содержимое страницы
        self.feed(self.read_site_content())
        # записываем результат в файл
        self.write_to_file()

    def handle_starttag(self, tag, attrs):
        """
        This is a function for start tag handling.
        :param tag: type - string. HTML tag type.
        :param attrs:
        :return:
        """
        #print("Encountered a start tag:", tag)
        if (tag=='p') and not (self.story_ended):
            self.data_ok = True
        else:
            self.data_ok = False

    def handle_data(self, data):
        """
        This is a function for text data handling.
        :param data: type - string. Text data within tags.
        :return:
        """
        if ('Смотрите также' in data) :
            self.story_ended = True
        if (self.data_ok) and not self.story_ended and not ('читать' in data) :
            self.text = self.text + data

    def read_site_content(self):
        """
        This function executes HTTP GET request and returns result page as a string
        :return: type - string. HTML page from specified in self.site_name address.
        """
        result=urllib.request.urlopen(self.site_name).read().decode("cp1251")
        return str(result)

    def write_to_file(self):
        """
        This function creates and fills a file within ../Data/texts directory
        :return:
        """
        # открываем файл
        f = open('..//Data//texts/new-story-'+str(self.id)+'.txt', 'w')
        # записываем текст в файл
        print('Creating new-story-'+str(self.id)+'.txt file')
        f.write(self.text)
        # закрываем файл
        f.close()


for page_id in list(range(30)):
    NarodStoryParser('http://narodstory.net/skazki-nosova.php?id='+str(page_id),page_id)
