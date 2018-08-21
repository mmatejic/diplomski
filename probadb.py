import sqlite3

conn = sqlite3.connect('game.db')

c = conn.cursor()
#c.execute('INSERT INTO igrac (ime, poeni) values ("ImeIgraca", 123151231)')
#conn.commit()
#c.execute('delete from igrac where ime = "ImeIgraca"')
#conn.commit()


for row in c.execute('SELECT * FROM igrac'):
        print(row)

conn.close()
