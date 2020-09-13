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

""" Testing handler of RFC2812 RPL_WELCOME message handler. RPL_WELCOME is the 
first message sent after client registration. The text used varies widely.
"""

@pytest.mark.parametrize( "raw_msg, expected_response",
    [   
        # Message format from freenode servers
        (
            b":tepper.freenode.net 001 NickName :Welcome to the freenode " +\
            b"Internet Relay Chat Network NickName\r\n", 
            {
            "_reply"    : "",
            "params"    : "NickName :Welcome to the freenode Internet " +\
                          "Relay Chat Network NickName",
            "cmd_name"  : "RPL_WELCOME",
            "cmd"       : "001",
            "prefix"    : "tepper.freenode.net", 
            } 
        ),
        (
            b":beckett.freenode.net 001 <nick> :Welcome to the Internet " +\
            b"Relay Network <nick>!<user>@<host> \r\n",
            {
            "_reply"    : "",
            "params"    : "<nick> :Welcome to the Internet Relay Network " +\
                          "<nick>!<user>@<host>",
            "cmd_name"  : "RPL_WELCOME",
            "cmd"       : "001",
            "prefix"    : "beckett.freenode.net", 
            } 
        ),
    ]
)
def test_001_RPL_WELCOME_msg_processing(raw_msg, expected_response):
    """
    Scenario: Test RPL_WELCOME message processing
      Given a RPL_WELCOME message
      Than it MUST be processed and expected dictionary must be returned
    """
    m = msg_preprocessing(raw_msg)
    response = rfc2812_handlers.process_msg_001_rpl_welcome(m)
    assert response == expected_response
