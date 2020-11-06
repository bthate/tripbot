# TRIPBOT - pure python3 IRC channel bot
#
#

"config"

from dbs import last
from dft import Default
from ofn import format

class Cfg(Default):

    pass

def cfg(event):
    "configure irc."
    from irc import Cfg
    c = Cfg()
    last(c)
    if not event.args:
        event.reply(format(c, skip=["username", "realname"]))
        return
    o = Object()
    parse(o, event.prs.otxt)
    if o.sets:
        update(c, o.sets)
        save(c)
