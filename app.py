import streamlit
import vertexai
import streamlit as st
import json
from google.oauth2 import service_account
from google.cloud import aiplatform

# Configure Google Vertex AI for Gemini
vertex_ai_credentials_json = st.secrets["vertex_ai_key"]
vertex_ai_credentials_info = json.loads(vertex_ai_credentials_json)
vertex_ai_credentials = service_account.Credentials.from_service_account_info(vertex_ai_credentials_info)
project_id = st.secrets["google_cloud"]["project_id"]
location = st.secrets["google_cloud"]["location"]
aiplatform.init(project=project_id, location=location, credentials=vertex_ai_credentials)

vertexai.init(project='prj-mygcpproject-219-8a4e', location='europe-west4')



from vertexai.generative_models import GenerativeModel
model = GenerativeModel("gemini-1.5-flash-001")
st.write("Hi")
st.write(model.generate_content("Why is sky blue?").text)
st.write("Hello again")
