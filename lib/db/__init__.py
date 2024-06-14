#db/__init__.py
import sqlite3

CONN = sqlite3.connect('realestate.db')
CURSOR = CONN.cursor()