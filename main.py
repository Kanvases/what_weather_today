from aip import AipSpeech
from tkinter import *
import time
import pyaudio
from getWeather import *
from VoiceRec import *
from AudioPlay import *
import os

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()



def callback():
    #recode/save
    wavPath=os.getcwd()+'/tmp.wav'
    resPath=os.getcwd()+'/res.mp3'
    rec(wavPath)
    res=client.asr(get_file_content(wavPath), 'wav', 16000, {
        'dev_pid': 1536,
    })
    print(res)
    if(res['err_no']==0):
        city=res['result'][0]
        print(city)
        WeatherInfo=Weather(city)
        infoString.set(WeatherInfo)
        result  = client.synthesis(WeatherInfo, 'zh', 1, {'vol': 3})
    else:
        infoString.set('识别失败，请清晰地再说一次。')
        result  = client.synthesis('识别失败，请清晰地再说一次。', 'zh', 1, {'vol': 3})
    if not isinstance(result, dict):
        aud=open(resPath, 'wb')
        aud.write(result)
        aud.close()
        AudioPlay(resPath)


APP_ID = '喵'
API_KEY = '喵'
SECRET_KEY = '喵'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
root=Tk()
root.title("What Weather Today")
root.geometry('400x300')
mainString=StringVar()
mainString.set('按下按钮，说出城市名')
btnString=StringVar()
btnString.set('按下聆听')
infoString=StringVar()
infoString.set(' ')

mainLabel = Label(root, textvariable=mainString, font=("Arial", 12), width=20, height=5)
mainLabel.pack(side=TOP)

mainButton = Button(root,textvariable=btnString,command=callback)
mainButton.pack()

infoLabel = Label(root, textvariable=infoString, font=("Arial", 12), width=30, height=30)
infoLabel.pack()
root.mainloop()



