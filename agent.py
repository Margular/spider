#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import random

def agent():
    user_agents = []
    with open('/usr/share/sqlmap/txt/user-agents.txt' , 'r') as f:
        for line in f:
            line = line.strip()
            if line and line[0] != '#':
                user_agents.append(line)
    return user_agents

if __name__ == '__main__':
    user_agents = agent()
    parser = argparse.ArgumentParser(description = '从sqlmap库里随机获取user-agent')
    parser.add_argument('number' , help='取回user-agent的数量' , default=1 , type=int , nargs = '?')
    args = parser.parse_args()
    for user_agent in random.sample(user_agents , args.number):
        print(user_agent)
