import sqlite3

CONN = sqlite3.connect('state_champs.db')
CURSOR = CONN.cursor()