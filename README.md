pdConversational PDF Chatbot using OpenAI API and Streamlit
This repository contains code to create a conversational PDF chatbot using OpenAI's APIs and Streamlit. The chatbot allows users to upload a PDF file and engage in conversation based on the contents of the PDF.

Prerequisites
OpenAI Account: You need to sign up for a free account at OpenAI to obtain API credentials. The free credits provided can be used to create the AI bot.
Python Environment: Ensure you have Python installed on your system. It's recommended to use a virtual environment to manage dependencies.
Streamlit: Install Streamlit using pip install streamlit.
OpenAI Python SDK: Install the OpenAI Python SDK using pip install openai.
Files Included
app.py: This is the main file containing the Streamlit application code.
requirements.txt: This file lists all the Python dependencies required for running the application.
Setting Up
copy this repository.
Navigate to the project directory.
Install the required dependencies using pip install -r requirements.txt.
Sign up for an account at OpenAI and obtain API key.
Replace the placeholder in app.py with your OpenAI API key.
Running the Application
To run the Streamlit app locally, execute the following command:

Copy code
streamlit run app.py
This will start the application, and you can access it via your web browser at http://localhost:8501.

Usage
Upon launching the app, you'll be presented with an interface to upload a PDF file.
Upload the PDF file you want to converse with.
Once the file is uploaded, you can start conversing with the chatbot based on the contents of the PDF.
The chatbot will respond to your queries and engage in conversation based on the information extracted from the PDF.

# ask_pdf
