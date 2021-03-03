#Functions

Artist = "Davido"
Genre = "Afro pop"
DurationInSeconds = 350
Year = 2010

def ForArtist():
    Order = Artist
    return Order
ForArtist()

def ForGenre():
    Order = Genre
    return Order
ForGenre()

def ForDurationInSeconds():
    Order = DurationInSeconds
    return Order
ForDurationInSeconds()

def ForYear():
    Order = Year
    return Order
ForYear()

def Boolean():
    Artist = 'Davido'
    while True:
        return Artist
Boolean()


Func1 = ForArtist()
print(Func1)
Func2 = ForGenre()
print(Func2)
Func3 = ForDurationInSeconds()
print(Func3)
Func4 = ForYear()
print(Func4)
Func5 = Boolean()
print(Func5)
#assignment 2 if/else
Grade = 70
School = 'Degree'
Admission = "Unknown"
Chance = True

if Grade >= 70 and School == 'Degree':
    Admission = "Accepted"

elif Grade < 60 >= 50 and School == 'Degree':
    Admission = "Probation"

elif Grade <50 and School == 'Degree':
    Admission = 'Unaccepted'

else:
    Admission = 'Not Applicable'

print(Admission)