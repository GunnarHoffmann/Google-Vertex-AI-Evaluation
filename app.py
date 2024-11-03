import streamlit
import vertexai

vertexai.init(project='prj-mygcpproject-219-8a4e', location='europe-west4')

from vertexai.generative_models import GenerativeModel
model = GenerativeModel("gemini-pro")
print(model.generate_content("Why is sky blue?"))
