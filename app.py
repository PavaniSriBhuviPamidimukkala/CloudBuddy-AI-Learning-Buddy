import streamlit as st
import requests
import json

# Page settings
st.set_page_config(
    page_title="AI Learning Buddy",
    page_icon="📚",
    layout="wide"
)

# Secure API setup from Streamlit secrets
api_key = st.secrets["GROQ_API_KEY"]

def generate_ai_response(prompt):
    """Helper function to call a completely free alternative model instantly."""
    # Corrected API Endpoint URL
    url = "https://groq.com"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama3-8b-8192",  # Fast, highly accurate learning model
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            # Correct JSON dictionary structure parsing
            return response.json()['choices'][0]['message']['content']
        else:
            return f"⚠️ API Error (Status {response.status_code}): Please verify your GROQ_API_KEY value in your secrets."
    except Exception as e:
        return f"⚠️ Connection Error: {str(e)}"

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
        if topic:
            with st.spinner("Tutor is thinking..."):
                prompt = f"""
                Explain {topic} in a simple way.
                Include:
                - Basic explanation
                - Key points
                - Important concepts
                """
                response_text = generate_ai_response(prompt)
                st.write(response_text)
        else:
            st.warning("Please enter a topic.")

# Real World Example
elif option == "Real World Example":
    topic = st.text_input("Enter the topic")
    if st.button("Generate Examples"):
        if topic:
            with st.spinner("Finding examples..."):
                prompt = f"""
                Give real world examples of {topic}.
                Explain how it is used in daily life and industries.
                """
                response_text = generate_ai_response(prompt)
                st.write(response_text)
        else:
            st.warning("Please enter a topic.")

# Quiz Generator
elif option == "Generate Quiz":
    topic = st.text_input("Enter the topic")
    number = st.slider("Number of questions", 3, 10, 5)
    if st.button("Create Quiz"):
        if topic:
            with st.spinner("Drafting questions..."):
                prompt = f"""
                Generate {number} unique MCQ questions on {topic}.
                Include:
                Question
                Four options
                Correct answer
                Explanation
                Generate different questions every time.
                """
                response_text = generate_ai_response(prompt)
                st.write(response_text)
        else:
            st.warning("Please enter a topic.")

# Summarize Notes
elif option == "Summarize Notes":
    notes = st.text_area("Paste your notes")
    if st.button("Summarize"):
        if notes:
            with st.spinner("Reading notes..."):
                prompt = f"""
                Summarize these notes:
                {notes}
                Provide:
                - Short summary
                - Important points
                - Keywords
                """
                response_text = generate_ai_response(prompt)
                st.write(response_text)
        else:
            st.warning("Please paste some notes first.")

# AI Tutor
elif option == "Ask AI Tutor":
    question = st.text_area("Ask your question")
    if st.button("Ask"):
        if question:
            with st.spinner("Formulating answer..."):
                prompt = f"""
                Act as an AI tutor.
                Explain this question clearly:
                {question}
                """
                response_text = generate_ai_response(prompt)
                st.write(response_text)
        else:
            st.warning("Please type a question.")
