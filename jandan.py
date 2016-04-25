#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import os
import random
import urllib.request
import urllib.parse
from agent import *

regexp = r'''<img src="(http://(?:ww).+?\.(?:jpg|jpeg|gif))"'''
url1 = 'http://jandan.net/ooxx/page-'
for url2 in range(1804,1805):
    url = '%s%d' % (url1 , url2)	#页面
    print('当前页面：%s' % url)
    html = urllib.request.urlopen(url).read().decode('utf-8')	#取得页面
    for pic in re.findall(regexp , html):	#图片
        local_path = os.path.join('/home/cui/图片/妹子图' , urllib.parse.unquote(os.path.basename(pic)).split('?')[0])
        if os.path.exists(local_path):
            print('%s已下载，跳过...' % pic)
            continue
        print('获取图片：%s' % pic)
        req = urllib.request.Request(pic , headers = {'User-Agent':random.choice(agent())})
        response = urllib.request.urlopen(req)
        if response:
            data = response.read()
            with open(local_path , 'wb') as f:
                f.write(data)
