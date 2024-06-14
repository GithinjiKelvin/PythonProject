#!/usr/bin/env python3

from db.__init__ import CONN, CURSOR
from db.owner import Owner
from db.apartment import Apartment
from db.tenant import Tenant
from db.payment import Payment

# import ipdb

def recreatedb():
    Owner.drop_table()
    Owner.create_table()
    Apartment.drop_table()
    Apartment.create_table()
    Tenant.drop_table()
    Tenant.create_table()
    Payment.drop_table()
    Payment.create_table()

    Owner.create("Kelvin", 25)
    Owner.create("Maggie", 20)
    Owner.create("Peter", 45)
    Owner.create("Rose", 40)

    Tenant.create("Kev", 20, 9876)
    Tenant.create("Mary", 20, 9876)
    Tenant.create("Neema", 20, 9876)
    Tenant.create("Abby", 20, 9876)
    Tenant.create("Jeff", 20, 9876)

    Apartment.create("Malaika", "Roysambu", 1, 2)
    Apartment.create("Jamhuri", "Kasarani", 1, 1)
    Apartment.create("Neptune", "Kilimani", 2, 3)
    Apartment.create("Mars", "Kileleshwa", 2, 4)
    Apartment.create("Prestige", "Prestige", 3, 1)
    Apartment.create("Naresho", "Kilimani", 3, 2)
    Apartment.create("Fancy", "Westalands", 4, 4)
    

    Payment.create("transaction1", 20000, 4)
    Payment.create("transaction2", 26000, 1)
    Payment.create("transaction3", 22000, 4)
    Payment.create("transaction4", 26000, 3)
    Payment.create("transaction5", 20000, 2)
    


recreatedb()
# ipdb.set_trace()