import streamlit as st
import requests
from streamlit_lottie import st_lottie

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def app():
    lottie_welcome = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_puciaact.json")
    lottie_health = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_5njp3vgg.json")
    
    # Lottie animations for team members
    lottie_john = load_lottieurl("https://lottie.host/02af5db5-20fa-428d-911f-cc2d1ed9cd72/rfAqetfjEx.json")
    lottie_jane = load_lottieurl("https://lottie.host/391d8375-f1e0-4947-bb21-6da354e80f70/enG8WyjajP.json")
    lottie_janvi = load_lottieurl("https://lottie.host/8eabeb49-e7b0-4ac0-8738-d2f020aad2c5/e8YxEqm7KL.json")  # Add URL for Janvi
    lottie_sarvesh = load_lottieurl("https://lottie.host/ae1acbbc-1b2c-4eab-b48d-40208b53a4ff/mzAjaxN9ef.json")  # Add URL for Sarvesh

    # Home Section
    st.title("╰┈➤  Team Skin Disease Prediction ")
    st_lottie(lottie_welcome, height=300, key="welcome")

    st.write("---")

    left_column, right_column = st.columns(2)

    with left_column:
        st.write("## Skin Disease Detection 🩺👩🏻‍⚕️💊")
        st.markdown(
            """
            Our application detects the following diseases👩‍⚕️🩺🫀:

            - **Actinic keratosis**
            - **Basal cell carcinoma**
            - **Dermatofibroma**
            - **Melanoma**
            - **Nevus**
            - **Pigmented benign keratosis**
            - **Seborrheic keratosis**
            - **Squamous cell carcinoma**
            - **Vascular lesion**
            """
        )

    with right_column:
        st_lottie(lottie_health, height=500, key="check")

    st.write("---")
    st.header("🛠️ How It Works?")
    st.write("Our application utilizes machine learning to predict skin diseases from images! 📸")

    st.write("---")
    st.markdown(
        """
        ### 🌟 Features:
        - **User-friendly Interface:** Easy navigation for all users.
        - **Real-time Predictions:** Instant feedback on uploaded images.
        - **Secure & Private:** Your data remains confidential.

        ### 📞 Get in Touch:
        If you have any questions, feel free to reach out!
        """
    )

    # About Section
    st.write("---")
    st.header("👨‍⚕️ About Team 👨🏻‍💼 ")
    st.write(
        """
        Team Diagnose is dedicated to revolutionizing the way skin diseases are detected. Our mission is to provide users with an easy-to-use application that leverages machine learning to analyze images and identify potential skin conditions.

        **Our Goals:**
        - **Accessibility:** Make skin disease detection available to everyone.
        - **Awareness:** Increase awareness about skin health and the importance of early detection.
        - **Innovation:** Continuously improve our algorithms and user experience based on feedback and research.

        **Meet the Team:**
        """
    )

    # Create columns for team members
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.subheader("Janvi")
        st_lottie(lottie_jane, height=150, key="john_image")  # Add Lottie animation here
        st.write("Address: 123 Healthcare Lane, Nagpur, MH 440001")
        st.write("Email: Janvi@email.com")
        st.write("Contact: +91 98765 43210")

    with col2:
        st.subheader("Vedant")
        st_lottie(lottie_john, height=150, key="jane_image")  # Add Lottie animation here
        st.write("Address: 456 Wellness Rd, Nagpur, MH 440002")
        st.write("Email: Vedant@email.com")
        st.write("Contact: +91 87654 32109")

    with col3:
        st.subheader("Smpada")
        st_lottie(lottie_jane, height=150, key="janvi_image")  # Add Lottie animation here
        st.write("Address: 321 Healthy St, Nagpur, MH 440004")
        st.write("Email: janvi.smpada@email.com")
        st.write("Contact: +91 76543 21097")

    with col4:
        st.subheader("Sarvesh ")
        st_lottie(lottie_john, height=150, key="sarvesh_image")  # Add Lottie animation here
        st.write("Address: 654 Care Ave, Nagpur, MH 440005")
        st.write("Email: sarvesh.vedant@email.com")
        st.write("Contact: +91 65432 10986")

    st.write("---")
    st.write("Join us in our mission to promote skin health and save lives!")

if __name__ == "__main__":
    app()
