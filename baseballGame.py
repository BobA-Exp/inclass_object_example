#! Baseball Game
class BaseballGame:
    #! Attributes
    def __init__(self, home_team, away_team):
        self.home_team = home_team
        self.away_team = away_team
        self.home_score = 0
        self.away_score = 0
        self.inning = 1
        self.top_bottom = "top"
        self.outs = 0
        self.balls = 0
        self.strikes = 0
        self.hits = 0
        self.errors = 0

    #! Methods
    def get_home_team(self):
        print(f"Home team: {self.home_team}")
    
    def get_away_team(self):
        print(f"Away team: {self.away_team}")
    
    def get_home_score(self):
        print(f"Home score: {self.home_score}")
    
    def get_away_score(self):
        print(f"Away score: {self.away_score}")
    
    def get_inning(self):
        print(f"Inning: {self.inning}")

    def get_top_bottom(self):
        print(f"Top/Bottom: {self.top_bottom}")

    def get_outs(self):
        print(f"Outs: {self.outs}")

    def get_balls(self):
        print(f"Balls: {self.balls}")

    def get_strikes(self):
        print(f"Strikes: {self.strikes}")

    def get_hits(self):
        print(f"Hits: {self.hits}")

    def get_errors(self):
        print(f"Errors: {self.errors}")