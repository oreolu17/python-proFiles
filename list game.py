flag = True
list = [ 10,20,30,40,50]

def menu():
    print("Enter 1: to insert \n Enter 2: to remove \n Enter 3: to sort \n Enter 4: to extend \n Enter 5 to reverse \n Enter 6: to transverse")
def insertlist(item):
    list.append(item)
def remove(item):
    list.remove(item)
def sort(item):
    list.sort()
def extend(item):
    list.extend()
def reverse(item):
    list.reverse()
def playgame():
    flag = True
    while (flag):
        menu()
        choice = input()
        choice = int(choice)
        if choice == 1:
            item = input ('Enter the item you want to add to the list')
            insertlist(item)
        elif choice == 2:
            item = input ('Enter the item you want to remove')
            remove(item)
        elif choice  == 3:
            item = input('Enter an item you want to sort')
            sort(item)
        elif choice == 4:
            item = input('Enter an item you want to extend')
            extend(item)
        elif choice == 5:
            item = input('Enter an item you want to reverse')
            reverse(item)
        elif choice == 6:
            for d in list:
                print(d)




        playagain = input ('Do you want to play again? ')
        if playagain == 'no':
            flag = False
playgame()

