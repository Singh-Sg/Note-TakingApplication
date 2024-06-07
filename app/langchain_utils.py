import openai

def summarize_note_with_langchain(content: str, api_key: str) -> str:
    openai.api_key = api_key
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Summarize this note: {content}",
        max_tokens=50
    )
    summary = response.choices[0].text.strip()
    return summary




