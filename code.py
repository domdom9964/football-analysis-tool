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
    print(f"\n✅ {name} has been added to the squad!\n")




    
def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. view full squad")
        print("2. view squad stats")
        print("3. add a new player")
        print("4. view players by position")
        print("5. compare two players")
        print("6. exit")
            
        choice = input("Enter your choice (1-6):")
            
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
        elif choice == "6":
            print("Exiting. Goodbye!")
            break
        else:
            print(f"\nyour input {choice} is not an available option pick again!\n")
                
# The actual code

main_menu()
