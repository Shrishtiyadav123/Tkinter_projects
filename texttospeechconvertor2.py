from gtts import gTTS
import os  #os : it is use coz we use operating system from inside of laptop   

file= open('demo.text','r').read()  #.read : it reads till the end  
language ='en'
output=gTTS(text=file,lang='hi',slow=False)
output.save("output.mp3")

os.system("start output.mp3")
