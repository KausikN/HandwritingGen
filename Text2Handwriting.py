'''
Convert text to Handwriting
'''

# Imports
import cv2
import pywhatkit

# Main Functions
def Text2Handwriting(text, savePath='handwriting.png', color=(0, 0, 0)):
    pywhatkit.text_to_handwriting(text, save_to=savePath, rgb=color)

# Driver Code
# Params
text = """
The white fox ran over the brown fence.
However the rabbit ran faster and got out of the fox's sight.
"""

savePath = 'Examples/Example_Handwriting.png'
color = (0, 0, 0)
# Params

# RunCode
Text2Handwriting(text, savePath, color)