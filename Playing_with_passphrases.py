# https://www.codewars.com/kata/playing-with-passphrases/train/python


def play_pass(s, n):
    letts = 'abcdefghijklmnopqrstuvwxyz'.upper()

    k = len(s) - 1
    S = [None] * (k+1)
    for i, char in enumerate(s):
        if char.isalpha():
            nn = (letts.index(char) + n) % 26
            if i % 2 == 0:
                char = letts[nn]
            else:
                char = letts.lower()[nn]

        if char.isdigit():
            char = 9 - int(char)

        S[k-i] = str(char)

    return "".join(S)


print(play_pass("THIS IS A TES? STRING 4885!!!", 17))
