import streamlit as st
import requests
import json

# Page settings
st.set_page_config(
    page_title="AI Learning Buddy",
    page_icon="📚",
    layout="wide"
)

# Secure API configuration via Streamlit Secrets Management
api_key = st.secrets["GROQ_API_KEY"]

def generate_ai_response(prompt):
    """Executes a valid POST request to the Groq API endpoint."""
    # FIXED: Ensured canonical slash configuration to eliminate the 405 Method Not Allowed error
    url = "https://api.groq.com/openai/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama3-8b-8192",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            # FIXED: Explicitly navigates Open-AI compatible dictionary outputs safely
            return response.json()['choices'][0]['message']['content']
        else:
            return f"⚠️ API Error (Status {response.status_code}): Please verify your GROQ_API_KEY value in your secrets dashboard."
    except Exception as e:
        return f"⚠️ Connection Error: {str(e)}"

# User Interface Title Engine
st.title("📚 AI Learning Buddy")
st.write("Your personal AI tutor to learn concepts easily.")

# Sidebar Execution Panel
option = st.sidebar.selectbox(
    "Choose Learning Mode",
    ["Explain a Topic", "Real World Example", "Generate Quiz", "Summarize Notes", "Ask AI Tutor"]
)

# Explain Topic Workflow
if option == "Explain a Topic":
    topic = st.text_input("Enter the topic")
    if st.button("Explain"):
        if topic.strip():
            with st.spinner("Tutor is thinking..."):
                prompt = f"Explain {topic} in a simple way.\nInclude:\n- Basic explanation\n- Key points\n- Important concepts"
                st.write(generate_ai_response(prompt))
        else:
            st.warning("Please enter a topic.")

# Real World Example Workflow
elif option == "Real World Example":
    topic = st.text_input("Enter the topic")
    if st.button("Generate Examples"):
        if topic.strip():
            with st.spinner("Finding examples..."):
                prompt = f"Give real world examples of {topic}.\nExplain how it is used in daily life and industries."
                st.write(generate_ai_response(prompt))
        else:
            st.warning("Please enter a topic.")

# Quiz Generator Workflow
elif option == "Generate Quiz":
    topic = st.text_input("Enter the topic")
    number = st.slider("Number of questions", 3, 10, 5)
    if st.button("Create Quiz"):
        if topic.strip():
            with st.spinner("Drafting questions..."):
                prompt = f"Generate {number} unique MCQ questions on {topic}.\nInclude:\nQuestion\nFour options\nCorrect answer\nExplanation\nGenerate different questions every time."
                st.write(generate_ai_response(prompt))
        else:
            st.warning("Please enter a topic.")

# Summarize Notes Workflow
elif option == "Summarize Notes":
    notes = st.text_area("Paste your notes")
    if st.button("Summarize"):
        if notes.strip():
            with st.spinner("Reading notes..."):
                prompt = f"Summarize these notes:\n{notes}\nProvide:\n- Short summary\n- Important points\n- Keywords"
                st.write(generate_ai_response(prompt))
        else:
            st.warning("Please paste some notes first.")

# AI Tutor Workflow
elif option == "Ask AI Tutor":
    question = st.text_area("Ask your question")
    if st.button("Ask"):
        if question.strip():
            with st.spinner("Formulating answer..."):
                prompt = f"Act as an AI tutor.\nExplain this question clearly:\n{question}"
                st.write(generate_ai_response(prompt))
        else:
            st.warning("Please type a question.")
