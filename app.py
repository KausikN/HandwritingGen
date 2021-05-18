"""
Stream lit GUI for hosting HandwritingGen
"""

# Imports
import streamlit as st
import json

import HandwritingGen

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
SAVEPATH_DEFAULT = 'handwriting.png'


# Repo Based Functions
def text_to_handwriting():
    # Title
    st.header("Convert Text to Handwriting")

    # Load Inputs
    USERINPUT_textcolor_Hex = st.color_picker("Select Text Color")
    if USERINPUT_textcolor_Hex is None: return
    USERINPUT_textcolor_RGB = HandwritingGen.Hex_to_RGB(USERINPUT_textcolor_Hex)

    USERINPUT_text = st.text_area("Enter Text", "Hello World!")
    if USERINPUT_text is None: return

    # Process Inputs on Button Click
    if st.button('Generate Handwriting'):
        HandwritingGen.Text2Handwriting(USERINPUT_text, color=USERINPUT_textcolor_RGB, savePath=SAVEPATH_DEFAULT)

        # Display Outputs
        st.image(SAVEPATH_DEFAULT, use_column_width=True, clamp=True)

def txt_file_to_handwriting():
    # Title
    st.header("Convert Text to Handwriting")

    # Load Inputs
    USERINPUT_textcolor_Hex = st.color_picker("Select Text Color")
    if USERINPUT_textcolor_Hex is None: return
    USERINPUT_textcolor_RGB = HandwritingGen.Hex_to_RGB(USERINPUT_textcolor_Hex)

    USERINPUT_file = st.file_uploader("Upload File", type=['txt'])
    if USERINPUT_file is None: return
    USERINPUT_text = USERINPUT_file.read()

    # Process Inputs on Button Click
    if st.button('Generate Handwriting'):
        HandwritingGen.Text2Handwriting(USERINPUT_text, color=USERINPUT_textcolor_RGB, savePath=SAVEPATH_DEFAULT)

        # Display Outputs
        st.image(SAVEPATH_DEFAULT, use_column_width=True, clamp=True)
    
#############################################################################################################################
# Driver Code
if __name__ == "__main__":
    main()