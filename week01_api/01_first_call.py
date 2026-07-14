from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Explain what is agentic AI in a few words",
)

print(interaction.output_text)