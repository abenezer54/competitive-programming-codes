import sys
import math, heapq, random
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n, k = IL()
    a = IL()
    initial_number_of_cards = sum(a)
    maximum_card_value = max(a)
    tot = initial_number_of_cards + k
    for size in range(n, 0, -1):
        # (size * number_of_deck) %  size == total number of cards
        # so find total possible number of card by removing the remainder
        # we want to maximize number of deck since it prevents from having duplicates on one deck
        possible_number_of_card = tot - (tot % size)
        if possible_number_of_card >= initial_number_of_cards: 
            number_of_deck = possible_number_of_card // size
            if maximum_card_value <= number_of_deck:
                print(size)
                return
    

    

for _ in range(II()):
    solve()
