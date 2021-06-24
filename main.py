# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 23:39:38 2021

@author: Admin
"""
import random

playerscore = 0

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


def mainexit():
    global playerscore
    print(playerscore)


def checksnakeandladder():
    global playerscore
    checkladder = True

    for snake in snakes:
        if playerscore in snake.keys():
            playerscore = snake[playerscore]
            checkladder = False
            break

    if checkladder:
        for ladder in ladders:
            if playerscore in ladder.keys():
                playerscore = ladder[playerscore]
                break

    mainexit()


if __name__ == "__main__":
    while playerscore < 100:
        dicevalue = random.randint(1, 6)
        if playerscore + dicevalue <= 100:
            playerscore = playerscore + dicevalue
            checksnakeandladder()
        else:
            pass
