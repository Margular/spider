#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import os
import urllib.parse
import urllib.request

regexp = r'''<a id="btn-download" title="下载原图到电脑" target="_blank" href="([^"]+?)">'''
regexp_next = r'''<a href="([^"]+?)" title="下一张" class="detail-img-next-btn btn">'''
start = ['http://www.chunmm.com/meimei/124-1.html']

for each in start:
    url = each
    while True:
        print('当前页面：%s' % url)
        html = urllib.request.urlopen(url).read().decode('utf-8')   #取得页面
        for pic in re.findall(regexp , html):   #图片
            local_path = os.path.join('/home/cui/图片/纯妹妹' , urllib.parse.unquote(os.path.basename(pic)).split('?')[0])
            if os.path.exists(local_path):
                print('%s已下载，跳过...' % pic)
                continue
            print('获取图片：%s' % pic)
            response = urllib.request.urlopen(pic)
            if response:
                data = response.read()
                with open(local_path , 'wb') as f:
                    f.write(data)

        urls = re.findall(regexp_next , urllib.request.urlopen(url).read().decode('utf-8'))
        if urls == []:
            break
        url = 'http://www.chunmm.com' + urls[0]
