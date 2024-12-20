import dotenv
import google.generativeai as genai
import os

dotenv.load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
# Create the model
generation_config = {
    "temperature": 0.1,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}


def main(generation_config, prompt):

    model = genai.GenerativeModel(
        model_name="gemini-2.0-flash-exp",
        generation_config=generation_config,
    )

    chat_session = model.start_chat(history=[])

    response = chat_session.send_message(f"{prompt}")

    print(response.text)


if __name__ == "__main__":
    while True:
        prompt = input("You: ")
        if prompt.lower() == "exit":
            break
        main(generation_config, prompt)
