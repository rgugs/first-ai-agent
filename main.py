import os

from dotenv import load_dotenv
from openai import OpenAI


def main():
    load_dotenv()

    current_model = os.environ.get("CURRENT_MODEL")
    if current_model is None:
        raise RuntimeError("Current model not set from environment")
    base_url = os.environ.get("REMOTE_URL")
    if base_url is None:
        raise RuntimeError("Base url not set from environment")
    api_key = os.environ.get("OLLAMA_API_KEY")
    if api_key is None:
        raise RuntimeError("API key not found in environment")

    client = OpenAI(
        base_url=base_url,
        api_key=api_key,
    )

    response = client.responses.create(
        model=current_model,
        input="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.",
    )

    print(f"User Prompt: {response.output_text}")
    print(f"Prompt tokens: {response.usage.input_tokens}")

    print(f"Response tokens: {response.usage.output_tokens}")


if __name__ == "__main__":
    main()
