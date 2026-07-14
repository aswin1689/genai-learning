from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    extra_body={
        "system_instruction":"""
    You are a senior software architect.
    Explain concepts for a developer with 5 years experience.
    Include architecture diagrams using text. Keep it under 500 words.
        """
    },
    input="""
    Explain microservices architecture.
    Compare it with monolith architecture.
    """
)

print(interaction.output_text)