from main import *
import csv
import pandas as pd

def json2csv(data):
    # Extract the list of people

    # create a pandas DataFrame from the dictionary
    df = pd.DataFrame.from_dict(data, orient='index')

    # reset the index of the DataFrame to create a new column for the index values
    df = df.reset_index()

    # rename the 'index' column to 'number'
    df = df.rename(columns={'index': 'number'})

    # save the DataFrame to a CSV file
    df.to_csv('output.csv', index=False)


def synthesize_town():
    data = {"people": []}

    assistant_content = """
                        You are an AI bot that helps generate synethic identities for democracy testing.
                        """
    prompt = """
            Here is an example identity for a citizen:

                {
                "name": "Alice Johnson",
                "gender": "female",
                "age": 35,
                "political_leaning": "liberal",
                "marital_status": "married",
                "education": "bachelor's degree",
                "occupation": "software engineer",
                "income": 80000,
                "religion": "Christian",
                "ethnicity": "Asian American",
                "nationality": "United States"
                }

            Generate a new identity and make sure it is different, offering a new perspective of a citizen of Praxis. Look at the following JSON for people already in the city, make sure you generate people that represent new viewpoints and backgrounds. 
            
            """ + json.dumps(data) + """
            
            Only output the JSON, do not edit the JSON fields.
            """

    messages = [
        {"role": "system", "content": assistant_content},
        {"role": "user", "content": prompt}
    ]

    #calls = ['gpt4', 'mistral-tiny', 'mistral-small', 'mistral-medium', 'mistral-large']
    calls = ['mistral-tiny']

    x = combined_calls(calls, messages, prompt, data, times=15)
    json2csv(x)