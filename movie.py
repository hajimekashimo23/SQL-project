import sqlite3

conn = sqlite3.connect('movies.db')
cur = conn.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS movies_rating (
           id INTEGER PRIMARY KEY, 
           title TEXT NOT NULL,
           movie_director TEXT NOT NULL,
           release_date TEXT,
           ratings TEXT,
           synopsis TEXT
) 

''')

movies_data = [
    ('Inception', 'Christopher Nolan', 'July 16, 2010', 'IMDb Rating: 8.8/10', 'A skilled thief, Dom Cobb, who has the ability to enter peoples dreams and steal secrets, is given the chance to have his criminal record erased. To do so, he must implant an idea into someones subconscious—a task known as inception.'),
    ('Parasite', 'Bong Joon-ho', 'May 30, 2019', 'IMDb Rating: 8.5/10', 'A poor family infiltrates the lives of a wealthy household by posing as highly qualified workers. As their deception deepens, an unexpected turn of events leads to chaos and tragedy.'),
    ('The Dark Knight', 'Christopher Nolan', 'July 18, 2008', 'IMDb Rating: 9.0/10', 'With Gotham City under threat from the Joker, Batman must push his limits to stop the criminal masterminds reign of terror, all while struggling with his own moral dilemmas.'),
    ('Interstellar', 'Christopher Nolan', 'November 7, 2014', 'IMDb Rating: 8.7/10', 'In a dystopian future where Earth is dying, a group of astronauts embarks on a mission through a wormhole in search of a new habitable planet for humanity.'),
    ('The Shawshank Redemption', 'Frank Darabont', 'September 23, 1994', 'IMDb Rating: 9.3/10', 'Andy Dufresne, a banker falsely convicted of murder, is sentenced to life in Shawshank prison. Over the years, he forms a deep friendship with fellow inmate Red and works on a plan that changes everything.')
]

cur.executemany('INSERT INTO movies_rating (title, movie_director, release_date, ratings, synopsis) VALUES (?,?,?,?,?)', movies_data)

cur.execute('SELECT * FROM movies_rating')
for row in cur.fetchall():
    print(row)

conn.commit()
conn.close()