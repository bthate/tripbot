# TRIPBOT - pure python3 IRC channel bot
#
#

"data entry"

from dbs import find
from obj import Object, save
from utl import get_type

class Log(Object):

    "log items"

    def __init__(self):
        super().__init__()
        self.txt = ""

class Todo(Object):

    "todo items"

    def __init__(self):
        super().__init__()
        self.txt = ""

def dne(event):
    "flag a todo item as done (dne)"
    if not event.args:
        return
    selector = {"txt": event.args[0]}
    for fn, o in find("ent.Todo", selector):
        o._deleted = True
        save(o)
        event.reply("ok")
        break

def log(event):
    "log some text (log)"
    if not event.rest:
        return
    l = Log()
    l.txt = event.rest
    save(l)
    event.reply("ok")

def tdo(event):
    "add a todo item (tdo)"
    if not event.rest:
        return
    o = Todo()
    o.txt = event.rest
    save(o)
    event.reply("ok")
