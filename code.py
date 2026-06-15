
# All perdefined lists in the code

squad = [
    {
        "name": "Erling Haaland",
        "club": "Man City",
        "position": "Forward",
        "age": 23,
        "goals": 36,
        "assists": 8,
        "matches": 35,
        "rating": 9.1,
    },
    {
        "name": "Marcus Rashford",
        "club": "Man United",
        "position": "Forward",
        "age": 26,
        "goals": 17,
        "assists": 5,
        "matches": 32,
        "rating": 7.4,
    },
    {
        "name": "Kevin De Bruyne",
        "club": "Man City",
        "position": "Midfielder",
        "age": 32,
        "goals": 7,
        "assists": 16,
        "matches": 28,
        "rating": 8.8,
    },
    {
        "name": "Jude Bellingham",
        "club": "Real Madrid",
        "position": "Midfielder",
        "age": 20,
        "goals": 23,
        "assists": 12,
        "matches": 38,
        "rating": 9.0,
    },
    {
        "name": "Virgil van Dijk",
        "club": "Liverpool",
        "position": "Defender",
        "age": 32,
        "goals": 4,
        "assists": 2,
        "matches": 36,
        "rating": 8.3,
    },
    {
        "name": "Trent Alexander-Arnold",
        "club": "Liverpool",
        "position": "Defender",
        "age": 25,
        "goals": 3,
        "assists": 13,
        "matches": 34,
        "rating": 8.1,
    },
    {
        "name": "Alisson Becker",
        "club": "Liverpool",
        "position": "Goalkeeper",
        "age": 31,
        "goals": 0,
        "assists": 0,
        "matches": 36,
        "rating": 8.5,
    },
]


# All definitions in the Code

def print_player_card(player):

    print("=" * 45)                        
    print(f"  {player['name']} — {player['club']}")
    print(f"  Position : {player['position']}  |  Age: {player['age']}")
    print(f"  Matches  : {player['matches']}")
    print(f"  Goals    : {player['goals']}   Assists: {player['assists']}")
    print(f"  Rating   : {player['rating']:.1f} / 10")
    print("=" * 45)


def goals_per_match(player):


    if player["matches"] == 0:
        return 0                             


    return round(player["goals"] / player["matches"], 2)


def get_contribution(player):
    return player["goals"] + player["assists"]


def rate_player(player):

    rating = player["rating"]            

    if rating >= 9.0:
        return "World Class"
    elif rating >= 8.0:                 
        return "Excellent"
    elif rating >= 7.0:
        return "Good"
    elif rating >= 6.0:
        return "Average"
    else:                               
        return "Needs Improvement"


def filter_by_position(squad, position):

    return [player for player in squad if player["position"] == position]


def squad_stats(squad):
    total_players = len(squad)

  
    total_goals = 0                        
    total_assists = 0

    for player in squad:                  
        total_goals += player["goals"]   
        total_assists += player["assists"]


    top_scorer = max(squad, key=lambda p: p["goals"])
    top_assist = max(squad, key=lambda p: p["assists"])
    top_rated  = max(squad, key=lambda p: p["rating"])


    avg_rating = round(sum(p["rating"] for p in squad) / total_players, 2)
    print(f"\nTotal Players: {total_players}")
    print(f"total_goals: {total_goals}")
    print(f"total_assists: {total_assists}")
    print(f"avg_rating: {avg_rating}")
    print(f"top_scorer: {top_scorer['name']}")
    print(f"top_assist: {top_assist['name']}")
    print(f"top_rated: {top_rated['name']}")

    # Return all results packaged in a dictionary
    return {
        "total_players": total_players,
        "total_goals": total_goals,
        "total_assists": total_assists,
        "avg_rating": avg_rating,
        "top_scorer": top_scorer,
        "top_assist": top_assist,
        "top_rated": top_rated,
    }
   


def add_player(squad, name, club, position, age, goals, assists, matches, rating):

    new_player = {
        "name": name,
        "club": club,
        "position": position,
        "age": age,
        "goals": goals,
        "assists": assists,
        "matches": matches,
        "rating": rating,
    }
    squad.append(new_player)      
    print(f"\n✅ {name} has been added to the squad!\n")#
    
