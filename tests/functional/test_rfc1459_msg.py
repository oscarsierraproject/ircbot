import pytest
#from ircbot import async_irc


"""
_ = [
     b':kornbluth.freenode.net 001 nicktestowynoweg :Welcome to the freenode Internet Relay Chat Network nicktestowynoweg\r\n',
     b':kornbluth.freenode.net 372 nicktestowynoweg :- global notices.\r\n',
     b':kornbluth.freenode.net 372 nicktestowynoweg :-  \r\n'
     b':nicktestowynoweg!~nicktesto@staticline-31-183-217-69.toya.net.pl JOIN #dumygargantula\r\n',
     b':kornbluth.freenode.net MODE #dumygargantula +ns\r\n',
     b':kornbluth.freenode.net 353 nicktestowynoweg @ #dumygargantula :@nicktestowynoweg\r\n',
     b':kornbluth.freenode.net 366 nicktestowynoweg #dumygargantula :End of /NAMES list.\r\n',
     ]
"""
"""
@pytest.mark.parametrize( "msg_input, expected",
    [   
        (b'PING :card.freenode.net\r\n', 
         {"servername":"", "nick":"", "user":"", "host":"", 
          "command":"PING", "params":["card.freenode.net",], "_valid":True} ),
        (b':nicktestowynoweg!~nicktesto@staticline-31-183-217-69.toya.net.pl JOIN #dumygargantula\r\n',
         {"servername":"", "nick":"nicktestowynoweg", "user":"~nicktesto", "host":"staticline-31-183-217-69.toya.net.pl", 
          "command":"JOIN", "params":["#dumygargantula",], "_valid":True} ),
        (b':sebthon!1fb7d945@staticline-31-183-217-69.toya.net.pl PRIVMSG #OscarSierraProject :cze\xc5\x9b\xc4\x87\r\n', 
         {"servername":"", "nick":"sebthon", "user":"1fb7d945", "host":"staticline-31-183-217-69.toya.net.pl", 
          "command":"PRIVMSG", "params":["cześć", ], "_valid":True} ),
    ]
)
"""

#def test_ping_message(msg_input, expected):
#    """
#    Scenario: Test response for PING message
#      Given a ping message 
#      Than it MUST be recognised and processed
#    """
#    assert async_irc.process_rfc1495_msg(msg_input) == expected
         
