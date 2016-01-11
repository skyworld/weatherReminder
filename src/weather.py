#-*- coding:utf-8 -*-
import json,urllib,urllib2,sys
from urllib import urlencode
import time
reload(sys)
sys.setdefaultencoding("utf-8")

# proxy setting
proxies = {'http': 'http://10.14.36.84:8080'}

hasError = True
try_cnt = 0;

while hasError == True and try_cnt < 10:
	try:
		weather_url = 'http://wzc.shnow.cn:8888/get'
		filehandle = urllib.urlopen(weather_url, proxies=proxies)
		content = filehandle.read()
		ret = json.loads(content)
		print ret
		try:
			if ret['code'] == '0':
				paramsDic = {'c':'Skyoption','act':'sms','rec':'188*******;188*******','title':'hi darling', 'content':ret['msg']}
				params = urllib.urlencode(paramsDic) 
				send_url = 'http://p.addev.com/php/daemon/index.php?%s' % params
				req = urllib2.Request(send_url.encode('utf8'))
				req.set_proxy(None,None)
				filehandle = urllib2.urlopen(req)
				content = filehandle.read()
				hasError = False
				print content
		except Exception , e:
			print e
			try_cnt = try_cnt+1
			time.sleep(10)

	except Exception , e:
		print e
		print 'get weather info error!'
		try_cnt = try_cnt+1
		time.sleep(10)


