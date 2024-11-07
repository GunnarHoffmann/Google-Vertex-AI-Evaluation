import streamlit as st
import vertexai
import json
from google.oauth2 import service_account
from google.cloud import aiplatform
from vertexai.generative_models import GenerativeModel

# Set page configuration for a more polished look
st.set_page_config(page_title='Gemini Q&A App', page_icon=':star:', layout='centered', initial_sidebar_state='auto')

# Add a sidebar with app information
st.sidebar.title('Gemini Q&A App')
st.sidebar.markdown('''
This app uses Google's Vertex AI to generate answers to your questions.

Features:
- Powered by Gemini model
- Simple and clean user interface
''')

# Configure Google Vertex AI for Gemini
vertex_ai_credentials_json = st.secrets["vertex_ai_key"]
vertex_ai_credentials_info = json.loads(vertex_ai_credentials_json)
vertex_ai_credentials = service_account.Credentials.from_service_account_info(vertex_ai_credentials_info)
project_id = st.secrets["google_cloud"]["project_id"]
location = st.secrets["google_cloud"]["location"]
aiplatform.init(project=project_id, location=location, credentials=vertex_ai_credentials)

# Initialize Vertex AI
vertexai.init(project='prj-mygcpproject-219-8a4e', location='europe-west4')

# Instantiate the generative model
model = GenerativeModel("gemini-1.5-flash-001")

# Add a header and question input
st.title('Gemini Q&A')
st.header('Ask anything to Google Gemini!')
question = st.text_input('Enter your question:', 'Why is the sky blue?')

# Generate answer when user submits a question
if st.button('Get Answer'):
    with st.spinner('Generating answer...'):
        answer = model.generate_content(question).text
    st.success('Answer generated successfully!')
    st.write(f'**Question:** {question}')
    st.write(f'**Answer by Google Gemini Flash:** {answer}')

# Add a footer with contact info
st.markdown("---")
st.markdown('Created by [Your Name](https://www.yourwebsite.com) | Powered by Google Vertex AI')
