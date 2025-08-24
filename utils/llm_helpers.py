import time
from openai import OpenAI, RateLimitError, APIError
from config import OPENAI_API_KEY
from transformers import pipeline

client = OpenAI(api_key=OPENAI_API_KEY)

#Task 1: API Integration (summarization, safe calls) 
def safe_api_call(messages, model="gpt-4o-mini", retries=3):
    """Safe wrapper for OpenAI API calls with retry logic."""
    for i in range(retries):
        try:
            response = client.chat.completions.create(model=model, messages=messages)
            return response.choices[0].message.content
        except RateLimitError:
            print("Rate limit hit. Retrying...")
            time.sleep(2)
        except APIError as e:
            print("API error:", e)
            return None
        except Exception as e:
            print("Unexpected error:", e)
            return None

def summarize_text(text: str) -> str:
    """Summarize input text using GPT model"""
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Summarize this in one sentence: {text}"}
    ]
    return safe_api_call(messages)

#Task 2: Analysis Features (sentiment analysis) 
_sentiment_analyzer = pipeline("sentiment-analysis")

def analyze_sentiment(text: str):
    """Return sentiment label and confidence score for given text"""
    return _sentiment_analyzer(text)
