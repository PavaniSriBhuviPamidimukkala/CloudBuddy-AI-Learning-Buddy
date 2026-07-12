import streamlit as st

st.set_page_config(
    page_title="CloudBuddy",
    page_icon="☁️",
    layout="wide"
)

st.title("☁️ CloudBuddy – AI Learning Buddy")
st.write("Welcome! Learn Cloud Computing Basics with your AI learning companion.")

menu = st.sidebar.selectbox(
    "Choose an Activity",
    [
        "Explain Topic",
        "Real-Life Example",
        "Quiz",
        "About"
    ]
)

if menu == "Explain Topic":

    topic = st.text_input("Enter Topic")

    if st.button("Explain"):

        st.success("Explanation")

        st.write("""
Cloud Computing means using computing resources such as storage,
servers, databases and software over the Internet instead of
your local computer.

Benefits:

• Cost Saving

• Scalability

• Flexibility

• Anywhere Access

• Automatic Backup
""")

elif menu == "Real-Life Example":

    st.info("""
Example:

Google Drive stores your files online.

You can access them from your laptop,
mobile or tablet anywhere.

This is Cloud Computing.
""")

elif menu == "Quiz":

    st.subheader("Cloud Computing Quiz")

    q1 = st.radio(
        "1. Cloud Computing uses",
        ["Internet","USB","Bluetooth","DVD"]
    )

    q2 = st.radio(
        "2. Which is SaaS?",
        ["Google Docs","Router","CPU","RAM"]
    )

    if st.button("Submit"):

        score=0

        if q1=="Internet":
            score+=1

        if q2=="Google Docs":
            score+=1

        st.success(f"Your Score : {score}/2")

        if score==2:
            st.balloons()

elif menu=="About":

    st.write("""
CloudBuddy

Developed by

Pavani Sri Bhuvi Pamidimukkala

AI Learning Buddy Project

Infosys Springboard AI EMPOW(H)ER
""")
