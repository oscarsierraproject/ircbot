# -*- coding: utf-8 -*-
from typing import ByteString, Dict

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
    # Sample:
    # b':tepper.freenode.net 002 P209M17B :Your host is 
    #    tepper.freenode.net[192.186.157.43/7000], running version
    #    ircd-seven-1.1.9\r\n'
    msg["_reply"]     = ""
    msg["cmd_name"]   = "RPL_YOURHOST"
    return msg
