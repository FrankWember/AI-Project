# Local LLM Querying Project (MacOS)

## Overview

This project runs **two local AI models (TinyLlama & Phi3-mini)** on your Mac using **Ollama**.  
It reads prompts from a text file, queries both models, and saves the responses to `responses.txt`.

---

## Installation (MacOS)

### **1️ Install Ollama**

Ollama is required to run local AI models. Install it via Homebrew:

```sh
brew install ollama
```

Or install it directly:

```sh

curl -fsSL https://ollama.ai/install.sh | sh
```

---

### **2️ Install the Required AI Models**

Pull the **TinyLlama** and **Phi3-mini** models:

```sh
ollama pull tinyllama
ollama pull phi3:mini
```

Verify the models are installed using:

```sh
ollama list
```

The expected output:

```
NAME                ID              SIZE      MODIFIED
phi3:mini           4f2222927938    2.2 GB    22 minutes ago
tinyllama:latest    2644915ede35    637 MB    33 minutes ago
```

---

### **3️ Install Python Dependencies**

Install the required Python package:

```sh
pip install requests
```

---

## Usage

### **1️ Start Ollama**

Before running the script, start Ollama:

```sh
ollama serve & to verify it is running
```

If Ollama is already running and you face issues, restart it using :

```sh
pkill -f ollama
ollama serve &
```

---

### **2️ Run the Script**

Execute the Python script:

```sh
python llm_runner.py
```

---

### **3️ View Results**

Terminal output:

```sh
llama_model_load: vocab only - skipping tensors
[GIN] 2025/02/18 - 23:49:49 | 200 | 47.287701416s |       127.0.0.1 | POST     "/api/generate"
[GIN] 2025/02/18 - 23:49:51 | 200 |  2.632460083s |       127.0.0.1 | POST     "/api/generate"
[GIN] 2025/02/18 - 23:50:20 | 200 | 28.759492833s |       127.0.0.1 | POST     "/api/generate"
[GIN] 2025/02/18 - 23:50:23 | 200 |   2.37592675s |       127.0.0.1 | POST     "/api/generate"
[GIN] 2025/02/18 - 23:50:42 | 200 | 18.812540625s |       127.0.0.1 | POST     "/api/generate"
Responses saved in responses.txt
```

After running the script, you can check the output file:

```sh
cat responses.txt
```

Example Output:

```
Prompt: A shocking Chinese AI advancement called DeepSeek is sending US stocks plunging
TinyLlama: DeepSeek is a major AI breakthrough that has disrupted stock markets...
Phi3: The AI industry is evolving fast, and China's latest innovation is shaking the markets...

[View Responses.txt](/responses.txt)

```

---

## 📌 Uninstalling

To remove Ollama and its models:

```sh
ollama rm tinyllama
ollama rm phi3:mini
brew uninstall ollama
```

## 📌 Environment Setup (`requirements.yaml`)

For easy dependency installation:

```yaml
dependencies:
  - python=3.10
  - pip:
      - requests
```

To set up the environment:

```sh
conda env create -f requirements.yaml
conda activate llm-project
```

---

## Conclusion

This project allows you to run TinyLlama & Phi3-mini locally, generate AI responses, and save them for analysis locally.

It runs entirely offline

```

---
```
