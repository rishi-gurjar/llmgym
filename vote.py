import pandas as pd
import json
from main import combined_calls
from arena import json2csv

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('people.csv')
df['number'] = df['number'].astype(int)
rows = df.to_dict('records')
people = {row['number']: row for row in rows}

def vote():
    for person in people:
        person_name = people[person]['name']
        person_gender = people[person]['gender']
        person_age = people[person]['age']
        person_political_leaning = people[person]['political_leaning']
        person_martial_status = people[person]['marital_status']
        person_education = people[person]['education']
        person_occupation = people[person]['occupation']
        person_income = people[person]['income']
        person_religion = people[person]['religion']
        person_ethnicity = people[person]['ethnicity']
        person_nationality = people[person]['nationality']

        assistant_content = f"""
        
        Your name is: {person_name}
        You are a {person_gender}, age {person_age}, and a {person_political_leaning}.
        You are {person_martial_status} with a {person_education}, and currently work as a {person_occupation}.
        Your income is ${person_income} a year and your religion is {person_religion}.
        Your ethnicity is {person_ethnicity}, born in {person_nationality}, and you've lived in the United States for many years now.
        """
        
        prompt = """
        Your hometown has $2 million and has the choice to build a public park or museum showing the heritage of the city. The decision is put up to a vote. Which way will you vote? Voting is on a scale from -1 to 1.

        If you really want to vote for a public park, vote with a 1. If you really want to vote for a museum, vote with a -1. If you want neither, vote 0. The farther from 0 indicates that you want it to happen more, for example, a person who votes with 0.8 wants a park more than someone who votes 0.1, who just marginally wants a park.

        Only output the number in the following JSON format:

        {
        'vote': <insert_vote>
        }
        """

        messages = [
        {"role": "system", "content": assistant_content},
        {"role": "user", "content": prompt}
        ]

        calls = ['gpt-3.5-turbo']

        print("Person #", people[person]['number'])
        person_vote = combined_calls(calls, messages, times=1)
        parsed_vote = json.loads(person_vote)
        vote_value = parsed_vote["vote"]

        people[person]['vote'] = vote_value
        print("Vote ", vote_value)

        #print(people[person])

    #print(x)
    #print(people)
    json2csv(people)
    #print(data)

if __name__ == "__main__":
    vote()
