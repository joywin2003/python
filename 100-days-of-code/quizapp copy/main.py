import random
import os

capitals = {
    'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
    'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
    'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
    'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines',
    'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston',
    'Michigan': 'Lansing', 'Minnesota': 'St. Paul', 'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln',
    'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
    'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville',
    'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier',
    'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
    'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'
}

if not os.path.exists('CapitalsQuizQuestions'):
    os.mkdir('CapitalsQuizQuestions')
    
if not os.path.exists('CapitalsQuizAnswers'):
    os.mkdir('CapitalsQuizAnswers')


for quiz_num in range(1, 36):
    with open(f'CapitalsQuizAnswers/capitalsquiz{quiz_num}.txt', 'w') as quiz_file, open(f'CapitalsQuizQuestions/capitalsquiz_answers{quiz_num}.txt', 'w') as answer_key_file:
        quiz_file.write('Name:\n\nDate:\n\nPeriod:\n\n')
        quiz_file.write((' ' * 20) + f'State Capitals Quiz (Form {quiz_num})')
        quiz_file.write('\n\n')

        states = list(capitals.keys())
        random.shuffle(states)

        for question_num in range(1, 51):
            correct_answer = capitals[states[question_num - 1]]
            wrong_answers = list(capitals.values())
            del wrong_answers[wrong_answers.index(correct_answer)]
            wrong_answers = random.sample(wrong_answers, 3)
            answer_options = wrong_answers + [correct_answer]
            random.shuffle(answer_options)

            quiz_file.write(f'{question_num}. What is the capital of {states[question_num - 1]}?\n')
            for i in range(4):
                quiz_file.write(f"{'ABCD'[i]}. {answer_options[i]}\n")
            quiz_file.write('\n')
            answer_key_file.write(f"{question_num}. {'ABCD'[answer_options.index(correct_answer)]}\n")



