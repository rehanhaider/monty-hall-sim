"""
# --*-- coding:utf-8 --*--
# Simulation of monty hall problem
# Author: Rehan Haider
"""
import random


class Game:
    def __init__(self):
        # Initialize the doors
        self.doors = [1, 2, 3]
        self.prize = random.choice(self.doors)

    def close_door(self, choice):
        # Close the door that is not the choice
        for door in self.doors:
            if door != choice and door != self.prize:
                self.doors.remove(door)


class Player:
    def __init__(self):
        self.choice = None

    def make_choice(self, game):
        self.choice = random.choice(game.doors)
        return self.choice


def play():
    game = Game()
    player = Player()

    choice = player.make_choice(game)

    # Remove the door without the prize
    game.close_door(choice)

    # Change the choice
    if choice != game.prize:
        return "win"
    else:
        return "lose"


def main():
    wins = 0
    for i in range(100000):
        result = play()
        if result == "win":
            wins += 1

    print(f"Wins %: {wins / 100000 * 100}")


if __name__ == "__main__":
    main()
