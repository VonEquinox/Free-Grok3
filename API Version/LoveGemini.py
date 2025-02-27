from openai import OpenAI

client = OpenAI(
    api_key="AIzaSyD8p2Z2d7Mn9SbqDK1Pg1h5rHsTqASoV-k",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

def ask_gemini_thinking(question):
    response = client.chat.completions.create(
        model="gemini-2.0-flash-thinking-exp-01-21",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": question
            }
        ]
    )

    return response.choices[0].message.content