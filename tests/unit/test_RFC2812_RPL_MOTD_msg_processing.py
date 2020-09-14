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
    flags = Rfc2812Flags() 
    flags.RPL_MOTDSTART = True
    flags.RPL_ENDOFMOTD = False
    yield flags
    Singleton._instances = {}  


@pytest.mark.parametrize( "raw_msg, exp_response, exp_flags",
    [   
        (
            b":barjavel.freenode.net 372 thebot " +\
            b":- Welcome to barjavel.freenode.net in Paris, FR, EU. \r\n",
            {
            "_reply"    : "",
            "params"    : "thebot :- Welcome to barjavel.freenode.net " +\
                          "in Paris, FR, EU.",
            "cmd_name"  : "RPL_MOTD",
            "cmd"       : "372",
            "prefix"    : "barjavel.freenode.net", 
            },
            {
            "RPL_MOTDSTART" : True,
            "RPL_MOTD"      : True,
            "RPL_ENDOFMOTD" : False,
            }
        ),
    ]
)
def test_372_RPL_MOTD_msg_processing(raw_msg, exp_response, exp_flags, flags):
    """
    Scenario: Test RPL_MOTD message processing
      Given a RPL_MOTD message
      Than it MUST be processed and expected dictionary must be returned
    """
    m = msg_preprocessing(raw_msg)
    response = rfc2812_handlers.process_msg_372_rpl_motd(m)
    assert response == exp_response
    assert flags.RPL_MOTDSTART == exp_flags["RPL_MOTDSTART"]
    assert flags.RPL_MOTD == exp_flags["RPL_MOTD"]
    assert flags.RPL_ENDOFMOTD == exp_flags["RPL_ENDOFMOTD"]

@pytest.mark.parametrize( "raw_msg",
                          [ b":barjavel.freenode.net 372 thebot " +\
                            b":- Welcome to barjavel.freenode.net in Paris, "+\
                            b"FR, EU. \r\n",])
def test_372_RPL_MOTD_msg_exceptions(raw_msg, flags):
    """
    Scenario: Test RPL_MOTD message processing
      Given a RPL_MOTD message
      Than it MUST be processed and expected dictionary must be returned
    """
    flags.RPL_MOTDSTART = False
    flags.RPL_ENDOFMOTD = False
    m = msg_preprocessing(raw_msg)
    with pytest.raises(Exception):
        response = rfc2812_handlers.process_msg_372_rpl_motd(m)
    flags.RPL_MOTDSTART = True
    flags.RPL_ENDOFMOTD = True
    with pytest.raises(Exception):
        response = rfc2812_handlers.process_msg_372_rpl_motd(m)
