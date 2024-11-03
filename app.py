import streamlit
import vertexai

vertexai.init(project='my-project', location='us-central1')

from vertexai.generative_models import GenerativeModel
model = GenerativeModel("gemini-pro")
print(model.generate_content("Why is sky blue?"))
