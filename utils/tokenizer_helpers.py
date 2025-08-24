from transformers import AutoTokenizer

def explore_tokenization(text: str):
    models = ["gpt2", "bert-base-uncased"]
    results = {}
    for model in models:
        tok = AutoTokenizer.from_pretrained(model)
        tokens = tok.tokenize(text)
        ids = tok.convert_tokens_to_ids(tokens)
        results[model] = {
            "tokens": tokens,
            "ids": ids,
            "num_tokens": len(tokens),
            "avg_token_length": sum(len(t) for t in tokens)/len(tokens) if tokens else 0
        }
    return results
