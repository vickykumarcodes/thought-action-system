# Thought → Action System

A local AI-powered automation system that converts natural language commands into real computer actions — no cloud APIs, no API keys, runs entirely on your machine.

## How it works

You type a command → a local LLM interprets it → actions execute on your PC

```
You: open youtube
You: type hello world
You: search for python tutorials
```

## Tech Stack
- **Python** — core pipeline
- **Ollama** — local LLM inference (no API key needed)
- **PyAutoGUI** — mouse, keyboard, and screen automation
- **requests** — HTTP client for Ollama

## Project Structure

thought_action_system/
├── main.py          # Entry point
├── core/            # Interpreter and executor pipeline
├── llm/             # Ollama HTTP client and prompt logic
├── actions/         # Browser, typing, system actions
├── utils/           # Config and logger (v1.1)
└── tests/           # Test suite (v1.1)

## Setup

**Requirements:** Python 3.10+, [Ollama](https://ollama.com) installed and running

```bash
git clone https://github.com/vickykumarcodes/thought-action-system.git
cd thought-action-system
python -m venv env
env\Scripts\activate        # Windows
pip install -r requirements.txt
```

Start Ollama with your model(llama3), then:

```bash
python main.py
```

## Roadmap

- [x] v1.0 — Core pipeline (interpret → execute), browser, typing, system actions
- [ ] v1.1 — File search across all drives, config system, logging
- [ ] v1.2 — Voice input support
- [ ] v1.3 — Gesture control