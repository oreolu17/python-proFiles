# def chop(t):
#     t.pop(0)
#     t.pop()
# def middle(t):
#     del t[1: -1]
#     return t
#
# t = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# chop (t)
# print(t)
#
# t= [1, 2, 3, 4, 5, 6, 7, 8, 9]
# t1 = middle(t)
# print(t1)



#
# import math
# #fractional number
# n = 100.7 #
#
# print (math.floor(n))
# print (math.ceil(n))

# calculator
# Program make a simple calculator
#
# This function adds two numbers
# def add(x, y):
#     return x + y
#
# # This function subtracts two numbers
# def subtract(x, y):
#     return x - y
#
# # This function multiplies two numbers
# def multiply(x, y):
#     return x * y
#
# # This function divides two numbers
# def divide(x, y):
#     return x / y
#
#
# print("Select operation.")
# print("1.Add")
# print("2.Subtract")
# print("3.Multiply")
# print("4.Divide")
#
# while True:
#     # Take input from the user
#     choice = input("Enter choice(1/2/3/4): ")
#
#     # Check if choice is one of the four options
#     if choice in ('1', '2', '3', '4'):
#         num1 = float(input("Enter first number: "))
#         num2 = float(input("Enter second number: "))
#
#         if choice == '1':
#             print(num1, "+", num2, "=", add(num1, num2))
#
#         elif choice == '2':
#             print(num1, "-", num2, "=", subtract(num1, num2))
#
#         elif choice == '3':
#             print(num1, "*", num2, "=", multiply(num1, num2))
#
#         elif choice == '4':
#             print(num1, "/", num2, "=", divide(num1, num2))
#         break
#     else:
#         print("Invalid Input")


# a = 'b'
# if True or True:
#     a = 'a'
#     print(a*2)
#
# word = "hello"
# Letters =[]
# for w in word:
#     Letters.append(w)
# print(Letters)
#
# i = 1
# while True:
#     if i%3 == 0:
#         break
#     print(i)
#     i+=1
#
# for i in range(2):
#     print(i)

# counter = 1
# while (counter<=10):
#     print(counter)
#     counter = counter + 1

X = "abcd"
for i in range(len(X)):
    print(i)