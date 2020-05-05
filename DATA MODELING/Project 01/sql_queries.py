# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS SONGPLAY;"
user_table_drop = "DROP TABLE IF EXISTS USERS;"
song_table_drop = "DROP TABLE IF EXISTS SONGS;"
artist_table_drop = "DROP TABLE IF EXISTS ARTISTS;"
time_table_drop = "DROP TABLE IF EXISTS TIME;"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS SONGPLAYS (songplay_id int GENERATED ALWAYS AS IDENTITY, start_time bigint, user_id varchar, level varchar, song_id varchar, artist_id varchar, session_id int, location varchar, user_agent varchar,
PRIMARY KEY (songplay_id,session_id),
FOREIGN KEY (user_id) REFERENCES users (user_id),
FOREIGN KEY (song_id,artist_id) REFERENCES songs (song_id,artist_id),
FOREIGN KEY (artist_id) REFERENCES artists (artist_id),
FOREIGN KEY (start_time) REFERENCES time (start_time)); 
""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users (user_id varchar, first_name varchar, last_name varchar, gender varchar, level varchar, PRIMARY KEY (user_id));
""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS SONGS (song_id varchar, title varchar, artist_id varchar, year int, duration float, PRIMARY KEY (song_id,artist_id));
""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists (artist_id varchar, name varchar, location varchar, latitude float, longitude float, PRIMARY KEY (artist_id));
""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time (start_time bigint, hour int, day int, week int, month int, year int, weekday int, PRIMARY KEY (start_time)); 
""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO SONGPLAYS(start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)
""")

user_table_insert = ("""INSERT INTO USERS(user_id, first_name, last_name, gender, level) VALUES(%s,%s,%s,%s,%s)
 """)

song_table_insert = ("""INSERT INTO SONGS(song_id, title, artist_id, year, duration) VALUES(%s,%s,%s,%s,%s)""")

artist_table_insert = ("""INSERT INTO ARTISTS(artist_id, name, location, latitude, longitude) values(%s,%s,%s,%s,%s)
 """)


time_table_insert = ("""INSERT INTO TIME(start_time, hour, day, week, month, year, weekday) values(%s,%s,%s,%s,%s,%s,%s)
 """)

# FIND SONGS

song_select = ("""SELECT s.song_id,s.artist_id
FROM songs s
JOIN artists a on a.artist_id = s.artist_id
WHERE 1=1
and s.title = %s
and a.name = %s
and s.duration = %s
""")

# QUERY LISTS

create_table_queries = [user_table_create, song_table_create, artist_table_create, time_table_create,songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]