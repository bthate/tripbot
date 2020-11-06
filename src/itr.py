# TRIPBOT - pure python3 IRC channel bot
#
#

"introspection (int)"

import importlib
import inspect
import pkgutil

from obj import Object
from obl import Ol
from utl import direct

def find_cmds(mod):
    "find commands"
    cmds = Object()
    for key, o in inspect.getmembers(mod, inspect.isfunction):
        if "event" in o.__code__.co_varnames:
            if o.__code__.co_argcount == 1:
                cmds[key] = o
    return cmds

def find_funcs(mod):
    "find full qualifed names of commands"
    funcs = Object()
    for key, o in inspect.getmembers(mod, inspect.isfunction):
        if "event" in o.__code__.co_varnames:
            if o.__code__.co_argcount == 1:
                funcs[key] = "%s.%s" % (o.__module__, o.__name__)
    return funcs

def find_mods(mod):
    "find modules of commands"
    mods = Object()
    for key, o in inspect.getmembers(mod, inspect.isfunction):
        if "event" in o.__code__.co_varnames:
            if o.__code__.co_argcount == 1:
                mods[key] = o.__module__
    return mods

def find_classes(mod):
    "find classes and their full qualified names"
    nms = Ol()
    for _key, o in inspect.getmembers(mod, inspect.isclass):
        if issubclass(o, Object):
            t = "%s.%s" % (o.__module__, o.__name__)
            nms.append(o.__name__, t)
    return nms

def find_class(mod):
    "find module of classes"
    mds = Ol()
    for key, o in inspect.getmembers(mod, inspect.isclass):
        if issubclass(o, Object):
            mds.append(o.__name__, o.__module__)
    return mds

def find_names(mod):
    "find modules of commands"
    tps = Ol()
    for _key, o in inspect.getmembers(mod, inspect.isclass):
        if issubclass(o, Object):
            t = "%s.%s" % (o.__module__, o.__name__)
            tps.append(o.__name__.lower(), t)
    return tps
