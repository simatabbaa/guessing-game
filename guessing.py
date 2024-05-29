import random

# List of animals and their facts
animals = {
    "elephant": ["It is a large animal.", "It has a trunk.", "It is found in Africa or Asia."],
    "cat": ["It is a small animal.", "It is a common household pet.", "It meows."],
    "dolphin": ["It is a marine animal.", "It is known for being intelligent.", "It lives in the ocean."],
    "eagle": ["It is a bird.", "It has sharp eyesight.", "It is known for its strength."]
}

def get_fact(animal, fact_index):
    return animals[animal][fact_index]

def user_guess():
    attempts = 0
    animal = random.choice(list(animals.keys()))
    print("The computer has picked an animal from the following list:", ", ".join(animals.keys()))

    while True:
        guess = input("Guess the animal: ").strip().lower()
        attempts += 1
        if guess == animal:
            print(f"Correct! You guessed it in {attempts} attempts.")
            break
        else:
            fact_index = attempts % len(animals[animal])
            print("Incorrect. Here's a fact about the animal:", get_fact(animal, fact_index))

def computer_guess():
    attempts = 0
    low, high = 0, len(animals) - 1
    animal_list = list(animals.keys())
    fact_index = 0

    print("Think of an animal from the following list:", ", ".join(animal_list))
    input("Press Enter when you are ready...")

    while low <= high:
        mid = (low + high) // 2
        guess = animal_list[mid]
        attempts += 1
        response = input(f"Is it a(n) {guess}? (yes/no): ").strip().lower()

        if response == "yes":
            print(f"The computer guessed your animal in {attempts} attempts!")
            break
        elif response == "no":
            if fact_index < len(animals[guess]):
                print("Here's a fact about the guessed animal:", get_fact(guess, fact_index))
                fact_index += 1
            correct_response = input("Is it too low or too high? (low/high): ").strip().lower()
            if correct_response == "low":
                low = mid + 1
            elif correct_response == "high":
                high = mid - 1
            else:
                print("Please respond with 'low' or 'high'.")

def main():
    print("Welcome to the Animal Guessing Game!")
    mode = input("Who will guess the animal? (user/computer): ").strip().lower()

    if mode == "user":
        user_guess()
    elif mode == "computer":
        computer_guess()
    else:
        print("Invalid option. Please choose 'user' or 'computer'.")

if __name__ == "__main__":
    main()