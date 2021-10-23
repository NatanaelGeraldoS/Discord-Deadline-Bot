import random

Label :
secret_number = random.randint(1, 10)

print('=' * 40)
print('Welcome to "Guess a Number" Game!')
print('=' * 40)

maximum_try = 3
for trying in range(maximum_try):
    answer = int(input(f'\n[trying {trying + 1}] Write Number: '))

    if answer == secret_number:
        print('Correct Answer!')
        question = input("“Would you like another game? Type y or n: ")
        break
    else:
        print(
            'Your Guess is too',
            'low' if answer < secret_number else 'high'
        )
else:
    print(f'\nThe Correct Answer Is {secret_number}!')
    question = input("“Would you like another game? Type y or n: ")
    if question == "n":
        print("Thank You For Playing!")
    elif question == "y":
        secret_number = random.randint(1, 10)
        print('=' * 40)
        print('Welcome to "Guess a Number" Game!')
        print('=' * 40)

        maximum_try = 3
        for trying in range(maximum_try):
            answer = int(input(f'\n[trying {trying + 1}] Write Number: '))

            if answer == secret_number:
                print('Correct Answer!')
                break
            else:
                print(
                    'Your Guess is too',
                    'low' if answer < secret_number else 'high'
                )
        else:
            print("Restart the program if you want to play again!")
