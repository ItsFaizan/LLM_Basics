import argparse
from utils.llm_helpers import summarize_text, analyze_sentiment
from utils.tokenizer_helpers import explore_tokenization

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="LLM Basics: Summarization, Tokenization, Sentiment Analysis"
    )
    parser.add_argument(
        "mode",
        choices=["summarize", "tokenize", "sentiment"],
        help="Choose the task to run"
    )
    parser.add_argument(
        "text",
        help="Input text for analysis (use quotes for multi-word input)"
    )
    args = parser.parse_args()

    if args.mode == "summarize":
        result = summarize_text(args.text)
        print("\n--- Summarization ---")
        print("Input:", args.text)
        print("Output:", result)

    elif args.mode == "tokenize":
        print("\n--- Tokenization Explorer ---")
        results = explore_tokenization(args.text)
        for model, info in results.items():
            print(f"\nModel: {model}")
            print("Tokens:", " | ".join(info["tokens"]))
            print("Token IDs:", info["ids"])
            print("Stats:", info["num_tokens"], "tokens, avg length", info["avg_token_length"])

    elif args.mode == "sentiment":
        print("\n--- Sentiment Analysis ---")
        result = analyze_sentiment(args.text)
        print("Input:", args.text)
        print("Output:", result)
