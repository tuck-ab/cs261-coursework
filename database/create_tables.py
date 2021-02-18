import sqlite3

conn = sqlite3.connect('live_feedback.db')

c = conn.cursor()

schema = open("database/schema.sql")
schema_string = schema.read()
c.executescript(schema_string)

conn.commit()

conn.close()