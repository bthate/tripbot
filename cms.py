# TRIPBOT - pure python3 IRC channel bot
#
#

"commands"

import threading, time

from dft import Default
from krn import get_kernel, starttime
from obj import Object, get, keys, save, update
from ofn import format
from prs import parse
from tms import elapsed
from utl import get_name

def cmd(event):
    "list commands (cmd)"
    k = get_kernel()
    c = sorted(keys(k.cmds))
    if c:
        event.reply(",".join(c))

def krn(event):
    "configure irc."
    k = get_kernel()
    o = Default()
    parse(o, event.prs.otxt)
    if o.sets:
        update(k.cfg, o.sets)
        save(k.cfg)
    event.reply(format(k.cfg))

def tsk(event):
    "list tasks (tsk)"
    psformat = "%s %s"
    result = []
    for thr in sorted(threading.enumerate(), key=lambda x: x.getName()):
        if str(thr).startswith("<_"):
            continue
        o = Object()
        update(o, thr)
        if get(o, "sleep", None):
            up = o.sleep - int(time.time() - o.state.latest)
        else:
            up = int(time.time() - starttime)
        thrname = thr.getName()
        result.append((up, psformat % (thrname, elapsed(up))))
    res = []
    for up, txt in sorted(result, key=lambda x: x[0]):
        res.append(txt)
    if res:
        event.reply(" | ".join(res))

def ver(event):
    "show version (ver)"
    import krn
    event.reply("TRIPBOT %s" % krn.__version__)
