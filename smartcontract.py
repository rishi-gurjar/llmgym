from main import combined_calls

assistant_content = """
You are the arbitrator of a contract between two individuals. Only Respond in True or False.

Data will be given to you and based on the data, you will decide if the contract is valid or not. If the
conditions are met, respond with True. If the conditions are not met, respond with False.

Contract details and data will be provided.
"""
prompt = """
The contract is as follows:

If the price of the $DOGE coin is above $0.50, then Person A 

The data is as follows:

The Warriors won the NBA Finals.
"""

messages = [
    {"role": "system", "content": assistant_content},
    {"role": "user", "content": prompt}
]

combined_calls(["gpt-3.5-turbo"], messages=messages, times=10)