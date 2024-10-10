import streamlit as st

def app():
 
    st.title("Find Doctor And Book Apointment here 👩‍⚕️🩺🫀")

    # URL of Practo
    #website_url = "https://www.hcgoncology.com/campaigns/hcg-oncology-nagpur-brand/?utm_source=google&utm_medium=CPM&utm_campaign=nagpur_brand&utm_source=google&utm_medium=CPC&utm_campaign=HCG_Brand_Nagpur&utm_content=search&gclid=Cj0KCQjwgL-3BhDnARIsAL6KZ69JMn5lHv4OLaepgM-KMRYjUYDilRFLzErF1Ic-KrIk0xGXpsPo3UwaAse4EALw_wcB"
    website_url = "https://www.credihealth.com/doctors/nagpur/cancer"
    # Iframe to embed the Practo website
    st.markdown(
        f'<iframe src="{website_url}" width="1000" height="1500" style="border:none;"></iframe>',
        unsafe_allow_html=True
    )
if __name__ == "__main__":
 app()