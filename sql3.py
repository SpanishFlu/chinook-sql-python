import sqlite3

# Connect to database
connection = sqlite3.connect("music_store.db")
cursor = connection.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS albums (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    artist TEXT,
    release_year INTEGER
)
""")

# Albums data (no IDs needed)
tracks = [
    ("6 elsob7", "Hussain elgasmy", 2000),
    ("masary x3", "ShabJdeed", 2003),
    ("Godzilla", "MNM", 2020),
]

# Insert multiple rows
cursor.executemany("""
INSERT INTO albums (name, artist, release_year)
VALUES (?, ?, ?)
""", tracks)

# Retrieve all albums
cursor.execute("SELECT * FROM albums")

results = cursor.fetchall()

# Display results
for row in results:
    print(row)

# Save changes and close connection
connection.commit()
connection.close()