import sqlite3

CONN = sqlite3.connect('lib/dogs.db')
CURSOR = CONN.cursor()

class Dog:

    all = [] #this will store the data retrieved from the database
    
    def __init__(self, name, breed):
        self.id = None
        self.name= name
        self.breed = breed
    
#create table
    @classmethod
    def create_table(cls):
        sql= """
                CREATE TABLE IF NOT EXISTS dogs(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                breed TEXT) 
            """
        CURSOR.execute(sql)

#classmethod to drop table
    @classmethod
    def drop_table(cls):
        sql = """
               DROP TABLE IF EXISTS dogs
            """
        CURSOR.execute(sql)

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
    def create(cls , name , breed):
        dog= Dog(name, breed)
        dog.save()
        return dog
    
#This classmethod retrieve data in the database is going to return an array representing a dog's data. 
#We need a way to cast that data into the appropriate attributes of a dog. This method encapsulates that functionality. 
    @classmethod
    def new_from_db(cls, row):
        dog= cls(row[1], row[2])
        dog.id = row[0]

# This class method should return a list of Dog instances for every record in the dogs table.
    @classmethod
    def get_all(cls):
        sql = """
                SELECT * 
                FROM dogs
            """
        all= CURSOR.execute(sql).fetchall()
        cls.all = [cls.new_from_db(row) for row in all]

# The test for this method will first insert a dog into the database and then attempt to find it by calling the find_by_name() method. 
# The expectations are that an instance of the dog class that has all the properties of a dog is returned, not primitive data.
    @classmethod
    def find_by_name(cls , name):
        sql= """
            SELECT * FROM dogs WHERE name = ? LIMIT 1
        """
        song= CURSOR.execute(sql, (name)).fetchone()
        return cls.new_from_db(song)

# This class method takes in an ID, and should return a single Dog instance for the corresponding record in the dogs table with that same ID. It behaves similarly to the find_by_name() method above.
    @classmethod
    def find_by_id(cls , self):
        sql= """
            SELECT * FROM dogs WHERE name = ? LIMIT 1
        """
        song= CURSOR.execute(sql, (self.id)).fetchone()
        return cls.new_from_db(song)
    
        




