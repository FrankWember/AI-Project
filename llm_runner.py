import requests
import json

# Function to query a local model
def query_model(model, prompt):
    url = "http://127.0.0.1:11434/api/generate"
    try:
        response = requests.post(url, json={"model": model, "prompt": prompt, "stream": False}, timeout=60)
        data = response.json()  # Parse JSON response
        return data.get("response", "No response received")  # Return model response
    except Exception as e:
        return f"Error: {e}"

# Read prompts
with open("prompts.txt") as file:
    prompts = [line.strip() for line in file]

# Get responses
responses = [
    f"Prompt: {p}\nTinyLlama: {query_model('tinyllama', p)}\nPhi3: {query_model('phi3:mini', p)}\n\n"
    for p in prompts
]

# Save results
with open("responses.txt", "w") as file:
    file.writelines(responses)

print("Responses saved in responses.txt")
