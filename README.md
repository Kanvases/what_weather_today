# what_weather_today
百度语音SDK实现的天气语音交互软件

- python 3.6.3
- 使用时请把aip-python-sdk-2.0.0文件夹放在main.py同级目录
- 依赖包： `pyAudio wave AipSpeech pygame requests os time`
- 识别率极低，是个人工智障┓( ´∀` )┏
- 逻辑：用户按下按钮，说出想要查询的城市名字，如‘北京’或‘北京市’，系统通过库函数将声音录下来，并调用语音识别SDK将这段音频转换成文字，用文字信息去天气网站上请求对应的json数据，将json数据转化为字符串后显示在屏幕上，并调用TTS  SDK将该段文本转换成音频，再通过库函数播放
