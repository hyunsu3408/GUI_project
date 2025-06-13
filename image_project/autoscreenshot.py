from PIL import ImageGrab
import time

time.sleep(3) # 5초 대기

for i in range(1,11):
    img = ImageGrab.grab() # 현재 스크린 이미지를 가져옴
    img.save("image{}.png".format(i)) # 파일로 저장(image1.png~ image10.png)
    time.sleep(2)
    
