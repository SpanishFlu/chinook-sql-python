#create tables in databes
import sqlite3 
con = sqlite3.connect('music.db')
cursor = con.cursor()
tracks = [
    ("lUREN", "adsd", "asf", 12)
    ("asdsd", "asdas", "asfdsd", 23)
    ("saass","adssf","asddssd", 2323 )
]
cursor.executemany("INSERT INTO tracks VALUES (?,?, ?, ?)", tracks)
#data = cursor.execute("SELECT * FROM tracks")
#for counter in data:
#    print(counter)
con.commit()
con.close()