# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 23:39:38 2021

@author: Admin
"""
import random
from termcolor import colored

PLAYER_SCORE = 0

snakes = [
    {15: 12},
    {45: 30},
    {80: 20},
]

ladders = [
    {52: 67},
    {28: 76},
    {1: 38}
]


def snake_ladder(player_score):
    """
    Parameters
    ----------
    player_score : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    check_ladder = True

    for snake in snakes:
        if player_score in snake.keys():
            player_score = snake[player_score]
            check_ladder = False
            print(colored("Snake Found Demoted to " + str(player_score), "red"))
            break

    if check_ladder:
        for ladder in ladders:
            if player_score in ladder.keys():
                player_score = ladder[player_score]
                print(colored("Ladder Found Promoted to " + str(player_score), "green"))
                break

    return player_score


if __name__ == "__main__":
    while PLAYER_SCORE < 100:
        DICE_VALUE = random.randint(1, 6)
        print("The Diced", DICE_VALUE)
        if PLAYER_SCORE + DICE_VALUE <= 100:
            PLAYER_SCORE = PLAYER_SCORE + DICE_VALUE
            PLAYER_SCORE = snake_ladder(PLAYER_SCORE)
            print("The Player Score", PLAYER_SCORE)
        else:
            pass
