from google import genai

client = genai.Client()

stream = client.interactions.create(
    model="gemini-3.5-flash",
    input="Explain how Gen AI works",
    stream=True
)

for event in stream:
    print(event)