import requests
from common.config import MODE

MODEL = "smollm:135m"
URL = "http://localhost:11434/api/generate"

def run_llm(query, context):
    if MODE == "normal":
        prompt = "."
        num_predict = 1
    else:
        prompt = f"Context: {context}\nQuestion: {query}\nAnswer in one short sentence:"
        num_predict = 10

    response = requests.post(
        URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False,
            "keep_alive": "30m",
            "options": {
                "num_predict": num_predict,
                "temperature": 1
            }
        },
        timeout=60
    )

    response.raise_for_status()
    return response.json()["response"]