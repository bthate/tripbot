# TRIPBOT - pure python3 IRC channel bot
#
#

import os, random, sys, time, unittest

from evt import Event
from krn import get_kernel
from obj import Object, get
from tsk import start

param = Object()
param.add = ["test@shell", "bart"]
param.dne = ["test4", ""]
param.edt = ["ent.Todo txt=bla", "ent.Log txt=bla", "ent.Todo txt=bla", "ent.Log txt=bla",
             "ent.Todo", "ent.Log", "todo", "log", "todo txt=okdan", "log txt=okdan"]
param.rm = ["reddit", ]
param.dpl = ["reddit title,summary,link",]
param.log = ["test1", ""]
param.flt = ["0", "1", ""]
param.fnd = ["log", "todo", "rss"]
param.rss = ["https://www.reddit.com/r/python/.rss", ""]
param.tdo = ["test4", ""]

events = []
ignore = []
nrtimes = 1

def open(txt):
    try:
        for line in os.popen(txt).readlines():
            print(line.rstrip())
    except:
        pass

k = get_kernel()

class Event(Event):

    def reply(self, txt):
        if "v" in k.cfg.opts:
            print(txt)

class Test_Tinder(unittest.TestCase):

    def test_all(self):
        for x in range(k.cfg.index or 1):
            tests(k)

    def test_thrs(self):
        thrs = []
        for x in range(k.cfg.index or 1):
            start(tests, k)
        consume(events)
        
def consume(elems):
    fixed = []
    res = []
    for e in elems:
        r = e.wait()
        res.append(r)
        fixed.append(e)
    for f in fixed:
        try:
            elems.remove(f)
        except ValueError:
            continue
    k.stop()
    return res
    
def tests(b):
    keys = list(k.cmds)
    random.shuffle(keys)
    for cmd in keys:
        if cmd in ignore:
            continue
        events.extend(do_cmd(cmd))

def do_cmd(cmd):
    exs = get(param, cmd, [""])
    e = list(exs)
    random.shuffle(e)
    events = []
    nr = 0
    for ex in e:
        nr += 1
        txt = cmd + " " + ex 
        if "-v" in sys.argv:
            print(txt)
        e = Event()
        e.otxt = e.txt = txt
        k.queue.put(e)
        events.append(e)
    return events
