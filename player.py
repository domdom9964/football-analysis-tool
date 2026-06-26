Save_file = "squad.json"
# All perdefined lists in the code

class Player():
    def __init__(self, name, club, position, age, goals, assists, matches, rating, market_value):
        self.name = name
        self.club = club
        self.position = position 
        self.age = age
        self.goals = goals
        self.assists = assists 
        self.matches = matches
        self.rating = rating
        self.market_value = market_value
    
    def print_player_card(self):

        print("=" * 45)                        
        print(f"  {self.name} — {self.club}")
        print(f"  Position    : {self.position}  |  Age: {self.age}")
        print(f"  Matches     : {self.matches}")
        print(f"  Goals       : {self.goals}   Assists: {self.assists}")
        print(f"  Rating      : {self.rating:.1f} / 10")
        print(f"  Market Value: {self.market_value}M")
        print("=" * 45)


    def goals_per_match(self):


        if self.matches == 0:
            return 0                             


        return round(self.goals / self.matches, 2)


    def get_contribution(self):
        return self.goals + self.assists


    def rate_player(self):

        rating = self.rating            

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
        
    def to_dict(self):
        return{
            "name": self.name,
            "club": self.club,
            "position": self.position,
            "age": self.age,
            "goals": self.goals,
            "assists": self.assists,
            "matches": self.matches,
            "rating": self.rating,
            "market_value": self.market_value,
        }
        
    @classmethod
    def from_dict(cls, data):
        return cls(
            data["name"],
            data["club"],
            data["position"],
            data["age"],
            data["goals"],
            data["assists"],
            data["matches"],
            data["rating"],
            data["market_value"]
        )
