>天气提醒小工具

**说明**


spider.py 为天气信息爬虫小工具，每天从中国天气信息网爬取信息，你可以修改代码中的city_code获取指定的城市的天气信息。可设置为每天早上7点钟爬取一次，爬取的数据将会入到data/*.weather的文件里


analyzer.py 为天气分析小工具，会读取data/*.weather的文件昨天和今天的天气信息进行比对，具体的分析规则见代码


webserver.py 为对外提供信息的web服务，运行在8888端口，通过该接口，你可以把你的短信、微博等提醒相关的内容放在其他任意第三方服务器上。 webserver.py需要作为daemon程序运行。访问地址：http://domain.com:8888/get 并且返回会的数据如下

```
// 有需要提醒的消息
{
	code: "0",
	msg: "明天会有雨哦，记得带伞出门，并且明天会有大幅降温哦，记得多穿一点，别着凉感冒了！by 爱你的XXXX n(*≧▽≦*)n",
	data: ""
}

// 无需要提醒的消息
{
	code: "-2",
	msg: "no thing to remind",
	data: ""
}

// 不合法的访问
{
	code: "-1",
	msg: "Access Denied",
	data: ""
}
```