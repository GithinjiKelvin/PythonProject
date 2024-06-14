#lib/db/owner.py
from db.__init__ import CURSOR, CONN

class Owner:

    all = {}

    def __init__(self, name, age, id = None):
        self.id = id
        self.name = name
        self.age = age
    
    def __repr__(self):
        return (
            f"<Owner {self.id}: {self.name}, {self.age}>"
        )
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError("Name must be a non empty string ")
    
    @classmethod
    def create_table(cls):

        sql = """
                CREATE TABLE IF NOT EXISTS owners (
                id INTEGER PRIMARY KEY,
                name TEXT,
                age INTEGER
                )
            """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):

        sql = """
                DROP TABLE IF EXISTS owners;
            """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):

        sql = """
                INSERT INTO owners(name, age)
                VALUES (?, ?)
            """
        CURSOR.execute(sql, (self.name, self.age))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
    
    def update(self):

        sql = """
                UPDATE owners
                SET name = ?, age = ?
                WHERE id = ?
            """
        CURSOR.execute(sql, (self.name, self.age, self.id))
        CONN.commit()
    
    def delete(self):
        sql = """
                DELETE FROM owners
                WHERE id = ?
            """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None
    
    @classmethod
    def create(cls, name, age):
        owner = cls(name, age)
        owner.save()
        return owner
    
    @classmethod
    def instance_from_db(cls, row):
        owner = cls.all.get(row[0])
        if owner:
            owner.name = row[1]
            owner.age = row[2]
        else:
            owner = cls(row[1], row[2])
            owner.id = row[0]
            cls.all[owner.id] = owner
        return owner
    
    @classmethod
    def get_all(cls):
        sql = """
                SELECT * FROM owners
            """
        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
                 SELECT *
                FROM owners
                WHERE id = ?
            """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM owners
            WHERE name is ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def apartments(self):
        from db.apartment import Apartment

        sql = """
                SELECT * FROM apartments
                WHERE owner_id = ?
            """
        CURSOR.execute(sql, (self.id, ),)

        rows = CURSOR.fetchall()
        return [Apartment.instance_from_db(row) for row in rows]

