import random

user_wins = 0
computer_wins = 0

input_choices = {1 : 'rock', 2 : 'paper', 3 : 'scissors'}

def userinput():
    while True:
        user_input = input("Type Rock/Paper/Scissors or Q to quit.\n>>>").lower()
        match user_input:
            case "rock":
                return user_input
                break
            case "paper":
                return user_input
                break
            case "scissors":
                return user_input
                break
            case "q":
                quit()
            case _:
                print("Invalid input. Try again.\n")

def game(computer_wins, user_wins):
    while True:
        user_input = userinput()
        computer_input = random.randrange(1, 4)
        computer_choice = input_choices[computer_input]
        print(f'The computer says... {computer_choice}\n')
        print(user_input)
        if user_input == 'rock':
            match computer_choice:
                case 'rock':
                    print('Draw\n')
                case 'paper':
                    print('Paper beats rock. You lose!\n')
                    computer_wins += 1
                    score(computer_wins, user_wins)
                case 'scissors':
                    print('Rock beats scissors. You win!\n')
                    user_wins += 1
                    score(computer_wins, user_wins)
        elif user_input == 'paper':
            match computer_choice:
                case 'rock':
                    print('Paper beats rock. You Win!\n')
                    user_wins += 1
                    score(computer_wins, user_wins)
                case 'paper':
                    print('Draw\n')
                case 'scissors':
                    print('Scissors beats paper. You lose!\n')
                    computer_wins += 1
                    score(computer_wins, user_wins)
        elif user_input == 'scissors':
            match computer_choice:
                case 'rock':
                    print('Rock beats scissors. You lose!\n')
                    computer_wins += 1
                    score(computer_wins, user_wins)
                case 'paper':
                    print('Scissors beats paper. You win!\n')
                    user_wins += 1
                    score(computer_wins, user_wins)
                case 'scissors':
                    print('Draw\n')

def score(computer_wins, user_wins):
    print(f'You have {user_wins} win(s). The Computer has {computer_wins} win(s).\n')

if __name__ == '__main__':
    game(computer_wins, user_wins)