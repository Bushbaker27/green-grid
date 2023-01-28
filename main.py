from Lib import Game
from Lib import Grid
def main():
    # Make a game and start it
    game = Game.Game()
    game.start_game()

if __name__ == '__main__':
    wow = sorted(["asparagus",
        "beans",
        "beets",
        "broccoli",
        "cabbage",
        "radishes",
        "squash",
        "strawberries",
        "zucchini",
        "corn",
        "pumpkin",
        "basil",
        "carrots",
        "onions",
        "potatoes",
        "tomatoes"])
    print(wow)
    main()

