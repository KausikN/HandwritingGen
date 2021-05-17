'''
Library Codes for HandwritingGen
'''

# Imports
import cv2
import requests

# Module Functions
def text_to_handwriting(string: str, save_to: str = "pywhatkit.png", rgb: list = [0, 0, 138]) -> None:
    data = requests.get(
        "https://pywhatkit.herokuapp.com/handwriting?text=%s&rgb=%s,%s,%s" % (string, rgb[0], rgb[1], rgb[2])).content
    file = open(save_to, "wb")
    file.write(data)
    file.close()

# Util Functions
def Hex_to_RGB(val):
    val = val.lstrip('#')
    lv = len(val)
    return tuple(int(val[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def ReadImage(path='handwriting.png'):
    return cv2.imread(path)

# Main Functions
def Text2Handwriting(text, savePath='handwriting.png', color=(0, 0, 0)):
    text_to_handwriting(text, save_to=savePath, rgb=color)

# Driver Code