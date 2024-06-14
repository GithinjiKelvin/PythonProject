#!/usr/bin/env python3

from db.__init__ import CONN, CURSOR
from db.owner import Owner
from db.apartment import Apartment

import ipdb

def recreatedb():
    Owner.drop_table()
    Owner.create_table()
    Apartment.drop_table()
    Apartment.create_table()

    Owner.create("Kelvin", 25)
    Owner.create("Maggie", 20)
    Owner.create("Peter", 45)
    Owner.create("Rose", 40)

    Apartment.create("Malaika", "Roysambu", 1)
    Apartment.create("Jamhuri", "Kasarani", 1)
    Apartment.create("Neptune", "Kilimani", 2)
    Apartment.create("Mars", "Kileleshwa", 2)
    Apartment.create("Prestige", "Prestige", 3)
    Apartment.create("Naresho", "Kilimani", 3)
    Apartment.create("Fancy", "Westalands", 4)
    Apartment.create("Dubai", "Roysambu", 4)

    




recreatedb()
ipdb.set_trace()