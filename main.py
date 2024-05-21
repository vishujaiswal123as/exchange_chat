import streamlit as st

from streamlit_option_menu import option_menu

import about, account, home, trending, your_posts ,bot

# st.set_page_config(
#         page_title="Pondering",
# )
import streamlit as st

# Set the page title and icon
st.set_page_config(
    page_title="My Streamlit Appp",
    page_icon="⛈️"
)

# Your Streamlit app code goes here...
st.title("Welcome to My Exchange 😁")

class MultiApp:

    def __init__(self):
        self.apps = []
    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })    

    def run():

        with st.sidebar:
            app = option_menu(
                menu_title='Exchanger',
                options=['Home','Account','Trending','Your Posts','Chat Bot','About'],
                icons=['house-fill','person-circle','trophy-fill','chat-fill','robot','info-circle-fill'],
                menu_icon='chat-text-fill',
                default_index=1,
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
        "icon": {"color": "white", "font-size": "23px"}, 
        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
        "nav-link-selected": {"background-color": "#02ab21"},}
                
                )    

        if app== 'Home':
            home.app()
        elif app== 'Account':
            account.app()
        elif app== 'Trending':
            trending.app()
        elif app== 'About':
            about.app()
        elif app== 'Your Posts':
            your_posts.app()
        elif app== 'Chat Bot':
            bot.bot()
    run()                                         


    