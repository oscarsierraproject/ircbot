#!/usr/bin/env python3
# -*- coding: 'utf-8' -*-

__author__      = "oscarsierraproject.eu"
__copyright__   = "Copyright 2020, oscarsierraproject.eu"
__license__     = "GNU General Public License 3.0"
__date__        = "13th September 2020"
__maintainer__  = "oscarsierraproject.eu"
__email__       = "oscarsierraproject@protonmail.com"
__status__      = "Development"

import asyncio
from ircbot import config
import signal
import time
from typing import ByteString, Dict

from ircbot.flags import Rfc2812Flags
from ircbot.rfc1459 import handlers as rfc1459_handlers
from ircbot.rfc2812 import handlers as rfc2812_handlers

config.init_logging()


def msg_preprocessing(raw_msg: ByteString) -> Dict:
    """ Covert message from byte string into pre filled dictionary """
    # <message>  ::= [':' <prefix> <SPACE> ] <command> <params> <crlf>
    if raw_msg[-2:] != b"\r\n":
        raise ValueError("Error: missing CRLF!")
    msg_decoded     = raw_msg.decode()
    if "PING" == msg_decoded[0:4:]:
        msg_list        = msg_decoded.split()
        return { "_reply"   : "", 
                 "cmd"      : msg_list[0],
                 "params"   : " ".join(msg_list[1::]),
                 "prefix"   : "", }
    else:
        msg_list        = msg_decoded[1::].split()
        return { "_reply"   : "", 
                 "cmd"      : msg_list[1], 
                 "params"   : " ".join(msg_list[2::]),
                 "prefix"   : msg_list[0], }

def msg_processing(raw_msg):
    """ Extract RFC1459, and RFC2812 messages fields """
    _msg = msg_preprocessing(raw_msg)
    msg_handlers = {
        "001": rfc2812_handlers.process_msg_001_rpl_welcome,
        "002": rfc2812_handlers.process_msg_002_rpl_yourhost,
        "372": rfc2812_handlers.process_msg_372_rpl_motd,
        "375": rfc2812_handlers.process_msg_375_rpl_motdstart,
        "376": rfc2812_handlers.process_msg_376_rpl_endofmotd,
        "PING": rfc1459_handlers.process_msg_ping
    }
    if _msg["cmd"] in msg_handlers.keys():
        _msg = msg_handlers[_msg["cmd"]](_msg)
    print(raw_msg)
    return _msg
        
async def receiver(reader, queue):
    """ Listen to data, make basic cleanup and put it in incoming queue"""
    while True:
        data = await reader.readline()
        await queue.put(msg_processing(data))

async def responser(writer, queue):
    """ Pick data from messages queue, analyze it and send response """
    await asyncio.sleep(5)  # Let's wait a while before sending data
    while True:
        msg = await queue.get()
        if not isinstance(msg, dict):
            raise TypeError("Message in queue must be dictionary")
        if msg["_reply"] != "" and isinstance(msg["_reply"], str):
            writer.write(bytes(msg["_reply"], "utf-8") + b"\r\n")
        elif msg["_reply"] != "" and isinstance(msg["_reply"], bytes):
            writer.write(msg["_reply"])
        await writer.drain()
        queue.task_done()
        continue

async def connect(msg_queue):
    reader, writer = await asyncio.open_connection(
                                host=config.IRC_NETWORKS["freenode"]["host"], 
                                port=config.IRC_NETWORKS["freenode"]["port"], 
                                ssl =config.IRC_NETWORKS["freenode"]["ssl"])
    return (reader, writer)

async def setup_connection(msg_queue):
    _msg = {}
    _msg["_reply"] = "NICK {}\r\n"\
                     .format(config.IRC_NETWORKS["freenode"]["nickname"])\
                     .encode("utf-8")
    await msg_queue.put(_msg)
    _msg = {}
    _msg["_reply"] = "USER {} * * {}\r\n"\
                     .format(config.IRC_NETWORKS["freenode"]["nickname"],\
                             config.IRC_NETWORKS["freenode"]["user_map"]["Bot"])\
                     .encode("utf-8")
    await msg_queue.put(_msg)
    # @TODO: Don't try to JOIN channels unless RPL_ENDOFMOTD is received 
    f = Rfc2812Flags()
    while(f.RPL_ENDOFMOTD!=True and f.ERR_NOMOTD!=False):
        await asyncio.sleep(3)
    for ch in config.IRC_NETWORKS["freenode"]["channels"]:
        _msg = {}
        _msg["_reply"] = "JOIN {}\r\n".format(ch).encode("utf-8") 
        await msg_queue.put(_msg)

async def main():
    def signal_SIGINT_handler(sig, frame):
        print('Close the connection')
        writer.close()
        import sys
        sys.exit(0)
    signal.signal(signal.SIGINT, signal_SIGINT_handler)
    msg_queue  = asyncio.Queue(maxsize=1024)
    (reader, writer) = await connect(msg_queue)
    await asyncio.gather(   setup_connection(msg_queue),
                            receiver(reader, msg_queue),
                            responser(writer, msg_queue), )
    # You will ever reach this point
