# Notes for Using OpenAI API with BootDev AI Agent Course

This is a bit of a touch and go getting things organized to use Ollama and a local model with OpenAI API to complete the AI Agent course on Boot.dev.

*Hints*
- Check the submission tests for Gemini specific text that is expected in the stdout. You can include this as a printed string to complete the tests that require it.
```python
print(response.output_text)
    "models.generate_content"
    ".text"
```

## Chapter 1 - LLMs
L1: Checking the bootdev cli and python3 are installed

L2: Set up UV environment. I don't follow these instructions. I make my Github repo and then clone it to the location and initialize a UV project inside the git project. You also don't need to activate the virtual environment as UV will do that whenever you run it. I have it set to initialize any venv found in my workspace just so I have a visual indicator the correct venv is being used, but it is not required. It as you add `uv add google-genai==1.12.1` and `uv add python-dotenv==1.1.0` and run the project with `uv run main.py`, and is going to check those are in the `uv pip list`. You must install these, but you can remove them later.

L3: This sets up the text to run your first API call. It expects Gemini specific code in the stdout that you can include as a print.