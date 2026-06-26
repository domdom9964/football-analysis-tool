from player import Player
from squad import load_squad, save_squad, add_player, squad_stats, remove_player, compare_players, change_market_value

def main_menu():
    
    squad = load_squad()
    
    while True:
        print("\nMain Menu:")
        print("1. view full squad")
        print("2. view squad stats")
        print("3. add a new player")
        print("4. view players by position")
        print("5. compare two players")
        print("6. delete a player")
        print("7. save squad")
        print("8. change Market value")
        print("9. exit")
            
        choice = input("Enter your choice (1-9):")
            
        if choice == "1":
            print("\nFULL SQUAD\n")
            for player in squad:
                player.print_player_card()
        elif choice == "2":
            print("\nSquad Stats\n")
            squad_stats(squad)
        elif choice == "3":
            print(f"\nAdd Player\n")
            name = input(f"Name:")
            club = input(f"Club:")
            position = input(f"position:") 
            age = int(input(f"Age:"))
            goals = int(input(f"Goals:"))
            assists = int(input(f"Assists:"))
            matches = int(input(f"Matches:"))
            rating = float(input(f"Rating:"))
            market_value =int(input(f"Market Value:"))
            add_player(squad, name, club, position, age, goals, assists, matches, rating, market_value)
        elif choice == "4":
            print (f"1: Forward\n 2: Middfielder\n 3: Defender\n 4: Goalkeeper")
            position = str(input(f"\nPosition (1-4) :"))
            position_map = {
                "1": "Forward",
                "2": "Midfielder",
                "3": "Defender",
                "4": "Goalkeeper"
            }
            position = position_map.get(position)
            for player in squad:
                if player.position == position:
                    print(f"\n{player.name}")
        elif choice == "5":
            print("\nCompare Players\n")
            for player in squad:
                print(f"  - {player.name}")  
            name1 = input("\nEnter first player name: ")
            name2 = input("Enter second player name: ")
            compare_players(squad, name1, name2)
        elif choice == "6":
            print(f"\n Delete Player\n")
            for player in squad:
                print(f" -{player.name}")
            name = input("\nPlayer to remove from the squad: ")
            remove_player(squad, name)
        elif choice == "7":
            save_squad(squad)
            print(f"Squad has been succesfully saved")
        elif choice == "8":
            print(f"\nChange Market Value")
            for player in squad:
                print(f"-{player.name}")
            player = input(f"choose a Player to change the Market value:")
            change_market_value(squad, player)
        elif choice == "9":
            save_squad(squad)
            print("Exiting. Goodbye!")
            break
        else:
            print(f"\nyour input {choice} is not an available option pick again!\n")
