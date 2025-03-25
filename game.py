import sqlite3

conn = sqlite3.connect('game.db')
cur = conn.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS game_recommendation (
            id INTEGER PRIMARY KEY,
            title TEXT,
            developers TEXT,
            reviews TEXT,
            genre TEXT,
            synopsis TEXT
)

''')

game_data = [
    ('Alan Wake 2', 'Remedy Entertainment', '9/10 (IGN), 92% (Metacritic), Overwhelmingly Positive (Steam)', 'Survival Horror, Psychological Thriller', 'In this long-awaited sequel, writer Alan Wake is trapped in the Dark Place, a nightmarish realm of shifting realities. Meanwhile, FBI agent Saga Anderson investigates ritualistic murders in the town of Bright Falls. As their stories intertwine, players must unravel a gripping mystery while surviving supernatural horrors.'),
    ('Baldur Gate 3', 'Larian Studios', '10/10 (IGN), 96% (Metacritic), Overwhelmingly Positive (Steam)', 'RPG, Fantasy, Turn-Based Strategy', 'Set in the Dungeons & Dragons universe, this critically acclaimed RPG follows a group of adventurers infected with a mind-flayer parasite. Players make choices that shape the story, engage in strategic turn-based combat, and build relationships with a diverse cast of characters.'),
    ('Lies of P', 'Neowiz Games, Round8 Studio', '8/10 (IGN), 85/100 (Metacritic)', 'Soulslike, Action RPG', 'Inspired by Pinocchio, this dark, steampunk reimagining puts players in the role of P, a puppet warrior searching for his creator, Geppetto. Set in the decayed city of Krat, players must fight grotesque automatons, uncover dark secrets, and determine how much of their humanity remains.'),
    ('Resident Evil 4 (Remake)', 'Capcom', '10/10 (IGN), 93% (Metacritic), Overwhelmingly Positive (Steam)', 'Survival Horror, Action', 'A faithful yet reimagined remake of the 2005 classic, Resident Evil 4 follows special agent Leon S. Kennedy as he rescues the presidents daughter from a sinister cult in a rural Spanish village. With enhanced graphics, improved gameplay mechanics, and more horror elements, this remake revitalizes the iconic title.'),
    ('Helldivers 2', 'Arrowhead Game Studios', '9/10 (IGN), 86/100 (Metacritic)', 'Third-Person Shooter, Co-op Multiplayer', 'A satirical, over-the-top war game where players take on the role of Helldivers—elite soldiers defending "Super Earth" from alien threats. With chaotic combat, friendly fire always on, and a need for teamwork, it delivers intense and hilarious multiplayer action.'),
    ('Elden Ring', 'FromSoftware', '10/10 (IGN), 96% (Metacritic), Overwhelmingly Positive (Steam)', 'Action RPG, Open World', 'Set in the Lands Between, Elden Ring is a dark fantasy epic where players explore a vast open world, battle formidable foes, and uncover deep lore crafted by Hidetaka Miyazaki and George R.R. Martin. With punishing yet rewarding gameplay, the game builds upon FromSoftware’s signature Souls-like formula.')
]

cur.executemany('INSERT INTO game_recommendation (title, developers, reviews, genre, synopsis) VALUES (?,?,?,?,?)', game_data)

cur.execute('SELECT * FROM game_recommendation')
for row in cur.fetchall():
    print(row)

conn.commit()
conn.close()