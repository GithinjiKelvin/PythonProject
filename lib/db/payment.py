#lib/db/aparpaymenttment.py
from db.__init__ import CURSOR, CONN

from db.tenant import Tenant

class Payment:

    all = {}

    def __init__(self, transaction_code, amount, tenant_id, id = None):
        self.id = id
        self.transaction_code = transaction_code
        self.amount = amount
        
        self.tenant_id = tenant_id
    
    def __repr__(self):
        return (
            f"<Payment {self.id}: {self.transaction_code}, {self.amount}, " +
           
            f"Tenant ID: {self.tenant_id}>"
        )
    
    @property
    def transaction_code(self):
        return self._transaction_code
    
    @transaction_code.setter
    def transaction_code(self, transaction_code):
        if isinstance(transaction_code, str) and len(transaction_code):
            self._transaction_code = transaction_code
        else:
            raise ValueError("Transaction_code must be a non empty string ")
    
    @property
    def amount(self):
        return self._amount
    
    @amount.setter
    def amount(self, amount):
        if isinstance(amount, int) :
            self._amount = amount
        else:
            raise ValueError("Amount must be a non empty Integer ")
        
    
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
                CREATE TABLE IF NOT EXISTS payments (
                id INTEGER PRIMARY KEY,
                transaction_code TEXT,
                amount INTEGER,
                tenant_id INTEGER,
                FOREIGN KEY (tenant_id) REFERENCES tenants(id))
                
            """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):

        sql = """
                DROP TABLE IF EXISTS payments;
            """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):

        sql = """
                INSERT INTO payments(transaction_code, amount, tenant_id)
                VALUES (?, ?, ?)
            """
        CURSOR.execute(sql, (self.transaction_code, self.amount, self.tenant_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
    
    def update(self):

        sql = """
                UPDATE payments
                SET transaction_code = ?, amount = ?, tenant_id = ?
                WHERE id = ?
            """
        CURSOR.execute(sql, (self.transaction_code, self.amount, self.tenant_id, self.id))
        CONN.commit()
    
    def delete(self):
        sql = """
                DELETE FROM payments
                WHERE id = ?
            """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None
    
    @classmethod
    def create(cls, transaction_code, amount, tenant_id):
        payment = cls(transaction_code, amount, tenant_id)
        payment.save()
        return payment
    
    @classmethod
    def instance_from_db(cls, row):
        payment = cls.all.get(row[0])
        if payment:
            payment.transaction_code = row[1]
            payment.amount = row[2]
            payment.tenant_id = row[3]
        else:
            payment = cls(row[1], row[2], row[3])
            payment.id = row[0]
            cls.all[payment.id] = payment
        return payment
    
    @classmethod
    def get_all(cls):
        sql = """
                SELECT * FROM payments
            """
        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
                 SELECT *
                FROM payments
                WHERE id = ?
            """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM payments
            WHERE name is ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

