#variables; variables are basically assigned to valeus e.g:
# one = 1
# two = 2
# three = 3

# print(one)
# print(two)
# print(three)

# decimal = 1.1
# print(decimal)
# two = 22
# print(two)
# stringVar = 'Hello'
# print(stringVar)
#
# one, two, three = 1, 2, 3
# print(one)
# print(two)
# print(three)
#
# #count values
# count = 0
# print(count)
# count = count + 1
# print(count)
# count += 1
# print(count)
# count = count * 3
# print(count)
# count /=3
# print(count)
#
# foo = 3
# foo /= 3
# print(foo)

# foo = "bar"
# foo +=3
# print(foo)

#Functions
# def FunctionName(Input):
#     Action
#     return output

# def addOne(Number):
#     Number = Number + 1
#     return Number

# def addOne(Number):
#     Output = Number + 1
#     return Output
#
# Var = 0
# print(Var)
# Var2 = addOne(Var)
# print(Var2)
# Var3 = addOne(Var2)
# print(Var3)
# Var4 = addOne(2.4 +3.6)
# print (Var4)

# def addOneaddTwo(NumberOne, NumberTwo):
#     output = NumberOne + 1
#     # output = output + NumberTwo + 2
#     output += NumberTwo + 2
#     return output
# sum = addOneaddTwo(1,2)
# print(sum)
#
# def addOne(number):
#     number += 1
#     return number
# one = addOne(0)
# two = addOne(one)
# print(two)
#
# def hello():
#     print('I am a beginner')
#     hello()
#     hello()

# def sumA(count):
#     array = count + 1
#     return array
# print(array)

# def printmessage(message, ntimes = 1):
#     print(message * ntimes)
#     printmessage("Hello")
#     printmessage("Hello",5)
#     print(printmessage)

# num = 1
# def func():
#     num = 4
#     print(num)
# func()
# print(num)


# If Statement

# if Condition:
#     Action

# click = False
#
# like = 0
#
# if click == True:
#     like = like + 1
#     click = False
#
#
# print(like)
#
# Temperature = 14
# Thermo = 15
# print(Thermo)
# if Temperature < 15:
#     Thermo = Thermo + 5
#
# print(Thermo)
#
#
# Temperature = 15
# Thermo = 15
# print(Thermo)
# if Temperature <= 15:
#     Thermo = Thermo + 5
#
# # print(Thermo)
#
# if Temperature >- 20:
#     Therm = Thermo - 3
#
# print(Thermo)

# Time = 'Day'
# Sleepy = False
# Pajamas = 'Off'
# if Time == 'Night' and Sleepy == True:
#     Pajamas = "On"
#
# print(Pajamas)
#
#
# Time = 'Night'
# Sleepy = True
# Pajamas = 'Off'
#     Pajamas = "On"
# print(Pajamas)
#
#
# Time = 'Night'
# Sleepy = False
# Pajamas = 'Off'
# if Time == 'Night' or Sleepy == True:
#     Pajamas = "On"
#
# print(Pajamas)


'''ELIF'''

# Time = 'Morning'
# Sleepy = True
# Pajamas = 'Off'
# InBed = True
#
# if Time == 'Night':
#     Pajamas = "On"
#
# elif Time == 'Morning':
#     Pajamas = 'On'
#
# else:
#     pajamas = 'Off'
#
#
# print(Pajamas)

#'''ELIF'''

#
# Time = 'Day'
# Sleepy = False
# Pajamas = 'Unknown'
# InBed = True
#
# print(Pajamas)
#
# if Time == 'Night':
#     Pajamas = "On"
#
# elif Time == 'Morning':
#     Pajamas = 'On'
#
# else:
#     Pajamas = 'Off'
#
# print(Pajamas)

#
# Grade = 70
# School = 'Degree'
# Admission = "Unknown"
# Chance = True
#
# if Grade >= 70 and School == 'Degree':
#     Admission = "Accepted"
#
# elif Grade < 60 >= 50 and School == 'Degree':
#     Admission = "Probation"
#
# elif Grade <50 and School == 'Degree':
#     Admission = 'Unaccepted'
#
# else:
#     Admission = 'Not Applicable'
#
# print(Admission)


#LISTS
# TestList = ['elelment1', "elemebt2", 'element3']
# TestList = [0.1,2,]

# Scores = [70, 85, 67.5, 90, 80]
# print(Scores)
# print(Scores[0])
# print(Scores[1])
# print(Scores[2])
# print(Scores[3])
# print(Scores[4])
#
# print(Scores[-1])
# print(Scores[-2])
# print(Scores[-3])
# print(Scores[-4])
# print(Scores[-5])
#
# print(Scores[0:2])
# print(Scores[0:3])
# print(Scores[1:3])
# print(Scores[1:])

#Adjusting the list
# Scores[0]= 75
# print(Scores)
# Scores[4]= 'Hello'
# print(Scores)

# Scores[1:3]= []
# print(Scores)

# Scores[2:3]= []
# print(Scores)

# Scores[2]= []
# print(Scores)
#
# Scores[2]= ['Hello', 'World']
# print(Scores)
# print(Scores[2])
# print(Scores[2][0])
#
# Scores.append(82)
# print(Scores)

