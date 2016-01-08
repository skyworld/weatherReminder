#-*- coding:utf-8 -*-
import urllib,sys,re,time
from datetime import date

city_code = '101020100'
proxies = {'http': 'http://web-proxy.oa.com:8080'}

# 如果失败了，至少尝试10次，保证一定能爬取到响应的信息
has_error = True
try_cnt = 0

while has_error == True and try_cnt < 10:
	try:
		url = 'http://www.weather.com.cn/weather1d/%s.shtml' % city_code
		#filehandle = urllib.urlopen(url, proxies=proxies)
		filehandle = urllib.urlopen(url)
		content = filehandle.read()
		pt = re.compile(r'<p class="wea" title="(.*?)">.*?</p>',re.S)
		match = pt.findall(content)
		#print match
		day = match[0]
		night = match[1]

		pt = re.compile(r'<span>(\d+)</span><em>°C</em>',re.S)
		match = pt.findall(content)
		day_temperature = match[0]
		night_temperature = match[1]
		print ('day:%s day_temperature:%s night:%s,night_temperature:%s'%(day, day_temperature, night, night_temperature))
		fp = open('%s/data/%s.weather'%(sys.path[0],city_code),'a+')
		fp.write('date:%s day:%s day_temperature:%s night:%s,night_temperature:%s\r\n'%(date.today() ,day, day_temperature, night, night_temperature))
		fp.close()
		has_error = False
	except Exception , e:
		print e
		time.sleep(10)
		try_cnt = try_cnt + 1
