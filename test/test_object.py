# TRIPBOT - pure python3 IRC channel bot
#
#

import os, types, unittest
import obj

from dbs import last
from obj import Object, load, save

class Test_Object(unittest.TestCase):

    def test_wd(self):
        oldwd = obj.wd
        obj.wd = "testdata"
        o = Object()
        o.key = "value"
        p = save(o)
        obj.wd = oldwd
        self.assertTrue(os.path.exists(os.path.join("testdata", "store", p)))

    def test_dotted(self):
        o = Object()
        o.o = Object()
        o.o.o = "bla"
        p = save(o)
        z = Object()
        load(z, p)
        self.assertTrue(z.o.o, "bla")

    def test_empty(self):
        o = Object()
        self.assertTrue(not o) 

    def test_final(self):
        o = Object()
        o.last = "bla"
        last(o)
        self.assertEqual(o.last, "bla")

    def test_stamp(self):
        o = Object()
        stp = save(o)
        self.assertTrue("Object" in stp)

    def test_attribute(self):
        o = Object()
        o.bla = "test"
        p = save(o)
        oo = Object()
        load(oo, p)
        self.assertEqual(oo.bla, "test")

    def test_changeattr(self):
        o = Object()
        o.bla = "test"
        p = save(o)
        oo = Object()
        load(oo, p)
        oo.bla = "mekker"
        pp = save(oo)
        ooo = Object()
        load(ooo, pp)
        self.assertEqual(ooo.bla, "mekker")

    def test_deleted(self):
        o = Object()
        o._deleted = True
        stp = save(o)
        oo = Object()
        load(oo, stp)
        self.assertEqual(oo._deleted, True)

    def test_contains(self):
        o = Object()
        o._deleted = True
        self.assertTrue("_deleted" in o)

    def test_last(self):
        o = Object()
        o.bla = "test"
        save(o)
        oo = Object()
        last(oo)
        self.assertEqual(oo.bla, "test")

    def test_lastest(self):
        o = Object()
        o.bla = "test"
        save(o)
        oo = Object()
        last(oo)
        oo.bla = "mekker"
        save(oo)
        ooo = Object()
        last(ooo)
        self.assertEqual(ooo.bla, "mekker")
