#-*- coding:utf-8 -*-
import json
import urllib
import sys
import re
from datetime import * 
import time
reload(sys)
sys.setdefaultencoding("utf-8")


city_code = '101020100'

# proxy setting
proxies = {'http': 'http://web-proxy.oa.com:8080'}

url = 'http://www.weather.com.cn/weather1d/%s.shtml' % city_code
#filehandle = urllib.urlopen(lvyou_list_url, proxies=proxies)
filehandle = urllib.urlopen(url)
content = filehandle.read()
#print content

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

fp = open('data/%s.weather'%city_code,'a+')
fp.write('date:%s day:%s day_temperature:%s night:%s,night_temperature:%s\r\n'%(date.today() ,day, day_temperature, night, night_temperature))
