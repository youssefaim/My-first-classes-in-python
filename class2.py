class Player():
    def __init__(self, name, age, post, club, nationality, ovr, rank):
        # Initialize the Player object with the provided parameters
        self.name = name
        self.age = age
        self.post = post
        self.rank = rank
        self.club = club
        self.nationality = nationality
        self.ovr = ovr
    
    def info(self):
        # Display information about the player
        print("{}, aged {}, plays as a {}, currently with {}. The {} player boasts an impressive overall {} rating, and his ranking is {}.".format(self.name, self.age, self.post, self.club, self.nationality, self.ovr, self.rank))
    
    # The following methods are commented out because they are not implemented in the code
    # def passs():
    # def shoot():
    # def jump():
    # def run():
    # def dribble():
    # ...

# Create instances of the Player class
player1 = Player("Ronaldo", 24, "ST", "Real Madrid", "Portugal", 91, 1)
player2 = Player("Erling Haaland", 23, "ST", "Manchester City", "Norwegian", 91, 2)
player3 = Player("Luka Modric", 32, "CM", "Real Madrid", "croitian", 91, 3)

# Display information about each player
player1.info()
player2.info()
player3.info()