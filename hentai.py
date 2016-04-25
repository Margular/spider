#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import os
import urllib.parse
import urllib.request
import urllib.error
from change_proxy import *

change_proxy('127.0.0.1:1234@socks5')
regexp = r'''<a href="(http://mobile\.madthumbscdn\.com/videos/[^"]+?)"></a>'''

for each in range(1,1613):
    url = r'http://m.madthumbs.com/hentai?p=%d' % each
    print('当前页面：%s' % url)
    html = urllib.request.urlopen(url).read().decode('utf-8')	#取得页面
    for movie in re.findall(regexp , html):	#图片
        local_path = os.path.join('/home/cui/视频/hentai' , urllib.parse.unquote(os.path.basename(movie)).split('?')[0])
        if os.path.exists(local_path):
            print('%s已下载，跳过...' % movie)
            continue
        print('获取视频：%s' % movie)
        try:
            response = urllib.request.urlopen(movie)
        except urllib.error.URLError as e:
            if hasattr(e , 'code') and e.code == 404:
                print(e)
                continue
        if response:
            data = response.read()
            with open(local_path , 'wb') as f:
                f.write(data)  