def remove_player(squad, name):
    for player in squad:
        if player["name"].lower() == name.lower():
            squad.remove(player)
            print(f"\n{player['name']} has been succesfully removed from the squad\n")
            return
    print(f"no player named {name} is in the squad")


def compare_players(squad, name1, name2):
    """
    Finds two players by name and prints a side-by-side comparison.
    """
    # Search the squad for each player by name (case-insensitive)
    player1 = None
    player2 = None

    for player in squad:
        if player["name"].lower() == name1.lower():
            player1 = player
        if player["name"].lower() == name2.lower():
            player2 = player

    # If either name wasn't found, tell the user and stop
    if player1 is None:
        print(f"\n❌ No player named '{name1}' found in the squad.\n")
        return
    if player2 is None:
        print(f"\n❌ No player named '{name2}' found in the squad.\n")
        return

    # Helper: adds a ✅ next to whichever player wins that stat
    def winner(val1, val2):
        if val1 > val2:
            return "✅", "  "
        elif val2 > val1:
            return "  ", "✅"
        else:
            return "==", "=="   # draw

    # Calculate extra stats for comparison
    gpm1 = goals_per_match(player1)   # reusing your existing function
    gpm2 = goals_per_match(player2)
    con1 = get_contribution(player1)  # reusing your existing function
    con2 = get_contribution(player2)

    # Print the comparison table
    print("\n" + "=" * 55)
    print(f"  {'CATEGORY':<20} {player1['name']:<15} {player2['name']}")
    print("=" * 55)

    w1, w2 = winner(player1["goals"], player2["goals"])
    print(f"  {'Goals':<20} {w1} {player1['goals']:<12} {w2} {player2['goals']}")

    w1, w2 = winner(player1["assists"], player2["assists"])
    print(f"  {'Assists':<20} {w1} {player1['assists']:<12} {w2} {player2['assists']}")

    w1, w2 = winner(con1, con2)
    print(f"  {'Contributions':<20} {w1} {con1:<12} {w2} {con2}")

    w1, w2 = winner(player1["matches"], player2["matches"])
    print(f"  {'Matches':<20} {w1} {player1['matches']:<12} {w2} {player2['matches']}")

    w1, w2 = winner(gpm1, gpm2)
    print(f"  {'Goals/Match':<20} {w1} {gpm1:<12} {w2} {gpm2}")

    w1, w2 = winner(player1["rating"], player2["rating"])
    print(f"  {'Rating':<20} {w1} {player1['rating']:<12} {w2} {player2['rating']}")

    print("=" * 55)
    print(f"  {player1['name']} is rated: {rate_player(player1)}")   # reusing rate_player
    print(f"  {player2['name']} is rated: {rate_player(player2)}")
    print("=" * 55 + "\n")
        
        
def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. view full squad")
        print("2. view squad stats")
        print("3. add a new player")
        print("4. view players by position")
        print("5. compare two players")
        print("6. delete a player")
        print("7. exit")
            
        choice = input("Enter your choice (1-7):")
            
        if choice == "1":
            print("\nFULL SQUAD\n")
            for player in squad:
                print_player_card(player)
        elif choice == "2":
            print("\nSquad Stats\n")
            squad_stats(squad)
        elif choice == "3":
            print(f"\nAdd Player\n")
            name = input(f"Name:")
            club = input(f"Club:")
            position = input(f"position:") 
            age = int(input(f"Age:"))
            goals = int(input(f"Goals"))
            assists = int(input(f"Assists:"))
            matches = int(input(f"Matches:"))
            rating = float(input(f"Rating:"))
            add_player(squad, name, club, position, age, goals, assists, matches, rating)
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
                if player["position"] == position:
                    print(f"\n{player['name']}")
        elif choice == "5":
            print("\nCompare Players\n")
            for player in squad:
                print(f"  - {player['name']}")   # show squad so user knows available names
            name1 = input("\nEnter first player name: ")
            name2 = input("Enter second player name: ")
            compare_players(squad, name1, name2)
        elif choice == "6":
            print(f"\n Delete Player\n")
            for player in squad:
                print(f" -{player['name']}")
            name = input("\nPlayer to remove from the squad: ")
            remove_player(squad, name)
        elif choice == "7":
            print("Exiting. Goodbye!")
            break
        else:
            print(f"\nyour input {choice} is not an available option pick again!\n")
                
# The actual code

main_menu()
