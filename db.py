import sqlite3

CONN = sqlite3.connect('pizza_stack.db')
CURSOR = CONN.cursor()