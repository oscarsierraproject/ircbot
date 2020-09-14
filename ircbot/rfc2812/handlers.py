# -*- coding: utf-8 -*-
from typing import ByteString, Dict

from ircbot.flags import Rfc2812Flags

__author__      = "oscarsierraproject.eu"
__copyright__   = "Copyright 2020, oscarsierraproject.eu"
__license__     = "GNU General Public License 3.0"
__date__        = "13th September 2020"
__maintainer__  = "oscarsierraproject.eu"
__email__       = "oscarsierraproject@protonmail.com"
__status__      = "Development"

def process_msg_001_rpl_welcome(msg: Dict) -> Dict:
    """ Process RFC2812 message RPL_WELCOME, code 001 """
    # Sample:
    # b':tepper.freenode.net 001 NICK :Welcome ... Network NICK\r\n' 
    msg["_reply"]     = ""
    msg["cmd_name"]   = "RPL_WELCOME"
    return msg

def process_msg_002_rpl_yourhost(msg: Dict) -> Dict:
    """ Process RFC2812 message RPL_YOURHOST, code 002 """
    msg["_reply"]     = ""
    msg["cmd_name"]   = "RPL_YOURHOST"
    return msg

def process_msg_372_rpl_motd(msg: Dict) -> Dict:
    """ Process RFC2812 message RPL_MOTD, code 372 """
    f = Rfc2812Flags()
    if f.RPL_MOTDSTART != True:
        raise Exception("Lost RPL_MOTDSTART command data.")
    if f.RPL_ENDOFMOTD != False:
        raise Exception("Already Received RPL_ENDOFMOTD command.")
    f.RPL_MOTD = True
    msg["_reply"]     = ""
    msg["cmd_name"]   = "RPL_MOTD"
    return msg

def process_msg_375_rpl_motdstart(msg: Dict) -> Dict:
    """ Process RFC2812 message RPL_MOTDSTART, code 375 """
    f = Rfc2812Flags()
    f.RPL_MOTDSTART = True
    f.RPL_ENDOFMOTD = False 
    msg["_reply"]     = ""
    msg["cmd_name"]   = "RPL_MOTDSTART"
    return msg

def process_msg_376_rpl_endofmotd(msg: Dict) -> Dict:
    """ Process RFC2812 message RPL_ENDOFMOTD, code 376 """
    f = Rfc2812Flags()
    f.RPL_ENDOFMOTD = True
    f.ERR_NOMOTD = False
    msg["_reply"]     = ""
    msg["cmd_name"]   = "RPL_ENDOFMOTD"
    return msg
