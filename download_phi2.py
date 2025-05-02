from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "microsoft/phi-2"

# Load tokenizer from Hugging Face
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Load the Phi-2 model from Hugging Face
model = AutoModelForCausalLM.from_pretrained(model_name)

# Save the model locally under "./models/phi-2"
model.save_pretrained("./models/phi-2")

# Save the tokenizer locally under "./models/phi-2"
tokenizer.save_pretrained("./models/phi-2")

print("Phi-2 model and tokenizer successfully downloaded and saved locally.")
