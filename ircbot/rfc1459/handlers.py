# -*- coding: utf-8 -*-

__author__      = "oscarsierraproject.eu"
__copyright__   = "Copyright 2020, oscarsierraproject.eu"
__license__     = "GNU General Public License 3.0"
__date__        = "13th September 2020"
__maintainer__  = "oscarsierraproject.eu"
__email__       = "oscarsierraproject@protonmail.com"
__status__      = "Development"

from typing import ByteString, Dict

def process_msg_ping(msg: Dict) -> Dict:
    """ Process RFC2812 message RPL_WELCOME, code 001 """
    # Sample:
    # b'PING :orwell.freenode.net\r\
    msg["_reply"]     = "PONG {}".format(msg["params"])
    msg["cmd_name"]   = "PING"
    return msg
