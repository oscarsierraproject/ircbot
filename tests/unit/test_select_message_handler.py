# -*- coding: utf-8 -*-
import pytest
from unittest import mock

from ircbot import async_irc

__author__      = "oscarsierraproject.eu"
__copyright__   = "Copyright 2020, oscarsierraproject.eu"
__license__     = "GNU General Public License 3.0"
__date__        = "13th September 2020"
__maintainer__  = "oscarsierraproject.eu"
__email__       = "oscarsierraproject@protonmail.com"
__status__      = "Development"

""" Testing message processing function. Verify if based on command code,
a proper handler is executed to process the message. """


@pytest.mark.parametrize("raw_msg",
    [   
        b":tepper.freenode.net 001 NickName :Welcome to the freenode " +\
        b"Internet Relay Chat Network NickName\r\n",
        b":beckett.freenode.net 001 <nick> :Welcome to the Internet " +\
        b"Relay Network <nick>!<user>@<host>\r\n",
    ]
)
@mock.patch("ircbot.rfc2812.handlers.process_msg_001_rpl_welcome")
def test_call_001_rpl_welcome_handler(mock_rfc2812_msg, raw_msg):
    """
    Scenario: Test message processing function with 001 command
      Given a RPL_WELCOME command message
      Than it MUST be recognised and processed by process_msg_001_rpl_welcome
        function.
    """
    m = async_irc.msg_preprocessing(raw_msg)
    async_irc.msg_processing(raw_msg) 
    mock_rfc2812_msg.assert_called_once_with(m)

@pytest.mark.parametrize("raw_msg", [b'PING :verne.freenode.net\r\n', ])
@mock.patch("ircbot.rfc1459.handlers.process_msg_ping")
def test_call_process_msg_ping_handler(mock_rfc1459_msg, raw_msg):
    """
    Scenario: Test message processing function with PING command
      Given a PING command message
      Than it MUST be recognised and processed by process_msg_ping function.
    """
    m = async_irc.msg_preprocessing(raw_msg)
    async_irc.msg_processing(raw_msg) 
    mock_rfc1459_msg.assert_called_once_with(m)
