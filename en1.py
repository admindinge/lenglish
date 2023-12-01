import random

def create_dictionary():
    dictionary = {
        'apple': 'яблоко',
        'banana': 'банан',
        'orange': 'апельсин',
        'grape': 'виноград',
        # Add more words of your choice
    }
    return dictionary

def testing(dictionary):
    correct_answers = 0
    words = list(dictionary.keys())

    number_of_questions = int(input("How many questions do you want to ask? "))

    for _ in range(number_of_questions):
        if not words:
            print("You've exhausted all the words in the dictionary.")
            break

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
    dictionary = create_dictionary()
    testing(dictionary)
