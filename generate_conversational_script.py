# generate_conversational_script.py
# This script uses OpenAI's API to transform an explanation into a conversational script.

# Install OpenAI library
!pip install openai

# Import OpenAI library
from openai import OpenAI

# Initialize OpenAI API client with API key
client = OpenAI(api_key="sk-")  # Replace with your actual OpenAI API key

# Set up explanation content (this would typically be passed from youtube_search_transcript.py)
explanation = """in this lesson we're going to talk about the integral of tangent x dx..."""

# Generate a conversational script from the explanation
chat_completion = client.chat.completions.create(
    model="ft:gpt-4o-2024-08-06:personal:ccarre:9z9gzNOs",
    messages=[
        {"role": "system", "content": "You are a math tutor that speaks English."},
        {"role": "user", "content": f"Transform the text in square brackets [{explanation}] into a 60-second skit between two people..."}
    ]
)

# Print the generated skit content
print(chat_completion.choices[0].message.content)
