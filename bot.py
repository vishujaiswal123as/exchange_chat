import streamlit as st
from groq import Groq

from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os
from rembg import remove
from PIL import Image
import os
import random
            

load_dotenv()

groq_api_key = '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'


def remove_background():
    st.header('Upload Your image for removing background')

    def remove_background_with_rembg(image_path, output_path):
        # Load the image
        input_image = Image.open(image_path)

        # Remove the background
        output_image = remove(input_image)

        # Save the output image
        output_image.save(output_path)
        st.write('Feel free to ask me anything...')
        return output_path

    # Usage
    user_image = st.file_uploader(
        'Upload Image here', type=['png', 'jpg', 'jpeg'])
    if user_image:
        output_path = remove_background_with_rembg(user_image, "output.png")

        if os.path.exists(output_path):
            st.write("Background removed successfully!")
            with open(output_path, "rb") as file:
                st.download_button(label="Download image", data=file,
                                   file_name="my.png", mime="image/png")
        else:
            st.write("Error: The output image does not exist.")


def bot():
    user_question=st.text_area('Type Your Query Here').lower()
    model='mixtral-8x7b-32768'
    
    # Add customization options to the sidebar

    conversational_memory_length = st.sidebar.slider(
        'Conversational memory length:', 1, 10, value=5)

    memory = ConversationBufferWindowMemory(k=conversational_memory_length)
    if user_question == 'what is my name' or user_question == "what's my name":
        st.write('Your name is vishal')
    elif user_question == 'who made you' or user_question == 'who makes you' or user_question == "who make's you" or user_question == "who developed you" or user_question == "who created you" or user_question == "who creates you":
        l=['i am developed by vishal','i am made and developed by vishal','i am created by vishal']
        st.write(l[random.randint(0,2)])
    elif 'remove background' == user_question or 'background remover' == user_question or'background remove' == user_question:
        remove_background()
    # session state variable
    else:
        if 'chat_history' not in st.session_state:
            st.session_state.chat_history = []
        else:
            for message in st.session_state.chat_history:
                memory.save_context({'input': message['human']}, {
                                    'output': message['AI']})

        # Initialize Groq Langchain chat object and conversation
        groq_chat = ChatGroq(
            groq_api_key=groq_api_key,
            model_name=model
        )

        conversation = ConversationChain(
            llm=groq_chat,
            memory=memory
        )

        if user_question:
            response = conversation(user_question)
            message = {'human': user_question, 'AI': response['response']}
            st.session_state.chat_history.append(message)
            st.write("Chatbot:", response['response'])
# bot()
