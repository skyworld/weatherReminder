#-*- coding:utf-8 -*-
import urllib,sys,re,time,json
from datetime import date
reload(sys)
sys.setdefaultencoding('utf-8')

city_code = '101020100'
proxies = {'http': 'http://web-proxy.oa.com:8080'}

# 如果失败了，至少尝试10次，保证一定能爬取到响应的信息
has_error = True
try_cnt = 0

while has_error == True and try_cnt < 10:
	try:
		url = 'https://api.heweather.com/x3/weather?cityid=CN%s&key=f02205ac528a4e7d986c4ad8ca4481c3' % city_code
		#filehandle = urllib.urlopen(url, proxies=proxies)
		filehandle = urllib.urlopen(url)
		content = filehandle.read()
		weather = json.loads(content)
		forecasts = weather['HeWeather data service 3.0'][0]['daily_forecast']
		
		for forecast in forecasts:
			if forecast['date'] == str(date.today()):
                		day = forecast['cond']['txt_d']
                		night = forecast['cond']['txt_n']
				day_temperature = forecast['tmp']['max']
                		night_temperature = forecast['tmp']['min']
               		 	print ('day:%s day_temperature:%s night:%s night_temperature:%s'%(day, day_temperature, night, night_temperature))
                		fp = open('%s/data/%s.weather'%(sys.path[0],city_code),'a+')
                		fp.write('date:%s day:%s day_temperature:%s night:%s night_temperature:%s\r\n'%(date.today() ,day, day_temperature, night, night_temperature))
                		fp.close()

			else:
				break
		has_error = False
	except Exception , e:
		print e
		time.sleep(10)
		try_cnt = try_cnt + 1
