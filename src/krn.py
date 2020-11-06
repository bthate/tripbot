# TRIPBOT - pure python3 IRC channel bot
#
#

"kernel (krn)"

__version__ = 1

import importlib, os, pkgutil, sys, time, threading
import obj

booted = False
starttime = time.time()
mods = [x[:-3] for x in os.listdir(os.path.dirname(obj.__file__)) 
        if not x.startswith("__") and x.endswith(".py")]

from bus import bus
from cfg import Cfg
from evt import Event
from ldr import Loader
from log import level
from hdl import Handler
from itr import *
from obj import Object, get, update
from prs import parse, parse_cli
from trm import termreset, termsave
from tsk import start
from utl import cdir, direct, get_exception, get_name, spl

class Cfg(Cfg):

    pass

class Kernel(Loader, Handler):

    "kernel class"

    classes = Object()
    cmds = Object()
    funcs = Object()
    mods = Object()
    names = Object()

    def __init__(self):
        super().__init__()
        self.ready = threading.Event()
        self.stopped = False
        self.cfg = Cfg()
        kernels.append(self)

    def announce(self, txt):
        "silence announcing"

    def cmd(self, txt):
        "execute single command"
        if not txt:
            return None
        e = Event()
        e.otxt = txt
        bus.add(self)
        self.dispatch(e)
        return e

    def direct(self, txt):
        "print text"
        print(txt.rstrip())

    def dispatch(self, e):
        "dispatch event"
        e.parse()
        if not e.orig:
            e.orig = repr(self)
        func = self.get_cmd(e.cmd)
        if not func:
            mn = get(self.mods, e.cmd, None)
            if mn:
                spec = importlib.util.find_spec(mn)
                if spec:
                    self.load(mn)
                    func = self.get_cmd(e.cmd)
        if func:
            func(e)
            e.show()
        e.ready.set()

    def get_cmd(self, cmd):
        "return command"
        cmd = cmd.lower()
        if cmd in self.cmds:
             return self.cmds[cmd]
        mn = get(self.mods, cmd, None)
        if not mn:
            return
        mod = None
        if mn in sys.modules:
            mod = sys.modules[mn]
        else:
            spec = importlib.util.find_spec(mn)
            if spec:
                mod = direct(mn)
        if mod:
            return getattr(mod, cmd, None)

    def init(self, mns):
        "call init() of modules"
        if not mns:
            return
        for mn in spl(mns):
            try:
                mod = self.load("triple.%s" % mn)
                self.scan(mod)
                mod.init(self)
            except AttributeError:
                continue
            except Exception as ex:
                print(get_exception()) 

    def say(self, channel, txt):
        "echo to screen"
        self.direct(txt)

    def scan(self, mod):
        "update tables"
        update(self.cmds, find_cmds(mod))
        update(self.funcs, find_funcs(mod))
        update(self.mods, find_mods(mod))
        update(self.names, find_names(mod))
        update(self.classes, find_class(mod))

    def stop(self):
        "stop kernel"
        self.stopped = True
        self.queue.put(None)

    def tabled(self, tbl):
        "initialise with a table"
        update(Kernel.classes, tbl.classes)
        update(Kernel.funcs, tbl.funcs)
        update(Kernel.mods, tbl.mods)
        update(Kernel.names, tbl.names)

    def wait(self):
        "loop forever"
        while not self.stopped:
            time.sleep(60.0)

    def walk(self, pkgname, names):
        "walk over packages and load their modules"
        for name in spl(names):
            mod = self.load("%s.%s" % (pkgname, name))
            self.scan(mod)

#:
kernels = []

def boot(name):
    "set basic paths, read cli options and return kernel"
    k = get_kernel()
    cfg = parse_cli()
    update(k.cfg, cfg)
    wd = obj.wd or k.cfg.wd or os.path.expanduser("~/.triple")
    obj.wd = k.cfg.wd = wd
    cdir(obj.wd)
    cdir(os.path.join(obj.wd, "store", ""))
    sys.path.insert(0, k.cfg.wd)
    import krn
    scandir(os.path.dirname(krn.__file__, "")
    return k

def cmd(txt):
    "execute single command"
    k = get_kernel()
    return k.cmd(txt)

def execute(main):
    "provide context for funcion"
    termsave()
    try:
        main()
    except KeyboardInterrupt:
        print("")
    except PermissionError:
        print("you need root permission.")
    except Exception as ex:
        print(get_exception())
    finally:
        termreset()

def get_kernel():
    "return kernel"
    if kernels:
        return kernels[0]
    return Kernel()

def scandir(path, name):
    "scan a modules directory"
    k = get_kernel()
    cdir(path + os.sep + "")
    for mn in [x[:-3]) for x in os.listdir(path)
                       if x and x.endswith(".py")
                       and not x.startswith("__")]:
        k.scan(k.load(mn))
