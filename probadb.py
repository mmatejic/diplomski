import random
import sqlite3

#conn = sqlite3.connect('game.db')

#c = conn.cursor()
#for i in range(10):
        #c.execute('INSERT INTO igrac (ime, poeni) values ("Mihailo", ' + str(random.randint(2000, 10000)) + ')')
#conn.commit()
#c.execute('delete from igrac where ime = ""')
#conn.commit()

#c.execute('delete from igrac where poeni = 1925')
#conn.commit()
#c.execute("insert into igrac (ime, poeni) values ('Dusan', 7552)")
#conn.commit()
#broj = c.execute('update igrac set ime = "Mihailo", poeni = 0 where poeni = 28829')
#conn.commit()
#broj = c.execute('select * from igrac order by poeni desc')
#print(list(c.execute('select count(*) from igrac')))


#conn.close()


string = "100.546,30"
string = string.replace('.', '')
string = string.replace(',', '.')
floating = float(string)
print(type(floating))
print(floating)

