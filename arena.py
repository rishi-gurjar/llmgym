from main import *
import csv


def json2csv(x):
    # Extract the list of people
    people = x['people']

    # Convert each person string to a dictionary
    people = [json.loads(person) for person in people]

    # Write the people list to a CSV file
    with open('people.csv', 'w', newline='') as csvfile:
        fieldnames = ['name', 'gender', 'age', 'political_leaning', 'marital_status', 'education', 'occupation', 'income', 'religion', 'ethnicity', 'nationality']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for person in people:
            writer.writerow(person)

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

#generate synethtic roles
#quadratic vote system