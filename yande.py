#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import os
import urllib.parse
import urllib.request

regexp = r'''<a class="directlink largeimg" href="([^"]+?)">'''
url1 = 'https://yande.re/post?tags=rating:e&page='
for url2 in range(1,1668):
	url = '%s%d' % (url1 , url2)
	print('当前页面：%s' % url)
	html = urllib.request.urlopen(url).read().decode('utf-8')	#取得页面
	for pic in re.findall(regexp , html):	#图片
		local_path = os.path.join('/home/cui/图片/yande' , urllib.parse.unquote(os.path.basename(pic)).split('?')[0])
		if os.path.exists(local_path):
			print('%s已下载，跳过...' % pic)
			continue
		print('获取图片：%s' % pic)
		response = urllib.request.urlopen(pic)
		if response:
			data = response.read()
			with open(local_path , 'wb') as f:
				f.write(data)
