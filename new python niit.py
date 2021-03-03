#string
# name = 'python'
# print(name[1])
#
# name1= 'python '
# name2 = 'is good'
# print(name1 + name2)
#
# name1 = 'python'
# var2 = 2
# print(name1 + str(var2))

# name = 'python'
# counter = 5
# print(len(name))
# while counter < len(name):
#     print(name[counter])
#     counter = counter + 1

# name = "python"
# print(name.upper())
# print(name.title())
# print(name.capitalize())

# un = 'user'
# input("Enter a password: ")
# if un == "user":
#     print('welcome')
# else:
#     print('password not correct')

#%%%%%%%%
# num = 5
# print('number %d is the value'%num)

# num = 5
# print('number %d is the value'%num)


# import string
# print (string.punctuation)
# line= input ('Enter a statement with punctuations: ')
# line= line.translate(string.punctuation)
# line = line.lower()
# words = line.split()
# print(words)

#file opening
# guest = input("what file do you want to open: ")
# file = open("C:/" + guest +".txt")
# read = file.read()
# print(read)

#creating a new file

# file = open("C:/name.txt", "a")
# line = "music is the coolest"
# file.write(line)
# print(file)
#
# # try and except
# try:
#     file = open("C:/name.txt", "a")
#     line = "music is the coolest"
#     file.write(line)
#     print(file)
# except:
#     print("Error: The file could not be found")

# LIST
# []
# TRANSVERSING LIST
# numbers = [10, 20, 30, 40]
# for r in range[len[numbers]]:
#     numbers[r] = numbers[i]*2
#     print(numbers[r])

# mylist = [30, 90, 50, 70]
# mylist.sort()
# print(mylist)
#
# mylist = ["a", "c", "f", "b"]
# mylist.sort()
# print(mylist)

# mylist = [30, 90, 50, 70]
# mylist.sort(reverse = True)
# print(mylist)

# str =
#DICTIONARY
# eng2sp = dict()
# print(eng2sp)


# dic = {'one': 1, 'two': 2, 'three': 3, 'four': 4 }
# dic.pop('two')
# del dic['three']
# print(dic)
# print(dic.keys())
# print(dic.values())
# print(dic.items())
# print(len(dic))
# print('one' in dic)
# print(2 in dic)
# mydic = dic.values()
# print(2 in dic)
# mydic = dic.keys()
# print('four' in dic)
# for key in dic:
#     print(key,dic[key])
# for key in dic:
#     print(dic.get(key))
# for value in dic:
#     print(dic.get(value))
#
#
# mydict = dict()
# mydict['one'] = 21
# mydict['two'] = 22
# print(mydict)

# mylist = ['x', 'y', 'z']
# mydict = dict.fromkeys(mylist)
# print(mydict)
#
# mylist = ['x', 'y', 'z']
# mydict = dict.fromkeys(mylist, 3)
# print(mydict)

#ASSIGNMENT
# states = {'Oregon':'OR', 'Florida':'FL', 'Califonia':'CA', 'New York':'NY', 'Michigan':'MI'}
# cities = {'CA': 'San Fransicso', 'MI': 'Detroit', 'FL': 'Jacksonville'}
# cities['NY'] = 'New York'
# cities['OR'] = 'Portland'
# print(states)
# print(cities)
# print(cities.keys())
# print(cities.values())


# TUPLES
# tup1= ('physics', 'chemistry', 20, 30);
# tup2 = (50, 60, 80);
# print(tup1[0])
# print (tup2)

# tuples = (1, 2, 3, 4, 5)

#access the elements
# ele = tuples[0]
# print(ele)

#delete the elements
# del tuples[3]
# print(ele)
# TUPLES CAN NOT BE DELETED EXCEPT YOU DELETE TEHE WHOLE THING
# del tuples
# print (tuples)

# try:
#     del tuples[0]
# except:
#     print('Tuple has been deleted')
#
# print(tuples)


#
# str1 = ('Ore', 'Akin', 'Seyi', 'Tomiwa', 'Jide')
# str2 = (10, 20, 30, 40, 50)
# print(max(str2))
# print(min(str2))
# print(str1[2:4])
# print(str2[2:4])

# fhand = open("c:/name.txt")
# print(fhand)

#JSON JSON JSON
#
# import json
# input = ''' [ {
# "id" : "001",
# "x" : "2",
# "name" : "Chuck"
# } ,
# {
# "id" : "009",
# "x" : "7",
# "name" : "Bill"
# } ]'''
# info = json.loads(input)
# print ('Usercount:',len(info))
# # for item in info:
# print ('Name:', ['name'])
# print ('Id:',['id'])
# print ('Attribute:',['x'])
#
# import urllib
# import json
# service_url = 'http://maps.googleapis.com/maps/api/geocode/json?'
# while True:
#
#     address = input('Enter location: ')
#     if len(address) < 1 :
#         break
# url = service_url + urllib.urlencode({'sensor':'false', 'address':address})
# print ('Retrieving',url)
# uh = urllib.urlopen(url)
# data = uh.read()
# print ('Retrieved',len(data),'characters')
# try:
#     js = json.loads(str(data))
# 	except:
#         js = None
# 	    if 'status' not in js or js['status'] != 'OK':
# 		print ('====FailureToRetrieve====')
# 	    print (data)
#         continue
# print (json.dumps(js, indent=4))
# lat = js["results"][0]["geometry"]["location"]["lat"]
# lng = js["results"][0]["geometry"]["location"]["lng"]
# print ('lat',lat,'lng',lng)
# location = js['results'][0]['formatted_address']
# print (location)

#SQLITE
import sqlite3
DatabaseName = 'text.db'
conn = sqlite3.connect(DatabaseName)
SQL = 'CREATE TABLE IF NOT EXISTS students(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER)'
conn.execute(SQL)

SQL = "INSERT INTO students(name, age) VALUES('Ore', 12)"
conn.execute(SQL)

SQL = "SELECT * FROM students"
var = conn.execute(SQL)

print(var.fetchall())
SQL = 'Delete from student where Id = 1'

print (var.fetchall())
