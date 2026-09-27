# 🤖 AI-Agent

A simple terminal-based AI assistant built with **Python 🐍, Ollama 🦙, and Qwen3:4b 🧠**.

## 🛠️ Requirements

- 🐍 **Python 3**
- 🦙 **Ollama**
- 🧠 **Qwen3:4b**
- 💻 **VS Code** — recommended for development

## 🚀 Setup

Create and activate virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install openai python-dotenv
```

Download Qwen3:

```bash
ollama pull qwen3:4b
```

## ▶️ Run

```bash
python3 main.py
```

Type `exit` to stop the assistant.

## 📁 Structure

AI-Agent/
├── main.py
├── assistant.py
├── .env
├── .gitignore
└── requirements.txt

💡 **Note:** VS Code is optional. Python and Ollama are the important requirements for running the project.