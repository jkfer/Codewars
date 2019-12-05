# https://www.codewars.com/kata/550f22f4d758534c1100025a
# 5 kyu


import re


def dirReduc(arr):
    S = " ".join(arr)

    while ("NORTH SOUTH" in S) or ("SOUTH NORTH" in S) or \
            ("EAST WEST" in S) or ("WEST EAST" in S):
        for n in ["NORTH SOUTH", "SOUTH NORTH", "EAST WEST", "WEST EAST"]:
            if n in S:
                S = re.sub(n, "", S)

                # correct an spaces
                S = re.sub(" {2,}", " ", S)

                # Trim leading or ending spaces
                S = S.strip()

    return S.split()


print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))
