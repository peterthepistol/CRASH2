#player class = needs more attributes

class Player:
    def __init__(self, name, overall_winnings, games_won,):
        self.name = name
        self.overall_winnings = overall_winnings
        self.games_won = games_won
    
    def __repr__(self):
        return f"{self.name} {self.overall_winnings} {self.games_won}"
        

#players are currently coded here but need to work out how to draw names from a table using SQL
player1 = Player("Pete", 200, 19)
player2 = Player("Azz", 180, 15)
player3 = Player('Wez', 110, 10)

print(f'{player1} \n {player2} \n {player3}')
