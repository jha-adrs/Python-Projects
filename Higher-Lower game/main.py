from random import shuffle
from art import logo,vs
from game_data import data
play=True
score=0
shuffle(data)
print(logo)

for i in range(0,len(data)-1) :
    print(data[i]['name'] , data[i]['description'], data[i]["country"], sep='\n')
    print(vs)
    print(data[i+1]['name'], data[i]['description'], data[i+1]["country"], sep='\n')
    choice = input("Enter h or l\n")
    if choice=='h' :
        if (data[i]['follower_count'] < data[i+1]['follower_count'] ):
            score+=1
        else :
            print(f'Your score is {score}')
            break
    elif choice =='l':
        if (data[i]['follower_count'] > data[i + 1]['follower_count']):
            score+=1
        else :
            print(f'Your Score was {score}')
            break
