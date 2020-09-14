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
    Singleton._instances = {}  
    yield Rfc2812Flags() 
    Singleton._instances = {}  


@pytest.mark.parametrize( "raw_msg, exp_response, exp_flags",
    [   
        (
            b":barjavel.freenode.net 376 thebot " +\
            b":End of /MOTD command.\r\n",
            {
            "_reply"    : "",
            "params"    : "thebot :End of /MOTD command.",
            "cmd_name"  : "RPL_ENDOFMOTD",
            "cmd"       : "376",
            "prefix"    : "barjavel.freenode.net", 
            },
            {
            "RPL_ENDOFMOTD" : True,
            "ERR_NOMOTD"    : False,
            }
        ),
    ]
)
def test_376_RPL_ENDOFMOTD_msg_processing(raw_msg, exp_response, exp_flags, flags):
    """
    Scenario: Test RPL_ENDOFMOTD message processing
      Given a RPL_ENDOFMOTD message
      Than it MUST be processed and expected dictionary must be returned
    """
    m = msg_preprocessing(raw_msg)
    response = rfc2812_handlers.process_msg_376_rpl_endofmotd(m)
    assert response == exp_response
    assert flags.RPL_ENDOFMOTD == exp_flags["RPL_ENDOFMOTD"]
    assert flags.ERR_NOMOTD == exp_flags["ERR_NOMOTD"]

