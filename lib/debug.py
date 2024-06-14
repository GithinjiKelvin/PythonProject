#!/usr/bin/env python3

from db.__init__ import CONN, CURSOR
from db.owner import Owner

import ipdb

def recreatedb():
    Owner.drop_table()
    Owner.create_table()

    Owner.create("Kelvin", 25)
    Owner.create("Maggie", 20)
    Owner.create("Peter", 45)
    Owner.create("Rose", 40)




recreatedb()
ipdb.set_trace()