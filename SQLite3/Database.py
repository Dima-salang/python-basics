import sqlite3

# Create a database
conn = sqlite3.connect('customers.db')

# Create a cursor
myCursor = conn.cursor()

# Create a table
# Data types in SQLite: NULL, INTEGER, TEXT, REAL, BLOB
# myCursor.execute(""" CREATE TABLE CustomerInfo (
#    firstName text,
#    lastName text,
#    email text,
#    contactNum integer
#    )""")

# Insert one record into table
# myCursor.execute("INSERT INTO CustomerInfo VALUES ('Therese', 'Gozum', 'therese@gmail.com', '987654321')")

# Insert multiple records
# multiple_customers = [
#                    ('Jake', 'Ramirez', 'jake@gmail.com', '456789123'),
#                    ('Sofia', 'First', 'sofia@gmail.com', '789456123')
#                     ]
# ? are placeholders
# myCursor.executemany(" INSERT INTO CustomerInfo VALUES (?,?,?,?)", multiple_customers)

# Querying a database
# asterisk means everything
# myCursor.execute("SELECT * FROM CustomerInfo")  # can also fetch primary key by rowid which is a unique id for each
# row where SQLite creates a column in the background.

# WHERE Clause
# myCursor.execute("SELECT * FROM CustomerInfo WHERE firstName = 'Luis'")

# WHERE + LIKE CLAUSE
# % is like a wildcard.
# myCursor.execute("SELECT * FROM CustomerInfo WHERE firstName LIKE 'Lu%'")

# UPDATE a record based on rowid
# myCursor.execute(""" UPDATE CustomerInfo SET email = 'sofia_1st@yahoo.com'
#            WHERE rowid = 4
# """)

# conn.commit()

# DELETE a record
# myCursor.execute("DELETE FROM CustomerInfo WHERE rowid = 3")

# DELETE all records
# myCursor.execute("DELETE FROM CustomerInfo")

# conn.commit()


myCursor.execute("SELECT rowid, * FROM CustomerInfo")

# myCursor.fetchone()
# myCursor.fetchmany(4)
info = myCursor.fetchall()

for data in info:
    print(data)

# Querying - AND and OR
# myCursor.execute("SELECT rowid, * FROM CustomerInfo WHERE firstName LIKE 'Lu%' AND lastName = 'Putan'")
# info3 = myCursor.fetchall()

# for data3 in info3:
#    print(data3)


# ORDER BY - ASC OR DESC
# myCursor.execute("SELECT rowid, * FROM CustomerInfo ORDER BY contactNum")
# info2 = myCursor.fetchall()

# for data2 in info2:
#    print(data2)

# Querying - Limiting Results
# myCursor.execute("SELECT rowid, * FROM CustomerInfo LIMIT 2")
# info4 = myCursor.fetchall()

# for data4 in info4:
#    print(data4)



# Format results
# print("NAME" + "\t\tEMAIL")
# for data in info:
#    print(data[1] + " " + data[0] + " | " + data[2])

# DROPPING A TABLE
# myCursor.execute("DROP TABLE CustomerInfo")
# conn.commit()

# Commit out command
conn.commit()

# Close the connection
conn.close()
