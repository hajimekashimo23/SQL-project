import sqlite3

conn = sqlite3.connect('youtube_favorites.db')
cur = conn.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS youtube_videos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        link TEXT NOT NULL,
        creator TEXT,
        release_date TEXT,
        description TEXT
    )
''')

videos_data = [
    ('PLOT: Ketika Rudal Amerika Jatuh ke tangan Iran (Cerita Game Call of Duty Modern Warfare II - 2022)', 'https://www.youtube.com/watch?v=clcq2cl4Mv4', 'Droomp', '2022-10-29', 'Melanjutkan kisah Modern Warfare (2019), Task Force 141 kini telah dikenal sebagai pasukan elit yang sangat berbahaya. Di bawah komando General Shepherd, Price, Soap, Ghost, dan Gaz bekerjasama dengan Shadow Company dan Los Vaqueros untuk mencari 3 rudal amerika yang menghilang..'),
    ('PLOT: Kisah Ngeri dan Tragis di Tengah Lautan Luas (Cerita Game Still Wakes The Deep + Penjelasan)', 'https://www.youtube.com/watch?v=Vxk7RN-Dtz4', 'Droomp', '2024-06-27', 'Kisah tragis dalam insiden di sebauh anjungan pengeboran minyak bernama Beira D. Caz sang montir listrik harus berusaha bertahan hidup di tengah kekhawatirannya akan masa depan keluarganya.'),
    ('PLOT: Kutukan Desa Keluarga Chen dan Bunda Buddha | Incantation', 'https://www.youtube.com/watch?v=S0kXBUqu37Q&t=4257s', 'Droomp', '2024-11-28', 'Film horror asal Taiwan berjudul Incantation mendapatkan adaptasi game dengan judul yang sama..'),
    ('PLOT: Hotel Penuh Orang - Orang Aneh | The Inn-Sanity', 'https://www.youtube.com/watch?v=Qe2S3n0DT0g&t=134s', 'Droomp', '2024-11-26', 'Seluruh Alur Cerita Game The Inn Sanity Terjebak di dalam sebuah hotel mewah, dan entah kenapa semua wajah penghuni hotel terlihat sangat aneh...'),
    ('KUTUK4N KELUARGA YG MEMBAWA KARM4 BURUK BAGI SEMUA KETURUNANYA - SELURUH ALUR CERITA THE MEDIUM', 'https://www.youtube.com/watch?v=6uu_xMe2d98', 'Story Pal', '2023-04-19', 'Video ini membahas tentang ALUR CERITA FILM THE MEDIUM (2021)')
]

cur.executemany('INSERT INTO youtube_videos (title, link, creator, release_date, description) VALUES (?,?,?,?,?)', videos_data)


cur.execute("UPDATE youtube_videos SET title = 'PLOT: Kisah Seram di Lautan Luas (Revisi)' WHERE title = 'PLOT: Kisah Ngeri dan Tragis di Tengah Lautan Luas (Cerita Game Still Wakes The Deep + Penjelasan)'")


cur.execute("DELETE FROM youtube_videos WHERE title = 'PLOT: Hotel Penuh Orang - Orang Aneh | The Inn-Sanity'")

cur.execute('SELECT * FROM youtube_videos')
for row in cur.fetchall():
    print(row)

conn.commit()
conn.close()
