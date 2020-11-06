# TRIPBOT - pure python3 IRC channel bot
#
#

"config"

from dft import Default

class Cfg(Default):

    pass

def cfg(event):
    "configure irc."
    c = Cfg()
    last(c)
    print(event)
    if not event.args:
        event.reply(format(c, skip=["username", "realname"]))
        return
    from triple.irc import Cfg
    o = Object()
    parse(o, event.prs.otxt)
    if o.sets:
        update(c, o.sets)
        save(c)
