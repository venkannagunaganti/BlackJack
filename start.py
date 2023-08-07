import  random
import art,os
# print(art.logo)
play_game=False
your=input("do you want to play the game: ")
if your=='y':
    play_game=True



def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return  card
user_cards=[]
computer_cards=[]
user_score=0
computer_score=0
is_game_over=False
for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
# print(f"{user_cards} {computer_cards}")
#calculating sum of cards
def calculate_score(cards):
    """this takes cards as input and returns corresponding sum value of it"""
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(user_score,computer_score):
    if user_score>21 and computer_score>21:
        return "you lose"
    elif computer_score==0:
        return "you lose,opponent has blackjack"
    elif user_score==computer_score:
        return "draw"
    elif user_score==0:
        return "you win as you have a blackjack"
    elif user_score>21:
        return "you lose as you exceeds"
    elif computer_score>21:
        return "you win as opponent exceeds"
    elif user_score<computer_score:
        return "you lose because your score less than computer score"
    else:
        return "you lose"



while play_game:
    print(art.logo)
    while not is_game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print((f"computer first card is: {computer_cards[0]}"))
        print(f"user cards are: {user_cards}, and score is: {user_score}")

        if user_score==0 or computer_score==0 or user_score>21:
            is_game_over=True
        else:
            user_choice=input("chose 'y' to continue and 'n' to stop the game: ")
            if user_choice=='y':
                os.system("cls")
                user_cards.append(deal_card())

            else:
                is_game_over=True
    while computer_score!=0 and computer_score<21:
        computer_cards.append(deal_card())
        computer_score=calculate_score(computer_cards)
    print(f"your final hand:{user_cards}, score:{user_score}")
    print(f"computer's final hand:{computer_cards}, score:{computer_score}")
    print(compare(user_score,computer_score))
    play_game=False