# TRIPBOT - pure python3 IRC channel bot
#
#

"utilities (utl)"

import importlib
import inspect
import os
import pwd
import sys
import traceback
import types

class ENOCLASS(Exception):

    "is not a class"

stopmarkers = ['python3']

def calledfrom(frame):
    "return the plugin name where given frame occured"
    try:
        filename = frame.f_back.f_code.co_filename
        plugfile = filename.split(os.sep)
        if plugfile:
            mod = []
            for i in plugfile[::-1]:
                mod.append(i)
                if i in stopmarkers: break
            modstr = '.'.join(mod[::-1])[:-3]
            if 'handler_' in modstr: modstr = modstr.split('.')[-1]
    except AttributeError: modstr = None
    del frame
    return modstr

def cdir(path):
    "create directory"
    if os.path.exists(path):
        return
    res = ""
    path2, _fn = os.path.split(path)
    for p in path2.split(os.sep):
        res += "%s%s" % (p, os.sep)
        padje = os.path.abspath(os.path.normpath(res))
        try:
            os.mkdir(padje)
            os.chmod(padje, 0o700)
        except (IsADirectoryError, NotADirectoryError, FileExistsError):
            pass

def direct(name):
    "load a module"
    return importlib.import_module(name, '')

def find_modules(pkgs, skip=None):
    "locate modules"
    modules = []
    for pkg in pkgs.split(","):
        if skip is not None and skip not in pkg:
            continue
        try:
            p = direct(pkg)
        except ModuleNotFoundError:
            continue
        for _key, m in inspect.getmembers(p, inspect.ismodule):
            if m not in modules:
                modules.append(m)
    return modules

def get_exception(txt="", sep=" "):
    "print exception trace"
    exctype, excvalue, tb = sys.exc_info()
    trace = traceback.extract_tb(tb)
    result = []
    for elem in trace:
        if elem[0].endswith(".py"):
            plugfile = elem[0][:-3].split(os.sep)
        else:
            plugfile = elem[0].split(os.sep)
        pp = os.sep.join(plugfile)
        if "python3" in pp or "<frozen" in pp:
            continue
        mod = []
        for element in plugfile[::-1]:
            if "triple" in element:
                break
            mod.append(element)
        ownname = ".".join(mod[::-1])
        result.append("%s:%s" % (ownname, elem[1]))
    res = "%s %s: %s %s" % (sep.join(result), exctype, excvalue, str(txt))
    del trace
    return res

def get_name(o):
    "return fully qualified name of an object"
    t = type(o)
    if t == types.ModuleType:
        return o.__name__
    try:
        n = "%s.%s" % (o.__self__.__class__.__name__, o.__name__)
    except AttributeError:
        try:
            n = "%s.%s" % (o.__class__.__name__, o.__name__)
        except AttributeError:
            try:
                n = o.__class__.__name__
            except AttributeError:
                n = o.__name__
    return n

def get_type(o):
    "return type of an object"
    t = type(o)
    if t == type:
        try:
            return "%s.%s" % (o.__module__, o.__name__)
        except AttributeError:
            pass
    return str(type(o)).split()[-1][1:-2]

def list_files(wd):
    "list files in directory"
    path = os.path.join(wd, "store")
    if not os.path.exists(path):
        return ""
    return " ".join(os.listdir(path))

def locked(l):
    "lock descriptor"
    def lockeddec(func, *args, **kwargs):
        def lockedfunc(*args, **kwargs):
            l.acquire()
            res = None
            try:
                res = func(*args, **kwargs)
            finally:
                l.release()
            return res
        lockeddec.__doc__ = func.__doc__
        return lockedfunc
    return lockeddec

def privileges(name):
    "lower privileges"
    if os.getuid() != 0:
        return
    pwnam = pwd.getpwnam(name)
    os.setgroups([])
    os.setgid(pwnam.pw_gid)
    os.setuid(pwnam.pw_uid)
    old_umask = os.umask(0o22)

def root():
    "check if root"
    if os.geteuid() != 0:
        return False
    return True

def spl(txt):
    "return comma splitted values"
    return iter([x for x in txt.split(",") if x])

def touch(fname):
    "touch a file"
    try:
        fd = os.open(fname, os.O_RDWR | os.O_CREAT)
        os.close(fd)
    except (IsADirectoryError, TypeError):
        pass

def callstack(frame):
    "return callstack trace as a string"
    result = []
    loopframe = frame
    marker = ""
    while 1:
        try:
            filename = loopframe.f_back.f_code.co_filename
            plugfile = filename.split(os.sep)
            if plugfile:
                mod = []
                for i in plugfile[::-1]:
                    mod.append(i)
                    if i in stopmarkers:
                         marker = i ; break
                modstr = '.'.join(mod[::-1])[:-3]
                if 'python3' in modstr:
                    modstr = modstr.split('.')[-1]
                if not modstr:
                    modstr = plugfile
            result.append("%s:%s" % (modstr, loopframe.f_back.f_lineno))
            loopframe = loopframe.f_back
        except: break
    del frame
    return result

def where():
    return callstack(sys._getframe(0))
