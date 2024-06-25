"""Funkcje dotyczące konfigurajic LLM - Groq"""

from groq import Groq


def groq_client(groq_api_key):
    """Inicjalizacja klienta Groq"""
    client = Groq(
        api_key=groq_api_key,
    )
    return client


def model_options(
    prompt: str,
    temperature: int,
    max_tokens: int,
):
    """Opcje dla Modeli"""
    return dict(
        {
            "prompt": prompt,
            "temperature": temperature,
            "max_tokens": max_tokens,
        }
    )


def run_groq_model(
    groq_api_key: str,
    model: str,
    options: dict,
):
    """Uruchomienie LLM do wskazanych zadan z trybem JSON lub nie"""
    client = groq_client(groq_api_key)
    chat_completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": options["prompt"]},
        ],
        temperature=options.get("temperature", 1),
        max_tokens=options.get("max_tokens", 1500),
        stream=False,
        stop=None,
    )

    model_response = chat_completion.choices[0].message.content
    return model_response
