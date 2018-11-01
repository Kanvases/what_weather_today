# what_weather_today
百度语音SDK实现的天气语音交互软件

- python 3.6.3
- ~~使用时请把aip-python-sdk-2.0.0文件夹放在main.py同级目录~~
- 依赖包： ` tkinter pyAudio wave AipSpeech pygame requests json`
- 识别率极低，是个人工智障┓( ´∀` )┏
- 逻辑：用户按下按钮，说出想要查询的城市名字，如‘北京’或‘北京市’，系统通过库函数将声音录下来，并调用语音识别SDK将这段音频转换成文字，用文字信息去天气网站上请求对应的json数据，将json数据转化为字符串后显示在屏幕上，并调用TTS  SDK将该段文本转换成音频，再通过pygame播放

---
### 更新信息：

- 谁能想象，我居然改善了这个玩意的UI界面
- 放弃了中国气象网的接口，改用万年历的接口
- 所以删除了转换城市ID的部分
- 因为tkinter不支持的透明背景的lebel，窗口背景采用了一种曲线救国的思路，可以看下`./images/`里面的背景图片

