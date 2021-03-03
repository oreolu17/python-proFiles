# import sqlite3
#
# sqlite3.connect('user1.db')
# conn = sqlite3.connect('user1.db')
# print ("Opened database successfully")
# conn.execute('''CREATE TABLE COMPANT
#     (ID INT PRIMARY KEY NOT NULL,
#      NAME TEXT NOT NULL,            
#      ADDRESS CHAT(50),              ]'

#      SALARY REAL);''')
# print("Table created successfully");
# conn.close()





#
# import sqlite3
#
# conn = sqlite3.connect('user1.db')
# print ('Opened data base successfully' );
# conn.execute(" INSERT INTO COMPANT (ID , NAME , ADDRESS , SALARY) \
#              VALUES ( 1, 'Paul', 'Califonia', 20000.00)");
# conn.execute(" INSERT INTO COMPANT (ID , NAME , ADDRESS , SALARY) \
#              VALUES ( 2, 'Allan', 'Texas', 15000.00)");
# conn.execute(" INSERT INTO COMPANT (ID , NAME , ADDRESS , SALARY) \
#              VALUES ( 3, 'Teddy', 'Norway', 20000.00)");
# conn.execute(" INSERT INTO COMPANT (ID , NAME , ADDRESS , SALARY) \
#              VALUES ( 4, 'Mark', 'Richmond', 65000.00)");
# conn.commit()
# print("Records created successfully");
# conn.close()      


import sqlite3
conn = sqlite3.connect ('user1.db')
print("Opened data successfully" );

cursor = conn.execute("SELECT id, name, address, salary from COMPANT")
for row in cursor:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("ADDRESS = ", row[2])
    print("SALARY = ", row[3], "\n")
print ("Operation done successfully")
conn.close()