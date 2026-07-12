import streamlit as st
import google.generativeai as genai

# Page settings
st.set_page_config(
    page_title="AI Learning Buddy",
    page_icon="📚",
    layout="wide"
)

# Gemini API setup
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-1.5-flash")

# Title
st.title("📚 AI Learning Buddy")
st.write("Your personal AI tutor to learn concepts easily.")

# Sidebar options
option = st.sidebar.selectbox(
    "Choose Learning Mode",
    [
        "Explain a Topic",
        "Real World Example",
        "Generate Quiz",
        "Summarize Notes",
        "Ask AI Tutor"
    ]
)

# Explain Topic
if option == "Explain a Topic":

    topic = st.text_input("Enter the topic")

    if st.button("Explain"):
        prompt = f"""
        Explain {topic} in a simple way.
        Include:
        - Basic explanation
        - Key points
        - Important concepts
        """

        response = model.generate_content(prompt)
        st.write(response.text)


# Real World Example
elif option == "Real World Example":

    topic = st.text_input("Enter the topic")

    if st.button("Generate Examples"):

        prompt = f"""
        Give real world examples of {topic}.
        Explain how it is used in daily life and industries.
        """

        response = model.generate_content(prompt)
        st.write(response.text)


# Quiz Generator
elif option == "Generate Quiz":

    topic = st.text_input("Enter the topic")
    number = st.slider("Number of questions", 3, 10, 5)

    if st.button("Create Quiz"):

        prompt = f"""
        Generate {number} unique MCQ questions on {topic}.

        Include:
        Question
        Four options
        Correct answer
        Explanation

        Generate different questions every time.
        """

        response = model.generate_content(prompt)
        st.write(response.text)


# Summarize Notes
elif option == "Summarize Notes":

    notes = st.text_area("Paste your notes")

    if st.button("Summarize"):

        prompt = f"""
        Summarize these notes:
        {notes}

        Provide:
        - Short summary
        - Important points
        - Keywords
        """

        response = model.generate_content(prompt)
        st.write(response.text)


# AI Tutor
elif option == "Ask AI Tutor":

    question = st.text_area("Ask your question")

    if st.button("Ask"):

        prompt = f"""
        Act as an AI tutor.
        Explain this question clearly:

        {question}
        """

        response = model.generate_content(prompt)
        st.write(response.text)