# li = [['a','b']]
# print(li[-1][-1])
#
# myUniqueList = []
# myUniqueList.append(60)
# myUniqueList.append(70)
# myUniqueList.append(80)
# myUniqueList.append(90)
# myUniqueList.append(100)
# print(myUniqueList)
#
# # ul = list()
#
# # def AddToList():
# def AddToList(item):
#     flag = False
#     for i in myUniqueList:
#         if i == item:
#             flag = True#Item already exists
#     if(flag == False):
#         myUniqueList.append(item)
#
# AddToList(70)
# AddToList(40)
# AddToList(30)
#
# print(myUniqueList)
#
# #loops loops
# #for loops
# #part 1
# word = "Hello"
# for w in word:
#     print(w)
#
# #part 2
# word = "Hello"
# for w in word:
#     print(w)
#     if w == "e":
#         print('what a funny letter')
#
# #part 3
# word = "Hello"
#
# letters = []
#
# for w in word:
#     print(w)
#     if w == "e":
#         print('what a funny letter')
#     letters.append(w)
# print(letters)
#
# #part 4
# word = "Hello"
#
# letters = []
#
# for w in word:
#     print(w)
#     if w == "e":
#         print('what a funny letter')
#     letters.append(w)
# print(letters)
#
# for l in letters:
#     print(l)
#
# # part 5
# word = "Hello"
#
# letters = []
#
# Numbers =[1,2,3,4,5]
#
# for l in Numbers:
#     print(l)
#
# modulus % explanation
# 1%2 = 1
# 2%2 = 0
# modulus is simply the remainder u get after u divide 2 numbers

# #part 6
# Numbers =[1,2,3,4,5]
# for l in Numbers:
#     if l%2 == 1:
#         print(l)
#
# #part 7
# for num in range(10):
#     print(num)
#
# #part 8
# Numbers = []
#
# for num in range(10):
#     Numbers.append(num)
#     print(num)
#
# print(Numbers)
#
# #part 9
#
# Numbers = []
# #To get odd numbers
# for num in range(1, 10, 2):
#     Numbers.append(num)
#     print(num)
#
# print(Numbers)


#while loops
# while (condition):
#     Action
#     Action2
#     Acttion3
#
# #part 1
# counter = 1
# while (counter <=10):
#     print(counter)
#     counter = counter + 1
#
# #part 2
# counter = 1
# Sum = 0
# while (counter <=1o):
#     print(counter)
#     Sum = Sum + counter
#     counter = counter + 1
#
# print(Sum)
#
#
# #part 3
# Letters =["a", "b", "c", "d", "e"]
# Index = 0
# while (Index < len(Letters)):
#     print(Index)
#     print(Letters[Index])
#     Index = Index + 1
#
# #part 4
# height = 5000
# velocity = 50
# time = 0
#
# while (height > 0):
#     height = height - velocity
#     time = time + 1
#
# print(height)
# print(time)


#Breaking and continuing loops

# #part 1
# participants = ["Jen", "Alex", "Tina", "Joe", "Ben"]
# position = 1
# for name in participants:
#     if name == "Tina":
#         break
#     position = position + 1
#
# print(position)
#
# #more understanding
# participants = ["Jen", "Alex", "Tina", "Joe", "Ben"]
# position = 1
# for name in participants:
#     if name == "Tina":
#         print("About to break")
#         break
#     print("About to increment")
#     position = position + 1
#
# print(position)

#part 3
#
# participants = ["Jen", "Alex", "Tina", "Joe", "Ben"]
# position = 1
#
# Index = 0
# for CurrentIndex in range(len(participants)):
#     if participants[CurrentIndex] == "Joe":
#         break
# print(CurrentIndex)
#
# # continue statement
# for number in range(10):
#     if number%3 == 0:
#         print(number)
#         print("Divisible by 3")
#         continue
#     print(number)
#     print("Not divisible by 3")


#
# for numbers in range(101):
#     if  numbers%3==0 and numbers%5 == 0:
#         print("FizzBuzz")
#     elif numbers%3 ==0:
#         print("Fizz")
#     elif numbers%5 == 0:
#         print('Buzz')
#     else:
#         print(numbers)


#Making Shapes with Loops
#
# #Triangle
# Length = 10
#
# for pos in range(1,Length + 1):
#     print("c"*pos)
#
# #part 2
# Length = 10
# ToPrint = "a"
# for pos in range(1,Length + 1):
#     print(ToPrint*pos)

#part 3
#
# for pos in range(Length,0,-1):
#     print(ToPrint*pos)

# For a better Triangle
# for pos in range(Length -1,0,-1):
#     print(ToPrint*pos)


#Nested LOops

#tictac toe
#
# for row in range(5):
#     if row%2==0:
#         print(" | | ")
#     else:
#         print("-----")
#
#
# #part 2
# for row in range(5):
#     if row%2==0:
#         for column in range(1,6):
#             if column%2==1:
#                 print(" ",end=" ")
#             else:
#                 print("|",end=" ")
#         # print(" | | ")
#     else:
#         print("-----")

# #prt 3
# for row in range(5):
#     if row%2==0:
#         for column in range(1,6):
#             if column%2==1:
#                 if column !=5:
#                     print(" ",end="")
#                 else:
#                     print(" ")
#             else:
#                 print("|",end="")
#         # print(" | | ")
#     else:
#         print("-----")

x = 2
for i in range(x):
    for j in range(x):
        a = x -j + i
        print(a)


f = 1
A = [[1, 2, 3], [2, 3, 4], [3, 4,5]]
for i in range(0, 3):
    f = f*i
    for j in range(0,3):
        A[i][j] = f
print(A)







