# llmgym
> "I'm in the arena"
-Chamath Palihapitiya

![arena](https://github.com/rishi-gurjar/llmgym/assets/41022502/d0b3c4c9-aaae-4883-aaff-ed23c041621c)

#### Setup
1. Create a .env file in the root directory. Populate it with these values:

```python
OPENAI_API_KEY=<your_openai_api_key>
MISTRAL_API_KEY=<your_mistral_api_key>
```

2. Edit 'proposition_text' and 'proposition_range' at the bottom of the vote.py file with your new proposition
3. Run the following code and see output.csv for voting results

> * python vote.py

###### LEARNINGS
1. When the same LLM (e.g. Mistral Tiny) vote as the same person on the same proposition, hallucination rate is near-zero, very aligned

###### TODO
1. quadratic vote system
2. financial data pipeline
3. visualization/statisical analysis pipeline