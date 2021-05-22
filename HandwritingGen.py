'''
Library Codes for HandwritingGen
'''

# Imports
import requests
from textblob import TextBlob

# Module Functions
def text_to_handwriting(string: str, save_to: str = "pywhatkit.png", rgb: list = [0, 0, 138]) -> None:
    data = requests.get(
        "https://pywhatkit.herokuapp.com/handwriting?text=%s&rgb=%s,%s,%s" % (string, rgb[0], rgb[1], rgb[2])).content
    file = open(save_to, "wb")
    file.write(data)
    file.close()

# Main Functions
def Text2Handwriting(text, savePath='handwriting.png', color=(0, 0, 0)):
    text_to_handwriting(text, save_to=savePath, rgb=color)

def SpellCorrect(text):
    return str(TextBlob(text).correct())

# Driver Code