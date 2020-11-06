# TRIPBOT - 24/7 channel daemon
#
#

__copyright__= "Public Domain"

def mods():
    import os
    return [x[:-3] for x in os.listdir("src") if x.endswith(".py")]

def read():
    return open("README.rst", "r").read()

setup(
    name='tripbot',
    version='1',
    url='https://github.com/bthate/tripbot',
    author='Bart Thate',
    author_email='bthate@dds.nl', 
    description="24/7 channel daemon",
    long_description=read(),
    license='Public Domain',
    zip_safe=False,
    package_dir=["", "src"],
    data_files=['', mods()]
    scripts=["bin/tripbot", "bin/tripbotctl", "bin/tripbotd", "bin/tripbotudp"],
    cmdclass={'install': Install},
    classifiers=['Development Status :: 3 - Alpha',
                 'License :: OSI Approved :: MIT License',
                 'Operating System :: Unix',
                 'Programming Language :: Python',
                 'Topic :: Utilities'
                ]
)
