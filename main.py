import streamlit as st
from streamlit_option_menu import option_menu
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import your application modules
import home
import upload
import about
import remedies

# Set the page configuration
st.set_page_config(page_title="Skin Cancer Detection")

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({"title": title, "function": func})

    def run(self):
        with st.sidebar:
            app = option_menu(
                menu_title='Skin disease  Detection',
                options=['Home', 'Predict disease', 'Diagnosis', 'About Skin Disease'],
                icons=['house-fill', 'upload', 'info-circle', 'play-circle'],
                menu_icon='cast',
                default_index=0,
                styles={
                    "container": {"padding": "5!important", "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px", "--hover-color": "blue"},
                    "nav-link-selected": {"background-color": "#02ab21"},
                }
            )

        for app_info in self.apps:
            if app_info["title"] == app:
                app_info["function"]()  # Call the app function
                break

# Create the MultiApp instance
app = MultiApp()

# Add apps to the MultiApp instance in the desired order
app.add_app("Home", home.app)  # Using the app() function
app.add_app("Predict disease", upload.app)  # Using the app() function
app.add_app("About Skin Disease", about.app)  # Using the app() functions
app.add_app("Diagnosis", remedies.app)  # Using the app() function

# Run the app
app.run()
