import streamlit as st
import openai
import PyPDF2

openai.api_key = "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"

def generate_response(user_input, pdf_text):
    # Prepare the prompt
    prompt = f"User: {user_input}\n\nPDF Text: {pdf_text}\n\nAssistant:"

    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    
    generated_response = response.choices[0].text.strip()

    return generated_response


def main():
    st.sidebar.image("https://aarambh.siluniversity.com/assets/images/sil-logo.webp", use_column_width=True)
    st.title("Conversational PDF Chatbot")

    
    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

    
    if uploaded_file is not None:
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        pdf_text = ""
        for page in pdf_reader.pages:
            pdf_text += page.extract_text()

        
        user_input = st.text_input("Ask a question about the PDF:")

        
        if user_input:
            generated_response = generate_response(user_input, pdf_text)
            st.text_area("Response:", value=generated_response, height=200)  # Adjust the height as needed

if __name__ == "__main__":
    main()
