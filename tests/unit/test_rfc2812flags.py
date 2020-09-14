# -*- coding: utf-8 -*-

__author__      = "oscarsierraproject.eu"
__copyright__   = "Copyright 2020, oscarsierraproject.eu"
__license__     = "GNU General Public License 3.0"
__date__        = "14th September 2020"
__maintainer__  = "oscarsierraproject.eu"
__email__       = "oscarsierraproject@protonmail.com"
__status__      = "Development"

import pytest
from ircbot.flags import Rfc2812Flags

def test_rfc2812_flags_setter_and_getter():
    """
    Scenario: Test Rfc2812Flags class instance
      Given a Rfc2812Flags class instance
      Than it MUST be possible to set and get random attributes.
    """
    f = Rfc2812Flags()
    assert(f.RPL_MOTDSTART == None)
    f.RPL_MOTDSTART = False
    assert(f.RPL_MOTDSTART == False)
    f.RPL_MOTDSTART = True
    assert(f.RPL_MOTDSTART == True)

def test_rfc2812_flags_is_singleton():
    """
    Scenario: Test Rfc2812Flags class instances
      Given a two Rfc2812Flags class instances
      Than all the time both must return the same value for given field
    """
    f1 = Rfc2812Flags()
    f2 = Rfc2812Flags()
    assert(id(f1)==id(f2))
    assert(f1.RPL_ENDOFMOTD == None)
    assert(f1.RPL_ENDOFMOTD == f2.RPL_ENDOFMOTD)
    f1.RPL_ENDOFMOTD = False
    assert(f2.RPL_ENDOFMOTD == False)
    assert(f1.RPL_ENDOFMOTD == f2.RPL_ENDOFMOTD)
    f2.RPL_ENDOFMOTD = True
    assert(f1.RPL_ENDOFMOTD == True)
    assert(f1.RPL_ENDOFMOTD == f2.RPL_ENDOFMOTD)
