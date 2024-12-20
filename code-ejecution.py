import os
import dotenv
import google.generativeai as genai

dotenv.load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])


def main():
    model = genai.GenerativeModel(
        model_name="gemini-2.0-flash-exp", tools="code_execution"
    )

    chat = model.start_chat()

    response = chat.send_message(
        (
            "What is the sum of the first 50 prime numbers? "
            "Generate and run code for the calculation, and make sure you get all 50."
        )
    )

    print(response.text)


if __name__ == "__main__":
    main()
