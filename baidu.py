#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import os
import urllib.parse
import urllib.request
import random
from agent import *

regexp = r'''"objURL":"(http://[^"]+?)"'''
url1 = 'http://image.baidu.com/search/flip?tn=baiduimage&word=' + urllib.parse.quote('仓木麻衣')
url2 = '&pn='
for url3 in range(1920,3600,60):		    
    url = '%s%s%d' % (url1 , url2 , url3)	#页面
    print('当前页面：%s' % url)
    html = urllib.request.urlopen(url).read().decode('utf-8')	#取得页面
    for pic in re.findall(regexp , html):	#图片
        local_path = os.path.join('/home/cui/图片/仓木麻衣' , urllib.parse.unquote(os.path.basename(pic)).split('?')[0])
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
