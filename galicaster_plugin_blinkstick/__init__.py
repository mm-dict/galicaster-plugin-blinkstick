# -*- coding:utf-8 -*-

from . import blinkstick_plugin
from distutils.version import LooseVersion

try:
    import galicaster
except:
    print("Error: Galicaster not found")


def init():
    if LooseVersion(galicaster.__version__) >= LooseVersion("3.0.0"):
        blinkstick_plugin.init()
    else:
        raise Exception("Plugin version mismatch")
