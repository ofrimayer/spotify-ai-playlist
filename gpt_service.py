# Uses GPT to analyze user prompts
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables (API keys)
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def analyze_prompt(prompt):
    # Ask GPT to suggest real artists/genres
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a music expert."
                    "If the prompt mentions a fictional character (e.g., Lorelai Gilmore),"
                    "ONLY suggest real artists and real genres explicitly shown, mentioned, or strongly associated with that character."
                    "Avoid vague moods. Only list the artist names or genres clearly, like a numbered or bullet list. "
                    "Make sure the artists you suggest have Spotify profiles."
                )
            },
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content


# using gpt4 caused problems