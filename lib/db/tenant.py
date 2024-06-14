#lib/db/tenant.py
from db.__init__ import CURSOR, CONN

class Tenant:

    all = {}

    def __init__(self, name, age, phone_num, id = None):
        self.id = id
        self.name = name
        self.age = age
        self.phone_num = phone_num
    
    def __repr__(self):
        return (
            f"<Owner {self.id}: {self.name}, {self.age}, {self.phone_num}>"
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
                CREATE TABLE IF NOT EXISTS tenants (
                id INTEGER PRIMARY KEY,
                name TEXT,
                age INTEGER,
                phone_num INTEGER
                )
            """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):

        sql = """
                DROP TABLE IF EXISTS tenants;
            """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):

        sql = """
                INSERT INTO tenants(name, age, phone_num)
                VALUES (?, ?, ?)
            """
        CURSOR.execute(sql, (self.name, self.age, self.phone_num))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
    
    def update(self):

        sql = """
                UPDATE tenants
                SET name = ?, age = ?, phone_num = ?
                WHERE id = ?
            """
        CURSOR.execute(sql, (self.name, self.age, self.phone_num, self.id))
        CONN.commit()
    
    def delete(self):
        sql = """
                DELETE FROM tenants
                WHERE id = ?
            """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None
    
    @classmethod
    def create(cls, name, age, phone_num):
        tenant = cls(name, age, phone_num)
        tenant.save()
        return tenant
    
    @classmethod
    def instance_from_db(cls, row):
        tenant = cls.all.get(row[0])
        if tenant:
            tenant.name = row[1]
            tenant.age = row[2]
            tenant.phone_num = row[3]
        else:
            tenant = cls(row[1], row[2], row[3])
            tenant.id = row[0]
            cls.all[tenant.id] = tenant
        return tenant
    
    @classmethod
    def get_all(cls):
        sql = """
                SELECT * FROM tenants
            """
        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
                 SELECT *
                FROM tenants
                WHERE id = ?
            """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM tenants
            WHERE name is ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def apartments(self):
        from db.apartment import Apartment

        sql = """
                SELECT * FROM apartments
                WHERE tenant_id = ?
            """
        CURSOR.execute(sql, (self.id, ),)

        rows = CURSOR.fetchall()
        return [Apartment.instance_from_db(row) for row in rows]

