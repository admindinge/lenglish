import random

def create_dictionary():
    dictionary = {
        'apple': 'ვაშლი',
        'banana': 'ბანანი',
        'orange': 'ფორთოხალი',
        'grape': 'ყურძენი',
        # Add more words of your choice
    }
    return dictionary

def testing(dictionary):
    correct_answers = 0
    words = list(dictionary.keys())

    number_of_questions = int(input("ᲠᲐᲛᲓᲔᲜᲘ ᲙᲘᲗᲮᲕᲘᲡ ᲓᲐᲡᲛᲐ ᲒᲡᲣᲠᲡ? "))

    for _ in range(number_of_questions):
        random_word = random.choice(words)
        correct_translation = dictionary[random_word]

        answer = input(f"ᲠᲐ ᲘᲥᲜᲔᲑᲐ ᲡᲬᲝᲠᲘ ᲗᲐᲠᲒᲛᲐᲜᲘ ᲡᲘᲢᲧᲕᲘᲡ '{random_word}'? ")

        if answer.lower() == correct_translation.lower():
            print("Correct!")
            correct_answers += 1
        else:
            print(f"ᲐᲠᲐᲐ. ᲡᲬᲝᲠᲘ ᲞᲐᲡᲣᲮᲘᲐ: {correct_translation}")

    percentage_correct = (correct_answers / number_of_questions) * 100
    print(f"\nYou ᲗᲥᲕᲔᲜ ᲡᲬᲝᲠᲔᲓ ᲣᲞᲐᲡᲣᲮᲔᲗ {correct_answers} ᲙᲘᲗᲮᲕᲐᲖᲔ, ᲡᲣᲚ ᲙᲘᲗᲮᲕᲔᲑᲘᲡ ᲠᲐᲝᲓᲔᲜᲝᲑᲐ {number_of_questions}.")
    print(f"ᲡᲬᲝᲠᲘ ᲞᲐᲡᲣᲮᲔᲑᲘ: {percentage_correct}%")

if __name__ == "__main__":
    dictionary = create_dictionary()
    testing(dictionary)
