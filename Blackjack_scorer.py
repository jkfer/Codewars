# https://www.codewars.com/kata/534ffb35edb1241eda0015fe
# 5kyu

"""
Scoring rules:
Number cards count as their face value (2 through 10).
Jack, Queen and King count as 10. An Ace can be counted as either 1 or 11.
Return the highest score of the cards that is less than or equal to 21.
If there is no score less than or equal to 21 return the smallest score
more than 21.
"""


def score_hand(cards):
    ans = 0
    A_count = 0
    for char in cards:
        if char in "JQK":
            ans += 10
        elif char == "A":
            A_count += 1
        else:
            ans += int(char)

    for a in range(A_count):
        if ans + 11 < 21:
            ans += 11
        elif a == A_count-1 and ans == 10:
            ans += 11
        else:
            ans += 1

    return ans


print(score_hand(['A', 'A', 'A', 'J']))
