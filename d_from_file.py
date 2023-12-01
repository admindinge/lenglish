import random

def read_dictionary_from_file(file_path):
    dictionary = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line:
                word, translation = line.split(' ', 1)
                dictionary[word] = translation
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
    file_path = 'path/to/your/dictionary.txt'  # Замените путь на путь к вашему файлу словаря
    dictionary = read_dictionary_from_file(file_path)
    testing(dictionary)
