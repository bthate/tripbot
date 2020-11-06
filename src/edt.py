# TRIPBOT - pure python3 IRC channel bot
#
#

"edit objects"

from dbs import lasttype
from krn import get_kernel
from obj import get, get_cls, save
from ofn import edit
from utl import list_files

def edt(event):
    "edit objects"
    if not event.args:
        import obj
        assert obj.wd
        f = list_files(obj.wd)
        if f:
            event.reply(f)
        return
    k = get_kernel()
    cn = get(k.names, event.args[0], [event.args[0]])
    if len(cn) > 1:
        event.reply(cn)
        return
    cn = cn[0]
    l = lasttype(cn)
    if not l:
        return
    if not event.prs.sets:
        event.reply(l)
        return
    edit(l, event.prs.sets)
    save(l)
    event.reply("ok")
