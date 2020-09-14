#!/usr/bin/env python3
# -*- coding: 'utf-8' -*-

__author__      = "oscarsierraproject.eu"
__copyright__   = "Copyright 2020, oscarsierraproject.eu"
__license__     = "GNU General Public License 3.0"
__date__        = "14th September 2020"
__maintainer__  = "oscarsierraproject.eu"
__email__       = "oscarsierraproject@protonmail.com"
__status__      = "Development"

from ircbot.singleton import Singleton

class Rfc2812Flags(object, metaclass=Singleton):
    def __init__(self):
        pass
    def __getattribute__(self, flag):
        return super(Rfc2812Flags, self).__getattribute__(flag)
    def __getattr__(self, flag):
        return None
    def __setattr__(self, flag, value):
        self.__dict__[flag] = value
