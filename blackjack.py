#Blackjack project
#VinayRatnam 09/20/23
import p1_random as p1

#define variables
rng = p1.P1Random()
number_of_games_played = 0
dealer_wins = 0
player_wins = 0
player_hand = 0
ties = 0

print("START GAME #1\n")
continue_game = True
while continue_game:
    #deal player card
    card_name = 0
    player_card = rng.next_int(13) + 1
    if player_card == 1:
        card_name = "ACE"
    elif player_card == 11:
        card_name = "JACK"
        player_card = 10
    elif player_card == 12:
        card_name = "QUEEN"
        player_card = 10
    elif player_card == 13:
        card_name = "KING"
        player_card = 10
    else:
        card_name = player_card

    #print player card and hand
    if type(player_card) is str:
        print("Your card is a " + card_name + "!")
    else:
        print(f"Your card is a {card_name}!")
    player_hand = player_hand + player_card
    print(f"Your hand is: {player_hand}\n")

    #create scenarios for when player hand is 21 or exceeds 21
    if player_hand == 21:
        print("BLACKJACK! You win!\n")
        player_wins += 1
        number_of_games_played += 1
        player_hand = 0
        current_game = number_of_games_played + 1
        print(f"START GAME #{current_game}\n")
        continue
    elif player_hand > 21:
        print("You exceeded 21! You lose.\n")
        dealer_wins += 1
        number_of_games_played += 1
        player_hand = 0
        current_game = number_of_games_played + 1
        print(f"START GAME #{current_game}\n")
        continue

    #create loop for player's options
    condition = True
    while condition:
        print("1. Get another card\n"
              "2. Hold Hand\n"
              "3. Print statistics\n"
              "4. Exit\n")
        player_option = int(input("Choose an option: ")) #Ask player what they want to do
        print()
        #exit nested loop for option 1
        if player_option == 1:
            break
        elif player_option == 2: #create output for holding hand
            dealer_hand = rng.next_int(11) + 16
            if player_hand > dealer_hand: #create outputs for when player wins by greater hand
                print(f"Dealer's hand: {dealer_hand}")
                print(f"Your hand is: {player_hand}\n")
                print("You win!\n")
                player_wins += 1
            elif player_hand < dealer_hand and dealer_hand > 21:
                print(f"Dealer's hand: {dealer_hand}")
                print(f"Your hand is: {player_hand}\n")
                print("You win!\n")
                player_wins += 1
            elif player_hand < dealer_hand and dealer_hand <= 21: #create output for when dealer wins
                print(f"Dealer's hand: {dealer_hand}")
                print(f"Your hand is: {player_hand}\n")
                print("Dealer wins!\n")
                dealer_wins += 1
            elif player_hand == dealer_hand: #create output for tie game
                print(f"Dealer's hand: {dealer_hand}")
                print(f"Your hand is: {player_hand}\n")
                print("It's a tie! No one wins!\n")
                ties += 1
            number_of_games_played += 1
            player_hand = 0
            current_game = number_of_games_played + 1
            print(f"START GAME #{current_game}\n")
            break
        elif player_option == 3: #print out statistics
            print(f"Number of Player wins: {player_wins}")
            print(f"Number of Dealer wins: {dealer_wins}")
            print(f"Number of tie games: {ties}")
            print(f"Total # of games played is: {number_of_games_played}")
            win_percentage = (player_wins / number_of_games_played) * 100
            print(f"Percentage of Player wins: {win_percentage}%\n")
        elif player_option == 4: #create output for when player exits program
            continue_game = False
            break
        else:
            print("Invalid input!")
            print("Please enter an integer value between 1 and 4.\n")
            continue