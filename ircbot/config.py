#/usr/bin/env python
# *-* coding: utf-8 *-*

__author__      = "oscarsierraproject.eu"
__copyright__   = "Copyright 2020, oscarsierraproject.eu"
__license__     = "GNU General Public License 3.0"
__date__        = "13th September 2020"
__maintainer__  = "oscarsierraproject.eu"
__email__       = "oscarsierraproject@protonmail.com"
__status__      = "Development"

import logging
import logging.config

# VARIABLES --------------------------------------------------------------------
IRC_CONFIG = {
    "reconnect_timeout": 5.0,       # Seconds
    "ctrl_th_sleep": 0.1,           # Seconds
    "sender_th_sleep": 0.2,         # Seconds
    "data_handle_th_sleep": 0.2,    # Seconds
}
IRC_NETWORKS = {
    "freenode": {
        "host": "irc.freenode.net",
        "port": 6697,
        "ssl": True,
        "nickname": "theoscarsierrabot",
        "channels": {
            "#oscarsierraproject": {}
        },
        "user_map": {
            "Bot": "TheRealName"
        }
    }
}

# METHODS ----------------------------------------------------------------------
def init_logging():
    # Setup logging facility to imrove execution readability
    logging_level  = logging.DEBUG
    logging_config = dict(
        version = 1,
        formatters = {
            'f': {  'format':
                    '%(asctime)s | %(levelname)8s | %(message)s | %(name)s'
            },
        },
        handlers = {
            'h': {  'class': 'logging.StreamHandler',
                    'formatter': 'f',
                    'level': logging_level,
            },
        },
        root = {
            'handlers': ['h'],
            'level': logging_level,
        },
    )
    logging.config.dictConfig(logging_config)
    root_logger = logging.getLogger()   # Global for the script
def __TestConfig():
  for network, cfg in IRC_NETWORKS.items():
    assert type(cfg["host"]) is str
    assert type(cfg["port"]) is int
    assert type(cfg["ssl"]) is bool
# MAIN -------------------------------------------------------------------------
if __name__ == "__main__":
  __TestConfig()
 
