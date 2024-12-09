import sqlite3
from pydantic import BaseModel

class Mall(BaseModel):
    name: str
    is_aeon: bool

def main():
    conn = sqlite3.connect('./db/malls.db')

    # create table
    conn.execute('''
        CREATE TABLE IF NOT EXISTS malls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            is_aeon BOOLEAN NOT NULL
        )
    ''')

    conn.commit()

    malls = [
        Mall(name='Aeon Mall', is_aeon=True),
        Mall(name='Ito Yokado', is_aeon=False),
        Mall(name='Sogo', is_aeon=False)
    ]

    for mall in malls:
        conn.execute('''
            INSERT INTO malls (name, is_aeon) VALUES (?, ?)
        ''', (mall.name, mall.is_aeon))

    conn.commit()

    # select data

    cursor = conn.execute('''
        SELECT * FROM malls WHERE is_aeon = 0
    ''')

    for row in cursor:
        print(row)

    conn.close()

if __name__ == '__main__':
    main()