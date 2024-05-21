import streamlit as st

def app():
    st.subheader('Trending')
    col1,col2,=st.columns(2)
    
    with col1:
     st.image('penguin.png.jpg')
    with col2:
     st.image('R.jpg')