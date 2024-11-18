from random import random, randint


class Dice:
    def roll(self):
        first = randint(1,6)
        second = randint(1,6)
        return first, second


dice = Dice()
print(dice.roll())