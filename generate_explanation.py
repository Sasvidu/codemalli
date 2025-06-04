from transformers import pipeline
from transformers import logging

logging.set_verbosity_debug()

# Load a small language model
llm = pipeline("text-generation", model="microsoft/phi-1_5", max_new_tokens=100)

def generate_explanation(question):
    prompt = f"Explain in simple words: {question}"
    output = llm(prompt)[0]['generated_text']
    return output.replace(prompt, "").strip()
