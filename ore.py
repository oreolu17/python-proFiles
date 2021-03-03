# import urllib.request
#
# fhand = urllib.request.urlopen('http://www.py4inf.com/code/romeo.txt')
# for line in fhand:
#     print(line.strip())
#
# import webbrowser
# url = input('Enter your url: ')
# webbrowser.open_new(url)

# import urllib.request
# from bs4 import BeautifulSoup
# wiki = 'http://www.facebook.com'
# page = urllib.request.urlopen(wiki)
# soup = BeautifulSoup(page, features='html.parser')
# # print(soup.prettify())
# # print(soup.body.prettify())
# print(soup.div.prettify())

import urllib.request
from PIL import Image
url = 'https://www.google.com/url?sa'
image = image .open(urllib.request.urlopen(url))
width, height = image.size
print (width, height)