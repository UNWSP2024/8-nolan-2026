# By Nolan Nelsen
# Written on 3/20/2026
# US State Capitals Quiz

# Program #3: Capital Quiz
# Write a program that creates a dictionary containing the U.S. states as keys,
# and their capitals as values.
# The program should then randomly quiz the user by displaying the name of a state
# and asking the user to enter the state's capital.
# The program should count of the number of correct and incorrect responses.
# (You could alternatively use another country and provinces,
# or countries of the world and capitals).

import random

def capital_quiz():
    # States with their respective capitals
    states_and_capitals = states_and_capitals = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
    "Colorado": "Denver",
    "Connecticut": "Hartford",
    "Delaware": "Dover",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
    "Hawaii": "Honolulu",
    "Idaho": "Boise",
    "Illinois": "Springfield",
    "Indiana": "Indianapolis",
    "Iowa": "Des Moines",
    "Kansas": "Topeka",
    "Kentucky": "Frankfort",
    "Louisiana": "Baton Rouge",
    "Maine": "Augusta",
    "Maryland": "Annapolis",
    "Massachusetts": "Boston",
    "Michigan": "Lansing",
    "Minnesota": "Saint Paul",
    "Mississippi": "Jackson",
    "Missouri": "Jefferson City",
    "Montana": "Helena",
    "Nebraska": "Lincoln",
    "Nevada": "Carson City",
    "New Hampshire": "Concord",
    "New Jersey": "Trenton",
    "New Mexico": "Santa Fe",
    "New York": "Albany",
    "North Carolina": "Raleigh",
    "North Dakota": "Bismarck",
    "Ohio": "Columbus",
    "Oklahoma": "Oklahoma City",
    "Oregon": "Salem",
    "Pennsylvania": "Harrisburg",
    "Rhode Island": "Providence",
    "South Carolina": "Columbia",
    "South Dakota": "Pierre",
    "Tennessee": "Nashville",
    "Texas": "Austin",
    "Utah": "Salt Lake City",
    "Vermont": "Montpelier",
    "Virginia": "Richmond",
    "Washington": "Olympia",
    "West Virginia": "Charleston",
    "Wisconsin": "Madison",
    "Wyoming": "Cheyenne"
}

    correct = 0
    incorrect = 0

    # Convert dictionary keys to a list for random selection
    states = list(states_and_capitals.keys())

    # Ask 5 random questions
    for _ in range(10):
        state = random.choice(states)
        answer = input(f"What is the capital of {state}? ")

        if answer.strip().lower() == states_and_capitals[state].lower():
            print("Correct!")
            correct += 1
        else:
            print(f"Incorrect. The capital is {states_and_capitals[state]}.")
            incorrect += 1

    print("\nQuiz Results:")
    print(f"Correct answers: {correct}")
    print(f"Incorrect answers: {incorrect}")


# Run the quiz
if __name__ == "__main__":
    capital_quiz()
