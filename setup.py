# TRIPBOT - pure python3 IRC channel bot
#
#

from setuptools import setup

def mods():
    import os
    return [x.split(os.sep)[-1][:-3] for x in os.listdir(os.getcwd()) if x.endswith(".py")]

def read():
    return open("README.rst", "r").read()

setup(
    name='tripbot',
    version='1',
    url='https://github.com/bthate/tripbot',
    author='Bart Thate',
    author_email='bthate@dds.nl', 
    description="pure python3 IRC channel bot",
    long_description=read(),
    zip_safe=False,
    py_modules=mods(),
    scripts=["bin/tripbot"],
    classifiers=['Development Status :: 3 - Alpha',
                 'Operating System :: Unix',
                 'Programming Language :: Python',
                 'Topic :: Utilities'
                ]
)
