import requests
import json
def Weather(city):
    if(city[-1]=='市'):
        city=city[0:-1]
    res=requests.get('http://wthrcdn.etouch.cn/weather_mini?city='+city)
    res.encoding='utf-8'
    tmpjson = json.loads(res.text)
    #print(tmpjson)
    if(tmpjson['desc']=="OK"):
        weatherStr=(tmpjson['data']['city']+'\n 11月'+tmpjson['data']['forecast'][0]['date']+'\n'+tmpjson['data']['forecast'][0]['type']+'\n'+ \
        tmpjson['data']['forecast'][0]['high']+' '+tmpjson['data']['forecast'][0]['low']+'\n'+ \
        tmpjson['data']['forecast'][0]['fengxiang']+' '+tmpjson['data']['forecast'][0]['fengli'][9:-3])
        print(weatherStr)
        return weatherStr
    else:
        print('找不到该城市：'+city)
        return ('找不到该城市：'+city)
def main():
    Weather('北京')
    Weather('北京市')
    Weather('哈哈')

if __name__ == '__main__':
    main()
