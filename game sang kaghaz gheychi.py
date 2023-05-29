import random

choices = ['r', 'p', 's']

choice_meaning = {
    'r': 'Rock',
    'p': 'Paper',
    's': 'Scissors'
}

user_score = 0
ai_score = 0

i = 0

while i < 4:
#User
    user_choice = input('Select From Rock, paper, Scissors: (r, p, s) ')

    #Ai 
    ai_choice = random.choice(choices)


    #Ifs
    if user_choice in choices:
        print(f'your choice ({choice_meaning[user_choice]}) , AI choice ({choice_meaning[ai_choice]})')
        if user_choice == ai_choice:
            print('Tie')
        elif (user_choice == 'r' and ai_choice == 's') or (user_choice == 'p' and ai_choice == 'r') or (user_choice == 's' and ai_choice == 'p'):
            print('user +1!')
            user_score += 1
        else:
            print('ai +1!')
            ai_score += 1
    else:
        print('Invalid Choice')
        i -= 1

    print(f'user score {user_score} / ai score {ai_score}')

    print('\n', '-'*15, '\n')  
    
    i += 1


if user_score > ai_score:
    print(f'score user = {user_score} , score Ai = {ai_score}')
    print('user win!')
elif user_score < ai_score:
    print(f'score user = {user_score} , score Ai = {ai_score}')
    print('ai win!')
else:
    print(f' It \'s a tie. score : {user_score}')