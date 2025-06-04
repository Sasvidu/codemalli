from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Setup
model_name = "microsoft/phi-1_5"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16)

# Use MPS if available
device = "mps" if torch.backends.mps.is_available() else "cpu"
model.to(device)

def generate_explanation(question):
    prompt = (
        "Explain in simple terms:\n"
        "Q: What is gravity?\n"
        "A: Gravity is the force that pulls things towards each other.\n\n"
        f"Q: {question}\n"
        "A:"
    )

    inputs = tokenizer(prompt, return_tensors="pt").to(device)

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=100,
            do_sample=True,
            top_k=50,
            top_p=0.95,
            temperature=0.8
        )

    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return generated_text.split("A:")[-1].strip()
