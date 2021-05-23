import random
game=['rock','paper','scissor']
a=0
b=0
def score():
    print(f'Computer scores : {a}')
    print(f'User Scores : {b}')
    if a==b:
        print('Its A Tie')
    elif a>b:
        print('Computer Wins')
    elif a<b:
        print('You Win')
while True:
    computer = random.choice(game)
    user=input('Choose - (Rock,Paper,Scissor (Press any key to exit)): ')
    if user.lower()==computer:
        print('You both have Chosen {},Try again'.format(user.upper()))
    elif user.lower()=='rock':
        if computer=='paper':
            print('Computer Choose Paper')
            print('You Choose Rock , You LOSE')
#            print('PAPER covers ROCK , You LOSE')
            a+=1
        elif computer=='scissor':
            print('Computer Choose Scissor')
            print('You Choose Rock , You WIN')
#            print('ROCk smashes SCISSOR , You WIN')
            b+=1
    elif user.lower()=='paper':
        if computer=='scissor':
            print('Computer Choose Scissor')
            print('You Choose Paper , You LOSE')
#            print('SCISSOR cuts PAPER , You LOSE')
            a+=1
        elif computer=='rock':
            print('Computer Choose Rock')
            print('You Choose Paper , You WIN')
#            print('PAPER covers ROCK , You WIN')
            b+=1
    elif user.lower() == 'scissor':
        if computer == 'paper':
            print('Computer Choose Paper')
            print('You Choose Scissor , You WIN')
#            print('SCISSOR cuts PAPER , You WIN')
            b+=1
        elif computer=='rock':
            print('Computer Choose Rock')
            print('You Choose Scissor , You LOSE')
#            print('ROCk smashes SCISSOR , You LOSE')
            a+=1
    else:
        print('Choose from (Rock,Paper,Scissor) only')
        res = input('Want to continue ? (Y/N) : ')
        if res.upper() == 'N':
            break
score()