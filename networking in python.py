import re
# statement = 'Hello from jack@niit.com to nancy@niit.com concerning the meeting @ 4pm'
# emails = re.findall('\S+@\S+', statement)
# print(emails)

# statement = 'The break 2 statement 3 is used 4 to exit 3 the loop'
# strings = re.findall('e', statement)
# print(strings)

# txt = "The rain in Spain falls mainly in the plain!"

#Check if the string contains "ai" followed by 0 or more "x" characters:

# x = re.findall("ait*", txt)
#
# print(x)
#
# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")

# import re
# 	hand = open("mbox.txt")
# 	search = raw_input("Enter a regular expression: ")
# 	count = 0
# 	for line in hand:
#     		line = line.rstrip()
# 		if re.search(search,line) :
#         			count = count + 1
#  
# 	print("mbox.txt had "+str(count)+" lines that matched "+search)

#
# #Assignment
# import re
# hand = open('C:/name.txt')
# search = input('Enter a regular expression: ')
# count = 0
# for line in hand:
#     try:
#         line = line.rstrip()
#         if re.search(search,line):
#             count = count + 1
#     except:
#         print('You gave an invalid information')
#
# print('note.txt had' ' '+str(count)+' ' 'lines that matched' ' '+search )






# regex ='python'
# count = 0
# try:
#     fhand = open('C:/name.txt')
#     for line in fhand:
#         m = re.findall('python', fhand)
#         count = count + 1
# except:
#     'error try again'
# print('name.txt had' " " +str(count) + " "'lines that matched ')


#NETWORKING
import socket

# import urllib.request
#
# fhand = urllib.request.urlopen('http://www.py4inf.com/code/romeo.txt')
# for line in fhand:
#     print(line.strip())


# import urllib.request
# from bs4 import BeautifulSoup
# wiki = 'http://www.facebook.com'
# page = urllib.request.urlopen(wiki)
# soup = BeautifulSoup(page, features='html.parser')
# # print(soup.prettify())
# # print(soup.body.prettify())
# print(soup.div.prettify())


# from bs4 import BeautifulSoup
# import urllib.request
# greg = urllib.request.urlopen('http://www.https://')
# print (greg)
#
#
# soup = BeautifulSoup
import urllib.request
from bs4 import BeautifulSoup
import requests

greg = requests.get('https://www.tutorialspoint.com/index.html')
soup = BeautifulSoup(greg.content, features='html.parser' )

for h in soup.select('html'):
    print(h)

print (soup.title.text)

