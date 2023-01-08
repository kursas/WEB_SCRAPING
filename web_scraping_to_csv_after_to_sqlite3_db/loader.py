from pathlib import Path
Path('AAAdata.db').touch()
import sqlite3
conn = sqlite3.connect('AAAdata.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS books (id  INTEGER, Title NOT NULL, Star_Rating NOT NULL,Price NOT NULL)''')
#id,Title,Star Rating,Price
import pandas as pd
# load the data into a Pandas DataFrame
users = pd.read_csv('AAAbooks.csv')
# write the data to a sqlite table
users.to_sql('books', conn, if_exists='append', index = False)
c.execute('''SELECT * FROM books''').fetchall()
c.fetchall()

#output
Process finished with exit code 0
