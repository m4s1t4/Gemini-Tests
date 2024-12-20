import dotenv
import google.generativeai as genai
import os
import base64

dotenv.load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
doc_path = "/home/m4s1t4/Documents/Mis_Docs/EstudioProductividad/Facultad/Segundo/Análisis_Matemático_2/Libros/CalculoVariasVariablesThomas.pdf"


def main(prompt, doc_path):
    # Read and encode the local file
    with open(doc_path, "rb") as doc_file:
        doc_data = base64.standard_b64encode(doc_file.read()).decode("utf-8")

    model = genai.GenerativeModel(
        model_name="gemini-1.5-pro",
    )

    response = model.generate_content(
        [{"mime_type": "application/pdf", "data": doc_data}, prompt]
    )

    print(response.text)


if __name__ == "__main__":
    while True:
        prompt = input("You: ")
        if prompt.lower() == "exit":
            break
        main(prompt, doc_path)
