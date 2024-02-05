
import random
import time

def blackjack():
    print(f"{'*':*^79}")
    while True:
        try:
            start_game=input("Would you like to play? (y/n): ").upper()
            if start_game not in {'Y','N'}:
                raise ValueError
            else:
                break
        except ValueError:
            print("You must input Y or N!")
            continue
    if start_game in {'Y','N'}:
        if start_game=='Y':
            while start_game=="Y":
                twenty_one=21
                print(f"{'*':*^79}")
                print('Welcome to Black Jack.')
                print(f"{'*':*^79}")
                cards=[2,3,4,5,6,7,8,9,10,'J','Q','K','A']
                face_cards={'J':10,'Q':10,'K':10}
                ace_card={'A1':1,'A11':11}
                dealer_card=[]
                player_card=[]
                dealer=[]
                player=[]
                x="H"
                my_answer=None

                def draws(user):
                    random_index=random.randint(0,len(cards)-1)
                    random_number=cards[random_index]
                    if random_number in {'J','Q','K'}:
                        user.append(face_cards[random_number])
                        if user==player:
                            player_card.append(random_number)
                        else:
                            dealer_card.append(random_number)
                    elif random_number=='A':
                        if sum(user)<=10:
                            user.append(ace_card.get('A11'))
                            if user==player:
                                player_card.append(random_number)
                            else:
                                dealer_card.append(random_number)
                        else:
                            user.append(ace_card.get('A1'))
                            if user==player:
                                player_card.append(random_number)
                            else:
                                dealer_card.append(random_number)
                    else:
                        user.append(random_number)
                        if user==player:
                            player_card.append(random_number)
                        else:
                            dealer_card.append(random_number)

                def print_function():
                    player_sum=sum(player)
                    dealer_sum=sum(dealer)
                    hidden_card=dealer[0]
                    if player_sum<=21 and len(dealer)<=2:
                        if player_sum==21:
                            print(f"You have a total of {player_sum} and the dealer has {dealer_sum}.")   
                        else:
                            print(f"You have a total of {player_sum} and the dealer has {hidden_card} and a hidden card.")          
                    if player_sum>21 and len(dealer)==2:
                        print(f"You have a total of {player_sum} and the dealer has {dealer_sum}.")
                    if player_sum<=21 and len(dealer)>2:
                        print(f"You have a total of {player_sum} and the dealer has {dealer_sum}.")  
                
                def dealer_move():
                    time.sleep(2)
                    print(f"The dealer reveals the hidden card of {dealer[1]} and has a total of {sum(dealer)}.")
                    time.sleep(2)
                    while sum(dealer)<=16:  
                        draws(dealer)
                        print(f"The Dealer draws a {dealer_card[-1]}.")
                        time.sleep(2)
                        print_function()
                        time.sleep(2)
                    if sum(dealer)<=twenty_one:
                        print("Dealer Stands.")
                    else:
                        print("Dealer Busts!") 

                def player_move():
                    nonlocal my_answer
                    while my_answer not in {"H","S"}:
                        try: 
                            my_answer=input("Hit or stand? (h/s): ").upper()
                            if my_answer not in {"H","S"}:
                                raise ValueError
                        except ValueError:
                            print("You can only enter H or S! Try Again.")
                            continue                    
                                      
                def game(*users):
                    for user in users:
                        while len(user)<2:
                            draws(user)
                    for user in users:
                        if user==player:
                            time.sleep(1)      
                            print(f"The player draws a {player_card[0]} and a {player_card[1]}.")   
                        else:
                            time.sleep(1)  
                            print(f"The dealer draws a {dealer_card[0]} and a hidden card.")
                    if sum(player)==21:
                        time.sleep(1) 
                        print('You Stand')
                        dealer_move()
                    else:    
                        nonlocal my_answer
                        player_move()
                        while my_answer==x:
                            if sum(player)==twenty_one:
                                print_function()
                                break
                            elif sum(player)<twenty_one:
                                draws(player)
                                time.sleep(2)
                                print(f"You draw a {player_card[-1]}.")
                                print_function()
                                if sum(player)>twenty_one:
                                    print("You Bust!")
                                    time.sleep(2)
                                    print("Dealer wins!")
                                    break
                                if sum(player)==twenty_one:
                                    break
                            else:
                                print("Dealer wins!")
                                break
                            my_answer=None
                            player_move()
                        if sum(player)<=twenty_one:
                            dealer_move()

                def end_game():
                    time.sleep(2)
                    if sum(player)<=twenty_one:
                        if sum(player)>sum(dealer):
                            print("You Win!")
                        elif sum(player)<sum(dealer):
                            if sum(dealer)<=twenty_one:
                                print("Dealer Wins!")
                            else:
                                print("Youn Win!")
                        else:
                            print("Dealer Wins!")
                game(player,dealer)
                end_game()
                while True:
                    try:
                        start_game=input("Would you like to play again? (y/n): ").upper()
                        if start_game not in {'Y','N'}:
                            raise ValueError
                        else:
                            break
                    except ValueError:
                        print("You must input Y or N!")
                        continue
        else:
            print('Goodbye!')
    print("See you again!")
            
blackjack()

 
                