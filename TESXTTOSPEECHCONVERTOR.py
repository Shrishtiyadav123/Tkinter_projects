from gtts import gTTS
import os

t="welcome shrishti yadav "
output=gTTS(text=t,lang="en",slow=False)  #which text you want to convert "T" variable ko  slow = false : it means it should not be much slow  
output.save("output.mp3")
os.system("start output.mp3")