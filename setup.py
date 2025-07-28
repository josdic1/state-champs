from lib import CURSOR, CONN

with open("setup.sql") as f:
    CURSOR.executescript(f.read())
    CONN.commit()
    
