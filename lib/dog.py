import sqlite3

CONN = sqlite3.connect('lib/dogs.db')
CURSOR = CONN.cursor()

class Dog:
    
    def __init__(self, name, breed):
        self.id = None
        self.name= name
        self.breed = breed
    
#create table
    @classmethod
    def create_table(cls):
        sql= ("""CREATE TABLE IF NOT EXISTS dogs(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT,
                       breed TEXT) """)
        CURSOR.execute(sql)

#classmethod to drop table
    @classmethod
    def drop_table(cls, cursor):
        sql = ("""DROP TABLE IF EXISTS dogs""")
        cursor.execute(sql)

# Saves a new dog object into the database or updates an existing one if it already exists.
    def save(self):
        sql = """
            INSERT INTO dogs (name, breed) 
            VALUES(?, ?)
            """
        CURSOR.execute(sql, (self.name, self.breed))
        CONN.commit()
        self.id = CURSOR.execute("SELECT last_insert_rowid() FROM dogs").fetchone()[0]

# Create a new row in the database.
# Return a new instance of the Dog class.
    @classmethod
    def create(cls):
        pass




