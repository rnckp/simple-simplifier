import os
import re
from dotenv import load_dotenv
from openai import OpenAI

from simplifier.utils_prompts import (
    SYSTEM_MESSAGE_ES,
    SYSTEM_MESSAGE_LS,
    RULES_ES,
    RULES_LS,
    REWRITE_COMPLETE,
    OPENAI_TEMPLATE_ES,
    OPENAI_TEMPLATE_LS,
)

OPENAI_TEMPLATES = [
    OPENAI_TEMPLATE_ES,
    OPENAI_TEMPLATE_LS,
]

# ---------------------------------------------------------------
# Constants

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai_client = OpenAI(api_key=OPENAI_API_KEY)

MODEL_NAME = "gpt-4o"
MAX_TOKENS = 4096

# From our testing we derive a sensible temperature of 0.5 as a good trade-off between creativity and coherence. Adjust this to your needs.
TEMPERATURE = 0.5


# Maximum number of characters for the input text.
# This is way below the context window size of the GPT-4o model. Adjust to your needs.
MAX_CHARS_INPUT = 100_000


# ---------------------------------------------------------------
# Main functions


def _create_prompt(text, prompt_es, prompt_ls, leichte_sprache=False):
    """Create prompt and system message."""
    if leichte_sprache:
        final_prompt = prompt_ls.format(
            rules=RULES_LS, completeness=REWRITE_COMPLETE, prompt=text
        )
        system = SYSTEM_MESSAGE_LS
    else:
        final_prompt = prompt_es.format(
            rules=RULES_ES, completeness=REWRITE_COMPLETE, prompt=text
        )
        system = SYSTEM_MESSAGE_ES
    return final_prompt, system


def _get_result_from_response(response, leichte_sprache=False):
    """Extract text between tags from response."""
    if leichte_sprache:
        result = re.findall(
            r"<leichtesprache>(.*?)</leichtesprache>", response, re.DOTALL
        )
    else:
        result = re.findall(
            r"<einfachesprache>(.*?)</einfachesprache>", response, re.DOTALL
        )
    result = "\n".join(result)
    return result.strip()


def _invoke_openai_model(text, leichte_sprache):
    """Invoke OpenAI model."""
    final_prompt, system = _create_prompt(text, *OPENAI_TEMPLATES, leichte_sprache)
    try:
        message = openai_client.chat.completions.create(
            model=MODEL_NAME,
            temperature=TEMPERATURE,
            max_tokens=MAX_TOKENS,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": final_prompt},
            ],
        )
        message = message.choices[0].message.content.strip()
        return True, _get_result_from_response(message, leichte_sprache)
    except Exception as e:
        print(f"Error: {e}")
        return False, e


def simplify_text(text, leichte_sprache=False):
    """Simplify text."""
    if len(text) > MAX_CHARS_INPUT:
        return f"Error: Dein Text ist zu lang für das System. Bitte kürze ihn auf {MAX_CHARS_INPUT} Zeichen oder weniger."
    success, response = _invoke_openai_model(text, leichte_sprache)
    if success:
        return response
    else:
        return "Error: " + response
