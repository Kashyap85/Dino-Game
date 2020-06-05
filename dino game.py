import pyautogui
from PIL import Image,ImageGrab
import time
from numpy import asarray

def hit(key):
    pyautogui.keyDown(key)

def isCollide(data):
    for i in range(300, 415):
        for j in range(640, 680):
            if data[i, j] < 100:
                return True
    return False

#whitecolor=255
if __name__ == "__main__":
    time.sleep(3)
    hit('up')

    while True:
        image = image = ImageGrab.grab().convert('L')
        data = image.load()
        if isCollide(data):
            hit('up')
        #print(asarray(image))
        #image.show()
