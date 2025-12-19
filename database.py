import sqlite3
from flask import g
import os 

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect("base_de_donnees.db")
        g.db.row_factory =sqlite3.Row
    return g.db

def close_db(e=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()
