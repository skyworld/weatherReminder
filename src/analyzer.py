# -- coding: UTF-8
import re,sys
reload(sys)  
sys.setdefaultencoding('utf8') 

class analyzer:
	
	# 要被分析的数据文件 	
	_dataFile = '';

	# 构造函数，fileName传入要被分析的数据文件
	def __init__(self, fileName):
		self._dataFile = fileName;
	

	# 获取文件倒数N行内容
	def tail(self,f, n, offset=0):
	    avg_line_length = 300
	    to_read = n + offset
	    while 1:
	        try:
	            f.seek(-(avg_line_length * to_read), 2)
	        except IOError:
	            f.seek(0)
	        pos = f.tell()
	        lines = f.read().splitlines()
	        if len(lines) >= to_read or pos == 0:
	            return lines[-to_read:offset and -offset or None]
	        avg_line_length *= 1.3

	# 判断是否有雨
	def hasRain(self, str):
		str = str.encode('utf-8')
		print str.find(u'雨')
		if str.find(u'雨') != -1 or str.find(u'冰雹') != -1 or str.find(u'雷暴') != -1:
			print str
			return True
		else:
			return False

	# 开始分析
	def run(self):
		fp = open(self._dataFile, 'r')
		lastLines = self.tail(fp,2,0)
		#date:2016-01-07 day:阴 day_temperature:10 night:雨,night_temperature:4
		pt = re.compile(r'date:(.*?) day:(.*?) day_temperature:(-{0,1})(\d+) night:(.*?) night_temperature:(-{0,1})(\d+)',re.S)
		yesterdayInfo = pt.findall(lastLines[0])
		todayInfo = pt.findall(lastLines[1])
		
		#print ('yesterdayInfo: %s' % lastLines[0])
		#print ('todayInfo: %s' % lastLines[1])
		
		# 昨天的天气信息
		y_date = yesterdayInfo[0][0]	
		y_day = yesterdayInfo[0][1]
		y_day_temperature_below = yesterdayInfo[0][2]
		y_day_temperature = int(yesterdayInfo[0][3])
		y_night = yesterdayInfo[0][4]
		y_night_temperature_below = yesterdayInfo[0][5]
		y_night_temperature = int(yesterdayInfo[0][6])

		if y_day_temperature_below == '-':
			y_day_temperature = 0 - y_day_temperature

		if y_night_temperature_below == '-':
			y_night_temperature = 0 - y_night_temperature

		# 今天的天气信息
		t_date = todayInfo[0][0]	
		t_day = todayInfo[0][1]
		t_day_temperature_below = todayInfo[0][2]
		t_day_temperature = int(todayInfo[0][3])
		t_night = todayInfo[0][4]
		t_night_temperature_below = todayInfo[0][5]
		t_night_temperature = int(todayInfo[0][6])

		if t_day_temperature_below == '-':
			t_day_temperature = 0 - t_day_temperature

		if t_night_temperature_below == '-':
			t_night_temperature = 0 - t_night_temperature

		
		# 昨天和今天是否下雨
		# 一天白天或者晚上，有一个时刻在下雨就是有雨
		yesterdayHasRain = self.hasRain(y_day) or self.hasRain(y_night)
		todayHasRain = self.hasRain(t_day) or self.hasRain(y_night)

		# 如果昨天没下雨，今天下雨了需要提醒
		# 如果连续下雨，提醒也没啥意义，不提醒了
		rainRemind = (yesterdayHasRain == False and todayHasRain == True)


		# 大幅降温提醒
		maxTempertureDiff = max(y_day_temperature - t_day_temperature,  y_night_temperature - t_night_temperature)
		print maxTempertureDiff

		# 开始处理消息提醒
		msg= {'code':-1,'msg':'nothing to remind'}
		if rainRemind == False and maxTempertureDiff < 4:
			return msg
		else:
			rainRemindStr = '';
			tempertureRemindStr = ''
			if rainRemind == True:
				rainRemindStr = '明天会有雨哦，记得带伞出门'

			if maxTempertureDiff >= 4:
				tempertureRemindStr = '明天会有大幅降温哦，记得多穿一点，别着凉感冒了'

			remindStr = '';
			if rainRemindStr == '' or tempertureRemindStr == '':
				remindStr = rainRemindStr+tempertureRemindStr+'！by 爱你的庚庚 n(*≧▽≦*)n'
			else:
				remindStr = rainRemindStr+'，并且'+tempertureRemindStr+'！by 爱你的庚庚 n(*≧▽≦*)n'
			msg = {'code':0,'msg':remindStr}
			return msg
		
#an = analyzer('data/101020100.weather')
#print an.run();
