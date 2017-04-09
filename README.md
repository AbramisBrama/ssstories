SSStories
=========

A small project to post cool stories to VK community like [SSStories](https://vk.com/ssstories)


Requirements
============

1. Python 3
2. PIP Python package manager.
3. It is recommended to use [Virtual Environments](http://docs.python-guide.org/en/latest/dev/virtualenvs) for
proper requirements management.


    pip3 install pymorphy2
    
  Then go to the current project's folder to create and initialize the virtual environment: 


    virtualenv ssenv
    source ./ssenv/bin/activate


3. [Pymorphy 2](https://pymorphy2.readthedocs.io/en/latest/) libs:

    
    pip3 install pymorphy2
    pip3 install pymorphy2-dicts
    pip3 install DAWG-Python
    
4. [Sphinx documentation](http://www.sphinx-doc.org/) libs:


    pip3 install Sphinx


Description
===========

The application uses [opencorpora dictionaries](http://opencorpora.org/)
for words analysis and names parsing.

To generate the documentation run:

    ./make.bat html

and open the file _build/html/index.html


Usage
=====

To get a piece of text with substituted names run:

    python -m text

To run all test use the following command:

    python -m unittest discover test