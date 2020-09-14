# -*- coding: utf-8 -*-

__author__      = "oscarsierraproject.eu"
__copyright__   = "Copyright 2020, oscarsierraproject.eu"
__license__     = "GNU General Public License 3.0"
__date__        = "14th September 2020"
__maintainer__  = "oscarsierraproject.eu"
__email__       = "oscarsierraproject@protonmail.com"
__status__      = "Development"

import pytest
from ircbot.async_irc import msg_preprocessing
from ircbot.flags import Rfc2812Flags
from ircbot.rfc2812 import handlers as rfc2812_handlers
from ircbot.singleton import Singleton

@pytest.fixture(scope="module")
def flags():
    yield Rfc2812Flags() 
    Singleton._instances = {}  

@pytest.mark.parametrize( "raw_msg, exp_response, exp_flags",
    [   
        (
            b":barjavel.freenode.net 375 thebot " +\
            b":- barjavel.freenode.net Message of the Day -\r\n",
            {
            "_reply"    : "",
            "params"    : "thebot :- barjavel.freenode.net Message of the Day -",
            "cmd_name"  : "RPL_MOTDSTART",
            "cmd"       : "375",
            "prefix"    : "barjavel.freenode.net", 
            },
            {
            "RPL_MOTDSTART" : True,
            "RPL_ENDOFMOTD" : False,
            }
        ),
    ]
)
def test_375_RPL_MOTDSTART_msg_processing(raw_msg, exp_response, exp_flags, flags):
    """
    Scenario: Test RPL_MOTDSTART message processing
      Given a RPL_MOTDSTART message
      Than it MUST be processed and expected dictionary must be returned
    """
    m = msg_preprocessing(raw_msg)
    response = rfc2812_handlers.process_msg_375_rpl_motdstart(m)
    assert response == exp_response
    assert flags.RPL_MOTDSTART == exp_flags["RPL_MOTDSTART"]
    assert flags.RPL_ENDOFMOTD == exp_flags["RPL_ENDOFMOTD"]
