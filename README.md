SSStories
=========

A small project to post cool stories to VK community like [SSStories](https://vk.com/ssstories)


Requirements
============

1. Python 3
2. Pymorphy 2 libs:

    pip install pymorphy2
    pip install pymorphy2-dicts
    pip install DAWG-Python


Description
===========

The application uses [opencorpora dictionaries](http://opencorpora.org/)
for words analyse and names parsing.

To generate the documentation run:

    ./make.bat html

and open the file _build/html/index.html


Usage
=====

To get a piece of text with substituted names run:

    python -m text

To run all test use the following command:

    python -m unittest discover test