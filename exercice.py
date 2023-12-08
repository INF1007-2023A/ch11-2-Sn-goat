"""
Chapitre 11.3
"""


import math
from inspect import *

from game import *
from character import *
from spells import *


def simulate_battle():
	sergile = Character("Sergile", 1000, 100, 150, 88)
	sergile.main_move = DrainingMove("Soul Taker", 55, 60, 0.20)
	sergile.secondary_move = IntensifyingMove("Uppy upp attack", 20, 70, 30)
	chris = Character("Chris", 1200, 90, 100, 80)
	chris.main_move = DrainingMove("Soul Breaker", 70, 70, 0.15)
	chris.secondary_move = IntensifyingMove("Big Ups", 30, 70, 30)

	turns = run_battle(sergile, chris)
	print(f"The battle ended in {turns} turns.")


def main():
	simulate_battle()

if __name__ == "__main__":
	main()

