
import random
import requests

def read_dictionary_from_github(raw_url):
    dictionary = {}
    response = requests.get(raw_url)
    
    if response.status_code == 200:
        content = response.text.split('\n')
        for line in content:
            line = line.strip()
            if line:
                word, translation = line.split(' ', 1)
                dictionary[word] = translation
    else:
        print(f"Failed to fetch dictionary. Status code: {response.status_code}")

    return dictionary

def testing(dictionary):
    correct_answers = 0
    words = list(dictionary.keys())

    number_of_questions = min(len(words), int(input("How many questions do you want to ask? ")))

    for _ in range(number_of_questions):
        random_word = random.choice(words)
        correct_translation = dictionary[random_word]

        answer = input(f"What is the translation of the word '{random_word}'? ")

        if answer.lower() == correct_translation.lower():
            print("Correct!")
            correct_answers += 1
        else:
            print(f"Incorrect. The correct answer is: {correct_translation}")

        words.remove(random_word)

    percentage_correct = (correct_answers / number_of_questions) * 100
    print(f"\nYou answered {correct_answers} out of {number_of_questions} questions correctly.")
    print(f"Percentage of correct answers: {percentage_correct}%")

if __name__ == "__main__":
    github_raw_url = 'https://raw.githubusercontent.com/your_username/your_repository/main/your_dictionary.txt'
    # Замените URL на фактический URL вашего словаря на GitHub
    dictionary = read_dictionary_from_github(github_raw_url)
    
    if dictionary:
        testing(dictionary)
