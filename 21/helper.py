buttonA = 10

"""
keypad layout:
+---+---+---+
| 7 | 8 | 9 |
+---+---+---+
| 4 | 5 | 6 |
+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
    | 0 | A |
    +---+---+
"""
neededMove = {
    (10, 0): -1+0j, (10, 1): -2+1j, (10, 2): -1+1j, (10, 3): 0+1j, 
                            (10, 4): -2+2j, (10, 5): -1+2j, (10, 6): 0+2j,
                            (10, 7): -2+3j, (10, 8): -1+3j, (10, 9): 0+3j,
                (0, 10): 1+0j, (0, 1): -1+1j, (0, 2): 0+1j, (0, 3): 1+1j,
                            (0, 4): -1+2j, (0, 5): 0+2j, (0, 6): 1+2j,
                            (0, 7): -1+3j, (0, 8): 0+3j, (0, 9): 1+3j,
                (1, 10): 2-1j, (1, 0): 1-1j, (1, 2): 1, (1, 3): 2+0j,
                            (1, 4): 0+1j, (1, 5): 1+1j, (1, 6): 2+1j,
                            (1, 7): 0+2j, (1, 8): 1+2j, (1, 9): 2+2j,
                (2, 10): 1-1j, (2, 0): 0-1j, (2, 1): -1, (2, 3): 1+0j,
                            (2, 4): -1+1j, (2, 5): 0+1j, (2, 6): 1+1j,
                            (2, 7): -1+2j, (2, 8): 0+2j, (2, 9): 1+2j,
                (3, 10): 0-1j, (3, 0): -1-1j, (3, 1): -2, (3, 2): -1+0j,
                            (3, 4): -2+1j, (3, 5): -1+1j, (3, 6): 0+1j,
                            (3, 7): -2+2j, (3, 8): -1+2j, (3, 9): 0+2j,
                (4, 10): 2-2j, (4, 0): 1-2j, (4, 1): 0-1j, (4, 2): 1-1j,
                            (4, 3): 2-1j, (4, 5): 1+0j, (4, 6): 2+0j,
                            (4, 7): 0+1j, (4, 8): 1+1j, (4, 9): 2+1j,
                (5, 10): 1-2j, (5, 0): 0-2j, (5, 1): -1-1j, (5, 2): 0-1j,
                            (5, 3): 1-1j, (5, 4): -1+0j, (5, 6): 1+0j,
                            (5, 7): -1+1j, (5, 8): 0+1j, (5, 9): 1+1j,
                (6, 10): 0-2j, (6, 0): -1-2j, (6, 1): -2-1j, (6, 2): -1-1j,
                            (6, 3): 0-1j, (6, 4): -2+0j, (6, 5): -1+0j,
                            (6, 7): -2+1j, (6, 8): -1+1j, (6, 9): 0+1j,
                (7, 10): 2-3j, (7, 0): 1-3j, (7, 1): 0-2j, (7, 2): 1-2j,
                            (7, 3): 2-2j, (7, 4): 0-1j, (7, 5): 1-1j,
                            (7, 6): 2-1j, (7, 8): 1+0j, (7, 9): 2+0j,
                (8, 10): 1-3j, (8, 0): 0-3j, (8, 1): -1-2j, (8, 2): 0-2j,
                            (8, 3): 1-2j, (8, 4): -1-1j, (8, 5): 0-1j,
                            (8, 6): 1-1j, (8, 7): -1+0j, (8, 9): 1+0j,
                (9, 10): 0-3j, (9, 0): -1-3j, (9, 1): -2-2j, (9, 2): -1-2j,
                            (9, 3): 0-2j, (9, 4): -2-1j, (9, 5): -1-1j,
                            (9, 6): 0-1j, (9, 7): -2+0j, (9, 8): -1+0j
}


"""
controller layout:
    +---+---+
    | ^ | A |
+---+---+---+
| < | v | > |
+---+---+---+
"""

neededMoveController = {
    (10, 1j): -1, (10, -1): -2-1j, (10, -1j): -1-1j, (10, 1): -1j,
    (1j, 10): 1, (1j, -1): -1-1j, (1j, -1j): -1j, (1j, 1): 1-1j,
    (-1, 10): 2+1j, (-1, 1j): 1+1j, (-1, -1j): 1, (-1, 1): 2,
    (-1j, 10): 1+1j, (-1j, 1j): 1j, (-1j, -1): -1, (-1j, 1): 1,
    (1, 10): 1j, (1, 1j): -1+1j, (1, -1j): -1, (1, -1): -2}

moveToChar = {0+1j: '^', 0-1j: 'v', -1+0j: '<', 1+0j: '>', buttonA: 'A'}