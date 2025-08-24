# Usage Examples

## Tokenization Demo

Input text:
🌟 Hello world 🌟

Output:
Model: gpt2
Tokens: ðŁ | Į | Ł | ĠHello | Ġworld | ĠðŁ | Į | Ł
Token IDs: [8582, 234, 253, 18435, 995, 12520, 234, 253]
Stats: 8 tokens, avg length 2.25

Model: bert-base-uncased
Tokens: [UNK] | hello | world | [UNK]
Token IDs: [100, 7592, 2088, 100]
Stats: 4 tokens, avg length 5.0

Input text:
🌟 Hello world 🌟!

Model: gpt2
Tokens: ðŁ | Į | Ł | ĠHello | Ġworld | ĠðŁ | Į | Ł | Ġ!
Token IDs: [8582, 234, 253, 18435, 995, 12520, 234, 253, 5145]
Stats: 9 tokens, avg length 2.5555555555555554

Model: bert-base-uncased
Tokens: [UNK] | hello | world | [UNK] | !
Token IDs: [100, 7592, 2088, 100, 999]
Stats: 5 tokens, avg length 4.2


### Notes
- Emojis like `🌟` are not always in the GPT-2 vocabulary as single tokens.  
- Instead, they get split into multiple sub-tokens (`['ðŁ', 'Į', 'Ł']`).  
- This shows how the tokenizer handles characters outside its common training data. 
- while that special character similar to G is for space


# Summarization
Input:
Large language models are trained on huge datasets to generate human-like text.

Output:
"LLMs generate human-like text by learning from massive datasets."

# Sentiment Analysis
Input: I love this project!
Output: [{'label': 'POSITIVE', 'score': 0.9998873472213745}]

Input: I hate this project!
Output: [{'label': 'NEGATIVE', 'score': 0.9997379183769226}]
