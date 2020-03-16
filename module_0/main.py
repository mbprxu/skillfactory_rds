import random


class UnknownNumber():
    """ keeps random value; can give hints """
    def __init__(self, min=0, max=99):
        assert min <= max
        self.number = random.randint(min, max)
        self.min = min
        self.max = max

    def guess(self, number):
        if self.number > number:
            return "more"
        elif self.number < number:
            return "less"
        else:
            return "equal"


def game(secret):
    """ binary search implementation; returns number of attempt """
    attempts = 0
    left = secret.min
    right = secret.max
    guessed = False
    while not guessed:
        attempts += 1
        predict = (right + left) // 2
        answer = secret.guess(predict)
        if answer == "less":
            right = predict - 1
        elif answer == "more":
            left = predict + 1
        elif answer == "equal":
            guessed = True
        else:
            raise Exception
    return attempts


def game_score(game, n=10000):
    assert n > 0
    random.seed(1)
    sum = 0
    for i in range(n):
        sum += game(UnknownNumber())
    return sum / n


print("Score = {}".format(game_score(game)))
