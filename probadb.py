import random
import sqlite3

conn = sqlite3.connect('game.db')

c = conn.cursor()
#for i in range(10):
        #c.execute('INSERT INTO igrac (ime, poeni) values ("Mihailo", ' + str(random.randint(2000, 10000)) + ')')
#conn.commit()
c.execute('delete from igrac where ime = ""')
conn.commit()


for row in c.execute('SELECT * FROM igrac'):
        print(row)

conn.close()
