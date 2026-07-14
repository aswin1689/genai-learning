from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="explain inference",
    extra_body={
        "system_instruction":"""
        you are a senior gen ai engineer.
        explain with simple examples
        """,
        "generation_config": {
            "temperature": 0.2,
            "max_output_tokens": 2000
        }
    }
    
)

print(interaction.output_text)
print(interaction.id)
print(interaction.model)