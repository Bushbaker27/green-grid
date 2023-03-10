from Lib import Game
import threading
from Lib.ReceiveSMS import runApp, runGame


def main():
    # Make a game and start it
    game = Game.Game()
    game.start_game()

if __name__ == '__main__':
    # Multi-thread our flask app and our application
    t1 = threading.Thread(target=runApp).start()
    t2 = threading.Thread(target=runGame).start()

