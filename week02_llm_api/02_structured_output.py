from google import genai
from pydantic import BaseModel

client = genai.Client()

class Recipe(BaseModel):
    name: str
    ingredients: list[str]
    process: list[str]

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Give me recipe for banana bread",
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": Recipe.model_json_schema()
    }
)

recipe = Recipe.model_validate_json(interaction.output_text)

print(recipe)

