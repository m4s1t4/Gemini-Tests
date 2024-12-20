import google.generativeai as genai

model = genai.GenerativeModel("models/gemini-1.5-pro-002")
response = model.generate_content(
    contents="What is the land area of Spain?", tools="google_search_retrieval"
)
print(response.text)
