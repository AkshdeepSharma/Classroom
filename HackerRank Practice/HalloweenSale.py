#!/bin/python3
import sys

def howManyGames(p, d, m, s):
    num_games = 0
    while s >= 0:
        s -= p
        if p - d >= m:
            p -= d
        else:
            p = m
        num_games += 1
    return num_games - 1


if __name__ == "__main__":
    p, d, m, s = input().strip().split(' ')
    p, d, m, s = [int(p), int(d), int(m), int(s)]
    answer = howManyGames(p, d, m, s)
    print(answer)