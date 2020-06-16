from gtts import gTTS
import os
myVoice = gTTS (lang='en',text='MY Name is adesh vinod datir From Anjangaon Surji Dist. Amravati I Learn In Bca At Dy Patil International University Akurdi Pune  ',slow=False)
myVoice.save("MyVoice.mp3")
os.system ('MyVoice.mp3')