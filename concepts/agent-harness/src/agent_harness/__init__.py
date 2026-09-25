import os
from openai import OpenAI
from dotenv import load_dotenv

def main() -> None:
    load_dotenv()
    client = OpenAI(
      base_url=os.getenv("BASE_URL"),
      api_key=os.getenv("API_KEY")
      )

    user_input = input("Enter your prompt>")

    SYSTEM_PROMPT = """
    You are an coding agent, with expertise in breaking down tasks into smaller subtasks and solving the complete tasks. You should only code.
    """

    response = client.chat.completions.create(
      model=os.getenv("MODEL_ID"),
      messages=[
          {"role": "system", "content": SYSTEM_PROMPT},
          {"role": "user", "content": user_input},
      ],
    )

    output = response.choices[0].message.content;
    completion_details = response.usage.completion_tokens_details;
    prompt_details = response.usage.prompt_tokens_details;

    usage = {
        "prompt_tokens": response.usage.prompt_tokens,
        "completion_tokens": response.usage.completion_tokens,
        "reasoning_tokens": getattr(completion_details, "reasoning_tokens", None),
        "cached_tokens": getattr(prompt_details, "cached_tokens", None)
    }

    print("\nAgent: ", output, "\n")
    print(usage)
