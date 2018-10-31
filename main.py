from aip import AipSpeech
from tkinter import *
from PIL import Image, ImageTk
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
        infoString.set('识别失败\n请清晰地再说一次。')
        result  = client.synthesis('识别失败,请清晰地再说一次。', 'zh', 1, {'vol': 3})
    if not isinstance(result, dict):
        aud=open(resPath, 'wb')
        aud.write(result)
        aud.close()
        AudioPlay(resPath)


APP_ID = ''
API_KEY = ''
SECRET_KEY = ''

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
root=Tk()
root.title("What Weather Today")
root.geometry('400x600')
mainString=StringVar()
mainString.set('按下按钮，说出城市名')
btnString=StringVar()
btnString.set('按下聆听')
infoString=StringVar()
infoString.set(' ')

image = Image.open("./images/Artboard.png") 
photo = ImageTk.PhotoImage(image)
bkLabel=Label(root,image=photo)
bkLabel.place(x=0,y=0,relwidth=1, relheight=1) 



photo1 = ImageTk.PhotoImage(image)
mainLabel = Label(root, textvariable=mainString,compound='center',image=photo1,font=("Arial", 15),fg='white')
mainLabel.place(x=125,y=20,width=150,height=50)
photo2 = ImageTk.PhotoImage(file='./images/2.gif')
infoLabel = Label(root, textvariable=infoString,compound='center',image=photo2, font=("Arial", 15),fg='black')
infoLabel.place(x=200,y=300,width=195,height=295)

mainButton = Button(root,textvariable=btnString,command=callback)
mainButton.place(x=155,y=205)



root.mainloop()



