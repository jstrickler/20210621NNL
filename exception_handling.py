import sqlite3

try:
    file_name = "wombats.txt"
    with open(file_name) as wombats_in:
        for line in wombats_in:
            print(line.rstrip())
except (FileNotFoundError, PermissionError) as err:
    print(err)

colors = ['red', 'blue', 'green', 'orange']
try:
    print(colors[9])
except IndexError as err:
    print(err)
except TypeError as err:
    print(err)


values = 5, 8.1, 0.0, 4.3, 2.7, 0, 3.9
for v in values:
    try:
        result = 23 / v
    except ZeroDivisionError as err:
        print(err)
    else:
        print(v, result)

conn = None
try:
    conn = sqlite3.connect('wombats.db')
except sqlite3.DatabaseError as err:
    print(err)
    exit()
else:  # if NO errors
    conn.execute("select 1")
finally:  # if errors or not
    if conn:
        conn.close()
