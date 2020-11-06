# TRIPBOT - pure python3 IRC channel bot
#
#

"module loader (ldr)"

import importlib

from obj import Object

class Loader(Object):

    "holds modules table"

    table = Object()

    def load(self, name):
        "load module"
        if name not in self.table:
            self.table[name] = importlib.import_module(name)
        return self.table[name]
