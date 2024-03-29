from litellm import completion
from dotenv import load_dotenv
import os
import json
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["MISTRAL_API_KEY"] = os.getenv("MISTRAL_API_KEY")


def openai_call(messages, model):
    response = completion(model=model, 
                          messages=messages, 
                          temperature=0.5,
                          response_format={"type": "json_object"},
                          max_tokens=1000
                          )

    return response.choices[0].message.content
    
def mistral_call(messages,model):
    response = completion(
        model=model,
        messages=messages,
        #response_format={"type": "json_object"},
        temperature=0.5,
        max_tokens=1000
     )

    return response.choices[0].message.content


def print_combined_calls(calls, messages, times=1):
    for _ in range(times):
        for call in calls:
            if call[:3] == 'gpt':
                if call == 'gpt4':
                    print('gpt-4')
                    print(openai_call(messages, 'gpt-4'))
                elif call == 'gpt-3.5-turbo':
                    print('gpt-3.5-turbo')
                    print(openai_call(messages, 'gpt-3.5-turbo'))
            elif 'mistral' in call:
                if call == 'mistral-tiny':
                    print('mistral/mistral-tiny')
                    print(mistral_call(messages, 'mistral/mistral-tiny'))             
                if call == 'mistral-small':
                    print('mistral/mistral-small')
                    print(mistral_call(messages, 'mistral/mistral-small'))
                if call == 'mistral-medium':
                    print('mistral/mistral-medium')
                    print(mistral_call(messages, 'mistral/mistral-medium'))
                elif call == 'mistral-large':
                    print('mistral/mistral-large-latest')
                    print(mistral_call(messages, 'mistral/mistral-large-latest'))
            print("")


def combined_calls(calls, messages, times=1):

    for _ in range(times):
        for call in calls:
            if call[:3] == 'gpt':
                if call == 'gpt4':
                    print('gpt-4')
                    print(openai_call(messages, 'gpt-4'))
                elif call == 'gpt-3.5-turbo':
                    print('gpt-3.5-turbo')
                    return openai_call(messages, 'gpt-3.5-turbo')

            elif 'mistral' in call:
                if call == 'mistral-tiny':
                    print('mistral/mistral-tiny')
                    print(mistral_call(messages, 'mistral/mistral-tiny'))
                if call == 'mistral-small':
                    print('mistral/mistral-small')
                    print(mistral_call(messages, 'mistral/mistral-small'))
                if call == 'mistral-medium':
                    print('mistral/mistral-medium')
                    print(mistral_call(messages, 'mistral/mistral-medium'))
                elif call == 'mistral-large':
                    print('mistral/mistral-large-latest')
                    print(mistral_call(messages, 'mistral/mistral-large-latest'))
            print("")
    
    return None

if __name__ == "__main__":

    assistant_content = "You are an AI assistant"
    prompt = "Tell me a joke about VCs"

    messages = [
        {"role": "system", "content": assistant_content},
        {"role": "user", "content": prompt}
    ]

    calls = ['gpt4', 'mistral-medium', 'mistral-large']
    print_combined_calls(calls, messages)


    