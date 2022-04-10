"""
Stream lit GUI for hosting HandwritingGen
"""

# Imports
import streamlit as st
import json

from HandwritingGen import *

# Main Vars
config = json.load(open('./StreamLitGUI/UIConfig.json', 'r'))

# Main Functions
def main():
    # Create Sidebar
    selected_box = st.sidebar.selectbox(
    'Choose one of the following',
        tuple(
            [config['PROJECT_NAME']] + 
            config['PROJECT_MODES']
        )
    )
    
    if selected_box == config['PROJECT_NAME']:
        HomePage()
    else:
        correspondingFuncName = selected_box.replace(' ', '_').lower()
        if correspondingFuncName in globals().keys():
            globals()[correspondingFuncName]()
 

def HomePage():
    st.title(config['PROJECT_NAME'])
    st.markdown('Github Repo: ' + "[" + config['PROJECT_LINK'] + "](" + config['PROJECT_LINK'] + ")")
    st.markdown(config['PROJECT_DESC'])

    # st.write(open(config['PROJECT_README'], 'r').read())

#############################################################################################################################
# Repo Based Vars
SAVEPATH_DEFAULT = "GeneratedVisualisations/Output.png"

# Util Functions
def Hex_to_RGB(val):
    val = val.lstrip('#')
    lv = len(val)
    return tuple(int(val[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

# Repo Based Functions
def text_to_handwriting():
    # Title
    st.header("Convert Text to Handwriting")

    # Load Inputs
    USERINPUT_textcolor_RGB = Hex_to_RGB(st.color_picker("Select Text Color"))
    USERINPUT_text = st.text_area("Enter Text", "Hello World!")

    USERINPUT_SpellCorrect = st.checkbox("Autocorrect")

    # Process Inputs on Button Click
    if st.button('Generate Handwriting'):
        if USERINPUT_SpellCorrect:
            USERINPUT_text = SpellCorrect(USERINPUT_text)
        Text2Handwriting(USERINPUT_text, color=USERINPUT_textcolor_RGB, savePath=SAVEPATH_DEFAULT)

        # Display Outputs
        st.image(SAVEPATH_DEFAULT, use_column_width=True, clamp=True)

def txt_file_to_handwriting():
    # Title
    st.header("Convert Text to Handwriting")

    # Load Inputs
    USERINPUT_textcolor_RGB = Hex_to_RGB(st.color_picker("Select Text Color"))
    USERINPUT_textData = st.file_uploader("Upload File", type=['txt'])
    USERINPUT_text = "This is some test text!"
    if USERINPUT_textData is not None:
        USERINPUT_text = USERINPUT_textData.read()

    USERINPUT_SpellCorrect = st.checkbox("Autocorrect")

    # Process Inputs on Button Click
    if st.button('Generate Handwriting'):
        if USERINPUT_SpellCorrect:
            USERINPUT_text = SpellCorrect(USERINPUT_text)
        Text2Handwriting(USERINPUT_text, color=USERINPUT_textcolor_RGB, savePath=SAVEPATH_DEFAULT)

        # Display Outputs
        st.image(SAVEPATH_DEFAULT, use_column_width=True, clamp=True)
    
#############################################################################################################################
# Driver Code
if __name__ == "__main__":
    main()