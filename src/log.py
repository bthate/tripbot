# TRIPBOT - pure python3 IRC channel bot
#
#

"log module"

import logging, logging.handlers, os, os.path, getpass

LEVELS = {
          'debug': logging.DEBUG,
          'info': logging.INFO,
          'warning': logging.WARNING,
          'warn': logging.WARNING,
          'error': logging.ERROR,
          'critical': logging.CRITICAL
         }

RLEVELS = {
           logging.DEBUG: 'debug',
           logging.INFO: 'info',
           logging.WARNING: 'warn',
           logging.ERROR: 'error',
           logging.CRITICAL: 'critical'
          }

datefmt = '%H:%M:%S'
logdir = "/var/log/tripbot"
logformat = "%(asctime)-8s %(message)-72s"

def level(name):
    "set loglevel"
    level = LEVELS.get(name, logging.NOTSET)
    root = logging.getLogger()
    root.setLevel(level)
    if root and root.handlers:
        for handler in root.handlers:
            root.removeHandler(handler)
    formatter = logging.Formatter(logformat, datefmt=datefmt)
    #filehandler = logging.handlers.TimedRotatingFileHandler(os.path.join(logdir, "tripbot.log"), 'midnight')
    #filehandler.setFormatter(formatter)
    ch = logging.StreamHandler()
    ch.setLevel(level)
    ch.setFormatter(formatter)
    root.addHandler(ch)

def getloglevel():
    root = logging.getLogger()
    return RLEVELS.get(root.level)
