# Project Title
Discuss the purpose of this database in the context of the startup, Sparkify, and their analytical goals.

Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app.
The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

## Getting Started

Run create_tables.py to create your database and tables.
Run test.ipynb to confirm the creation of your tables with the correct columns. 
Run etl.py, where you'll process the entire datasets. Remember to run create_tables.py before running etl.py to reset your tables. Run test.ipynb to confirm your records were successfully inserted into each table.

### Prerequisites
Libraries:

*os
*glob
*psycopg2
*pandas
*sql_queries

### Schema design and ETL pipeline
<h4>Fact Table</h4>
<br>
<p>songplays - records in log data associated with song plays i.e. records with page NextSong</p>

<p>songplay_id , start_time, user_id, level, song_id, artist_id, session_id, location, user_agent</p>

<p>Primary Key identifiers for songplays are songplay_id and session_id. such as songplay is the unique identifier for the
fact table and we want to analyze unique session_ids.</p>

<p>Songplay_id has to be generated automatically so it a identity field.</p>
<br>
<h4>Dimension Tables</h4>
<br>
<p>users - users in the app.<p>
<p>user_id (Primary_key), first_name, last_name, gender, level</p>

<p>songs - songs in music database</p>

<p>song_id, title, artist_id, year, duration</p>
Compound primary key for song_id and artist_id because a song is unique for each artist.

<p>artists - artists in music database</p>
<p>artist_id, name, location, latitude, longitude
primary key artist_id</p>

<p>time - timestamps of records in songplays broken down into specific units</p>

<p>start_time, hour, day, week, month, year, weekday</p>

<p>start_time is a timestamp with miliseconds so it's the unique identifier</p>

<h1>ETL PIPELINE:</h1><br>
<p>I used some functions like drop_duplicates() because there are some rows duplicates on json files, that 
can raise errors inserting values.</p>

## Authors
* **William Suarez** 


