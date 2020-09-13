# -*- coding: utf-8 -*-

__author__      = "oscarsierraproject.eu"
__copyright__   = "Copyright 2020, oscarsierraproject.eu"
__license__     = "GNU General Public License 3.0"
__date__        = "13th September 2020"
__maintainer__  = "oscarsierraproject.eu"
__email__       = "oscarsierraproject@protonmail.com"
__status__      = "Development"

import pytest
from ircbot.async_irc import msg_preprocessing
from ircbot.rfc2812 import handlers as rfc2812_handlers

""" Testing handler of RFC2812 RPL_YOURHOST message handler. RPL_YOURHOST is the 
part of the post-registration greeting. The text used varies widely.
"""

@pytest.mark.parametrize( "raw_msg, expected_response",
    [   
        # Message format from freenode servers
        (
            b":tepper.freenode.net 002 P209M17B :Your host is " +
            b"tepper.freenode.net[192.186.157.43/7000], running " +
            b"version ircd-seven-1.1.9\r\n",
            {
            "_reply"    : "",
            "params"    : "P209M17B :Your host is tepper.freenode.net" +\
                          "[192.186.157.43/7000], running version " +\
                          "ircd-seven-1.1.9",
            "cmd_name"  : "RPL_YOURHOST",
            "cmd"       : "002",
            "prefix"    : "tepper.freenode.net", 
            } 
        ),
    ]
)
def test_002_RPL_YOURHOST_msg_processing(raw_msg, expected_response):
    """
    Scenario: Test RPL_YOURHOST message processing
      Given a RPL_YOURHOST message
      Than it MUST be processed and expected dictionary must be returned
    """
    m = msg_preprocessing(raw_msg)
    response = rfc2812_handlers.process_msg_002_rpl_yourhost(m)
    assert response == expected_response
