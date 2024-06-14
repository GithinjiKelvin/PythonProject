#lib/db/apartment.py
from db.__init__ import CURSOR, CONN
from db.owner import Owner
from db.tenant import Tenant

class Apartment:

    all = {}

    def __init__(self, name, location, owner_id, tenant_id, id = None):
        self.id = id
        self.name = name
        self.location = location
        self.owner_id = owner_id
        self.tenant_id = tenant_id
    
    def __repr__(self):
        return (
            f"<Apartment {self.id}: {self.name}, {self.location}, " +
            f"Owner ID: {self.owner_id}"+
            f"Tenant ID: {self.tenant_id}>"
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
    
    @property
    def location(self):
        return self._location
    
    @location.setter
    def location(self, location):
        if isinstance(location, str) and len(location):
            self._location = location
        else:
            raise ValueError("Location must be a non empty string ")
        
    @property
    def owner_id(self):
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        if type(owner_id) is int and Owner.find_by_id(owner_id):
            self._owner_id = owner_id
        else:
            raise ValueError(
                "owner_id must reference a owner in the database")
    @property
    def tenant_id(self):
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        if type(tenant_id) is int and Tenant.find_by_id(tenant_id):
            self._tenant_id = tenant_id
        else:
            raise ValueError(
                "Tenant_id must reference a tenant in the database")

    
    @classmethod
    def create_table(cls):

        sql = """
                CREATE TABLE IF NOT EXISTS apartments (
                id INTEGER PRIMARY KEY,
                name TEXT,
                location TEXT,
                owner_id INTEGER,
                tenant_id INTEGER,
                FOREIGN KEY (owner_id) REFERENCES owners(id),
                
                FOREIGN KEY (tenant_id) REFERENCES tenants(id))
                
            """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):

        sql = """
                DROP TABLE IF EXISTS apartments;
            """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):

        sql = """
                INSERT INTO apartments(name, location, owner_id, tenant_id)
                VALUES (?, ?, ?, ?)
            """
        CURSOR.execute(sql, (self.name, self.location, self.owner_id, self.tenant_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
    
    def update(self):

        sql = """
                UPDATE apartments
                SET name = ?, location = ?, owner_id = ?, tenant_id = ?
                WHERE id = ?
            """
        CURSOR.execute(sql, (self.name, self.location, self.owner_id, self.tenant_id, self.id))
        CONN.commit()
    
    def delete(self):
        sql = """
                DELETE FROM apartments
                WHERE id = ?
            """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None
    
    @classmethod
    def create(cls, name, location, owner_id, tenant_id):
        apartment = cls(name, location, owner_id, tenant_id)
        apartment.save()
        return apartment
    
    @classmethod
    def instance_from_db(cls, row):
        apartment = cls.all.get(row[0])
        if apartment:
            apartment.name = row[1]
            apartment.location = row[2]
            apartment.owner_id = row[3]
            apartment.tenant_id = row[4]
        else:
            apartment = cls(row[1], row[2], row[3], row[4])
            apartment.id = row[0]
            cls.all[apartment.id] = apartment
        return apartment
    
    @classmethod
    def get_all(cls):
        sql = """
                SELECT * FROM apartments
            """
        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
                 SELECT *
                FROM apartments
                WHERE id = ?
            """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM apartments
            WHERE name is ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

