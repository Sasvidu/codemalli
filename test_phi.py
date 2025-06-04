from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load model and tokenizer
model_name = "microsoft/phi-1_5"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16)

# Use MPS (Metal GPU) if available
device = "mps" if torch.backends.mps.is_available() else "cpu"
model.to(device)

# Example prompt
prompt = "Explain what a neural network is in simple terms."

# Tokenize input
inputs = tokenizer(prompt, return_tensors="pt").to(device)

# Generate response
with torch.no_grad():
    output = model.generate(**inputs, max_new_tokens=100)

# Decode output
print("\n🧠 Response:\n", tokenizer.decode(output[0], skip_special_tokens=True))
