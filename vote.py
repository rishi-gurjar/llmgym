import pandas as pd
import json
from main import combined_calls
from arena import json2csv

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('people.csv')
df['number'] = df['number'].astype(int)
rows = df.to_dict('records')
people = {row['number']: row for row in rows}

def vote(proposition_text, proposition_range):
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
        
        prompt = f"""
        Your hometown has $2 million and has the following proposition: 

        {proposition_text}

        The proposition is put up to a vote for all citizens. Which way will you vote? Voting is on a scale from -1 to 1.

        Vote with a 1 if you want to vote for: {proposition_range[1]}
        Vote with a -1 if you want to vote for: {proposition_range[0]}
        If you want neither, vote 0. 
        
        The farther from 0 indicates that you want it to happen more, for example, a person who votes with 0.8 wants {proposition_range[1]} more than someone who votes 0.1, who just marginally wants it.

        Only output the number in the following JSON format:

        {{
        'vote': <insert_vote>
        }}
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
    #proposition_text = "Give all executive power to the mayor or give executive power among a citizen-elected committee."
    #proposition_range = ["executive power to the mayor", "executive power among a citizen-elected committee"]

    proposition_text = """

    The stock market is at a crossroads. Where would you want the city to invest the money, Bitcoin or Gold?

    The GDP growth rate has decreased from 4.9% to 3.2%, indicating a slowdown in economic activity. However, the non-farm payrolls have increased by 275 thousand, suggesting a strong job market.
    The inflation rate has risen to 3.2%, which is above the central bank's target of 2%. This could lead to higher interest rates and reduced consumer spending. On the other hand, the manufacturing PMI has increased to 52.5, indicating expansion in the manufacturing sector.
    The balance of trade deficit has widened to -$67.43 billion, indicating that imports are outpacing exports. However, the current account deficit has narrowed to -$195 billion, suggesting an improvement in the overall trade balance.
    The government debt to GDP ratio has increased to 129%, indicating a high level of government borrowing. This could lead to higher interest rates and reduced government spending in the future. However, the government budget deficit has decreased to -5.8% of GDP, indicating an improvement in fiscal policy.
    """
    proposition_range = ["bitcoin", "gold"] # "0 index" is -1 and "1 index" is 1 for gradient vote in range [-1, 1]
    vote(proposition_text, proposition_range)
