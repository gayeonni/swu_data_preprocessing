import sqlite3

conn = sqlite3.connect('test2.db')  # create and connect db
cursor = conn.cursor()

create_query = "CREATE TABLE friend_info(friend_id int, friend_name text)"  # create SQL statement
cursor.execute(create_query)  # execute SQL statement

insert_query = "INSERT INTO friend_info VALUES(1, 'megan')"  # create SQL statement
cursor.execute(insert_query)  # execute SQL statement

select_query = "SELECT * FROM friend_info"  # create SQL statement
cursor.execute(select_query)  # execute SQL statement
print(cursor.fetchall())  # show all retrieved results
