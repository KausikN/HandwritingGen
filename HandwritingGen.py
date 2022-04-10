'''
Library Codes for HandwritingGen
'''

# Imports
import requests
from textblob import TextBlob

# Main Functions
def Text2Handwriting(text, savePath='handwriting.png', color=(0, 0, 0)):
    data = requests.get(
        "https://pywhatkit.herokuapp.com/handwriting?text=%s&rgb=%s,%s,%s" % (text, color[0], color[1], color[2])).content
    file = open(savePath, "wb")
    file.write(data)
    file.close()

def SpellCorrect(text):
    return str(TextBlob(text).correct())

# Driver Code