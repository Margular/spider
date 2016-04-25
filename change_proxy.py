#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import socks
import socket
import urllib.request

def change_proxy(proxy = None):
    if proxy is None:
        with open('proxy.txt' , 'r') as f:
            proxies = f.read().split('\n')
            proxy = random.choice(proxies)
    [host , protocol] = proxy.split('@')
    #安装代理
    if protocol == 'socks4':
        [ip , port] = host.split(':')
        socks.set_default_proxy(socks.SOCKS4 ,ip , int(port))
        socket.socket = socks.socksocket
    elif protocol == 'socks5':
        [ip , port] = host.split(':')
        socks.set_default_proxy(socks.SOCKS5 ,ip , int(port))
        socket.socket = socks.socksocket
    else: 
        proxy_support = urllib.request.ProxyHandler({protocol : host})
        opener = urllib.request.build_opener(proxy_support)
        urllib.request.install_opener(opener)
    return (protocol , host)
