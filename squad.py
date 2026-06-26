import json
import os
from player import Player

starting_squad = [
    Player("Erling Haaland", "Man City", "Forward", 23, 36, 8, 35, 9.1, 200), 
    Player("Marcus Rashford", "Man United", "Forward", 26, 17, 5, 32, 7.4, 40),
    Player("Kevin De Bruyne", "Man City", "Midfielder", 32, 7, 16, 28, 8.8, 10),
    Player("Jude Bellingham", "Real Madrid", "Midfielder", 20, 23, 12, 38, 9.0, 160),
    Player("Virgil van Dijk", "Liverpool", "Defender", 32, 4, 2, 36, 8.3, 15),
    Player("Trent Alexander-Arnold", "Liverpool", "Defender", 25, 3, 13, 34, 8.1, 60),
    Player("Alisson Becker", "Liverpool", "Goalkeeper", 31, 0, 0, 36, 8.5, 15),
]     



# All definitions in the Code

def save_squad(squad):
    data = [player.to_dict() for player in squad]
    with open(Save_file, "w") as file:
        json.dump(data, file, indent=4)
    print(f"\n Squad saved to {Save_file}\n")

def load_squad():
    if not os.path.exists(Save_file):
        return starting_squad
    with open(Save_file, "r") as file:
        data = json.load(file)
    squad = [Player.from_dict(p) for p in data]
    print(f"\nSquad loaded from {Save_file}\n")
    return squad
        
        
def squad_stats(squad):
    total_players = len(squad)

  
    total_goals = 0                        
    total_assists = 0

    for player in squad:                  
        total_goals += player.goals   
        total_assists += player.assists


    top_scorer = max(squad, key=lambda p: p.goals)
    top_assist = max(squad, key=lambda p: p.assists)
    top_rated  = max(squad, key=lambda p: p.rating)
    most_expensive = max(squad, key=lambda p: p.market_value)

    avg_rating = round(sum(p.rating for p in squad) / total_players, 2)
    print(f"\nTotal Players: {total_players}")
    print(f"total_goals: {total_goals}")
    print(f"total_assists: {total_assists}")
    print(f"avg_rating: {avg_rating}")
    print(f"top_scorer: {top_scorer.name}")
    print(f"top_assist: {top_assist.name}")
    print(f"top_rated: {top_rated.name}")

    # Return all results packaged in a dictionary
    return {
        "total_players": total_players,
        "total_goals": total_goals,
        "total_assists": total_assists,
        "avg_rating": avg_rating,
        "top_scorer": top_scorer,
        "top_assist": top_assist,
        "top_rated": top_rated,
        "most_expensive":  most_expensive,
    }
   


def add_player(squad, name, club, position, age, goals, assists, matches, rating, market_value):

    new_player = Player(name, club, position, age, goals, assists, matches, rating, market_value)
    squad.append(new_player)      
    print(f"\n✅ {name} has been added to the squad!\n")#
    
def remove_player(squad, name):
    for player in squad:
        if player.name.lower() == name.lower():
            squad.remove(player)
            print(f"\n{player.name} has been succesfully removed from the squad\n")
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
        if player.name.lower() == name1.lower():
            player1 = player
        if player.name.lower() == name2.lower():
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
    gpm1 = player1.goals_per_match()   # reusing your existing function
    gpm2 = player2.goals_per_match()
    con1 = player1.get_contribution()  # reusing your existing function
    con2 = player2.get_contribution()

    # Print the comparison table
    print("\n" + "=" * 55)
    print(f"  {'CATEGORY':<20} {player1.name:<15} {player2.name}")
    print("=" * 55)

    w1, w2 = winner(player1.goals, player2.goals)
    print(f"  {'Goals':<20} {w1} {player1.goals:<12} {w2} {player2.goals}")

    w1, w2 = winner(player1.assists, player2.assists)
    print(f"  {'Assists':<20} {w1} {player1.assists:<12} {w2} {player2.assists}")

    w1, w2 = winner(con1, con2)
    print(f"  {'Contributions':<20} {w1} {con1:<12} {w2} {con2}")

    w1, w2 = winner(player1.matches, player2.matches)
    print(f"  {'Matches':<20} {w1} {player1.matches:<12} {w2} {player2.matches}")

    w1, w2 = winner(gpm1, gpm2)
    print(f"  {'Goals/Match':<20} {w1} {gpm1:<12} {w2} {gpm2}")

    w1, w2 = winner(player1.rating, player2.rating)
    print(f"  {'Rating':<20} {w1} {player1.rating:<12} {w2} {player2.rating}")

    print("=" * 55)
    print(f"  {player1.name} is rated: {player1.rate_player()}")   # reusing rate_player
    print(f"  {player2.name} is rated: {player2.rate_player()}")
    print("=" * 55 + "\n")
    
def change_market_value(squad, player1):
    for player in squad:
        if player.name.lower() == player1.lower():
            new_market_value = int(input(f"Market Value (in M):"))
            player.market_value = new_market_value
            print(f"\n {player.name} has a new Market Value of {player.market_value}M")
            save_squad(squad)
            return
