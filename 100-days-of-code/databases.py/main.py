import sqlite3

conn = sqlite3.connect("connect.db")
c = conn.cursor()
# c.execute('''CREATE TABLE customer(
#     first_name text,
#     last_name text
#     )''')
# c.execute("INSERT INTO customer VALUES ('samwin','pinto')")
# many_costumers = [('joy','ben'),
#                   ('chris','pinto'),
#                   ]
# c.executemany("INSERT INTO customer VALUES (?,?)", many_costumers)

#query and fetch

c.execute("UPDATE customer SET first_name='charis' WHERE last_name ='pinto'")
c.execute("SELECT rowid,* FROM customer")
print(c.fetchall())

conn.commit()
conn.close()