# simple if condiion
#
# course = input ("Enter Your Course: ")
# if course == "python":
#     print (" Please go to online 7, Its your class Time!")

# if else condition
#
# age = int(input("Enter your age: "))
# if age >=18:
#     print("Adult... You are legible to Vote!")
# else:
#     print("Too young to vote!")

# chained condition

# score = int(input("Enter the sore: "))
# if score >= 80:
#     print("Grade A")
# elif score >= 70:
#     print("Grade B")
# elif score >= 50:
#     print("Grade C")
# elif score >= 40:
#     print("Grade D")
# elif score <= 30:
#     print("Grade E")
# else:
#     print("Invalid number")

# nested conditionl execution

# amount = int(input("Enter the total amount of goods bought: "))
# if amount >= 5000:
#     day = input("Enter the current day of the week: ")
#     if day == 'monday':
#         print ("Congratulations!!!.....you have 10% discount on your purchase ")
#     else:
#         print("oops.. no discount today!")
# else:
#     print("Thanks for your patronge")

# timeC = input("Enter time in 24Hs Format (e.g. 13): " )
# time = float(timeC)
# if (time>=0 and time <=12):
#     print("Good Morning")
# elif (time>=13 and <=16):
#     print("Good Afternoon")
# elif (time>=17 and <=20):
#     print("Good Evening")
# elif (time>=21 and <=24):
#     print("Good Night")
# else:
#     print("Invalid Time")
#     print("Wrong Input")
#
# time = float(input (' Enter time in 24 hours format: '))
# ('Good Morning')
# elif ( time>=12 and time<=16):
#     print ('Good Afternoon')
# elif ( time>16 and time<=24):
#     print ('Good Night')
# else:
#     print ('Invalid Time')
#     print ('Good-bye')
# if (time>=0 and time<12):
#     print

# Functions


# def add():
#     x=2+3
#     print(x)
#
# add()
#
# def add():
#     x = int(input("Enter First Number "))
#     y = int(input("Enter second number "))
#     z = x + y
#     print(z)
#
# add()
#
# def add(x, y):
#     z = x + y
#     print(z)
#
# add(12, 13)

# def add(x=12, y=13):
#     z = x + y
#     print(z)
#
# add()
# add(20)
# add(23, 12)


# while statement
# var = 10
# while var > 7:
#     print(var)
#     var = var - 1
#     print("Here, learnimg never stops")

# n = 2
# while n <= 10:
#     if n % 2 == 0:
#         print(n)
#     n = n + 1


# while True:
#     line = input("Enter Name: ")
#     if line == "Done":
#         break
#         print("Done!")
#     print(line)

# x = 1
# while x > 0:
#     if x == 20:
#         break
#     print(x)
#     x = x + 1

# while True:
#     line = input(">")
#     if line(0) == "#":
#         continue
#     if line == "Done!":
#         break
#     print(line)
# print("Done!")

# using for loop
# friends = ["Joseph", "Ore", "Seyi"]
# for friend in friends:
#     print("Good morning", friend)
# print ('Done!')

# total = 0
# for value in [3, 41, 21, 30, 50]:
#     total = total + value
# print("Total = ", total)

# smallest = None
# for value in [41,12, 74, 9, 15, 3]:
#     if smallest is None or value < smallest:
#         smallest = value
# print('smallest', smallest)
#
# largest = None
# for value in [3, 41, 12, 9, 74, 15 ]:
#     if largest is None or value > largest:
#         largest = value
# print ('largest', largest)

# try and except

# count = 0
# total = 0
# while True:
#     num = input("Enter a number ")
#     if num == 'Done':
#         break
#     try:
#         value = float(num)
#     except:
#         print("Bad Input")
#         continue
#     total = total + value
#     count = count + 1
#
# average = total/count
# print(total)
# print(count)

# concatenation
# a = "Hello"
# b = "python"
# print (a  + b)

# multiple string
# greetings = "Hello Nelson"
# part = greetings[0]
# print(part)
# print(greetings[6:12])
#
# print('s' in greetings)
# print('k' in greetings)
#
# print('k' not in greetings)
# print('s' not in greetings)



# total = 0
# count = 0
# while (True):
#     fig = input("Enter a number: ")
#     if fig == "0":
#         break
#     try:
#         value = float(fig)
#     except:
#         print("casting error")
#         continue
#     total = total + value
#     count = count + 1
# average = total/count
# print (total)
# print(count)
# print(str(average))




































































































