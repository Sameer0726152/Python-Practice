from google import genai
client = genai.Client(
    api_key = "Your-API-Key"
)
response = client.models.generate_content(
    model = "gemini-3.6-flash", contents = "How do you feel?"
)
print(response.text)