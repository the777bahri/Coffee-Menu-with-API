
from openai import OpenAI

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
  api_key="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",
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-3.5-turbo",
)