# LLM_Basics – Week 1 Fellowship Project

## Overview
This project explores the basics of Large Language Models (LLMs) through two core areas:

1. **API Integration** with OpenAI GPT models (summarization).
2. **Tokenization Exploration** using Hugging Face (GPT-2, BERT).

It also includes analysis features (sentiment detection) and a simple CLI interface to interact with all features.

---

## Features

- OpenAI API integration with error handling & safe retries.
- Summarization via GPT (when API quota is available).
- Tokenization explorer: compare GPT-2 vs. BERT tokenization.
- Token stats: number of tokens, average token length.
- Handles edge cases (emojis 🌟, special characters).
- Sentiment analysis using Hugging Face pipeline.
- Command-line interface (CLI) with modes: `summarize`, `tokenize`, `sentiment`.

---

## ⚙️ Setup Instructions

### 1. Clone & Install
git clone <your-repo-url>
cd LLM_Basics
pip install -r requirements.txt
