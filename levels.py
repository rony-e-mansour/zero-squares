from cell import Cell
import numpy as np
from game_logic import *

w = Cell(type="wall", color=None)
n = Cell()
e = Cell(type="empty", color=None)
r = Cell(type="player", color="red")
b = Cell(type="player", color="blue")
g = Cell(type="player", color="green")
o = Cell(type="player", color="orange")
p = Cell(type="player", color="pink")
R = Cell(type="goal", color="red")
B = Cell(type="goal", color="blue")
G = Cell(type="goal", color="green")
O = Cell(type="goal", color="orange")
P = Cell(type="goal", color="pink")
oB = Cell(type="mixed", color="blue", top_cell=Cell(type="player", color="orange"))
rO = Cell(type="mixed", color="orange", top_cell=Cell(type="player", color="red"))
bR = Cell(type="mixed", color="red", top_cell=Cell(type="player", color="blue"))
gB = Cell(type="mixed", color="blue", top_cell=Cell(type="player", color="green"))
gP = Cell(type="mixed", color="pink", top_cell=Cell(type="player", color="green"))
oG = Cell(type="mixed", color="green", top_cell=Cell(type="player", color="orange"))


def generate_h_wall(length):
    return [w for _ in range(length)]


def generate_empty_with_wall(total_length, start_index, num_walls, start=e, end=e):
    section = []
    section.append(start)
    # Generate empty cells until we reach the start index
    section.extend([e for _ in range(start_index)])

    # Add walls
    section.extend([w for _ in range(num_walls)])

    # Fill the rest with empty cells
    if end == e:
        section.extend([e for _ in range(total_length - len(section))])
    else:
        section.extend([e for _ in range(total_length - len(section) - 1)])
        section.append(end)

    return section[:total_length]


def generate_wall_with_empty(total_length, start_index, num_walls, start=w, end=w):
    section = []
    section.append(start)
    # Generate empty cells until we reach the start index
    section.extend([w for _ in range(start_index)])

    # Add walls
    section.extend([e for _ in range(num_walls)])

    # Fill the rest with empty cells
    if end == w:
        section.extend([w for _ in range(total_length - len(section))])
    else:
        section.extend([w for _ in range(total_length - len(section) - 1)])
        section.append(end)

    return section[:total_length]


# level 1
level1 = [
    [w, w, w, w, w, w, w, w],
    [w, e, e, e, e, e, R, w],
    [w, w, w, w, w, w, w, w],
]
level1[1][1] = r

# level 2
level2 = [
    generate_h_wall(8),
    generate_empty_with_wall(8, 2, 1, w, w),
    generate_empty_with_wall(8, 0, 0, w, w),
    generate_empty_with_wall(8, 0, 0, w, w),
    [w, w, w, w, R, w, w, w],
    generate_empty_with_wall(8, 2, 3),
]
level2[1][2] = r

# level 3
level3 = [
    generate_empty_with_wall(13, 1, 11),
    [e, e, w, e, e, e, e, e, e, e, e, e, w],
    [w, w, w, e, e, w, w, w, w, w, w, e, w],
    [w, e, e, e, e, e, R, e, e, e, w, e, w],
    [w, e, w, e, e, e, e, e, e, e, w, e, w],
    [w, e, e, e, e, e, e, e, e, e, e, e, w],
    generate_wall_with_empty(13, 3, 8),
    generate_empty_with_wall(13, 2, 11),
]
level3[1][3] = r

# level 4
level4 = [
    generate_empty_with_wall(11, 2, 3),
    [e, e, e, w, e, w, w, w, w, w, w],
    generate_wall_with_empty(11, 3, 6),
    [w, e, w, e, e, e, e, w, e, e, w],
    generate_empty_with_wall(11, 0, 0, w, w),
    [w, e, e, e, e, e, w, e, e, e, w],
    generate_empty_with_wall(11, 4, 5, w, w),
    generate_empty_with_wall(11, 4, 1, w, e),
    generate_wall_with_empty(11, 5, 6),
]
level4[5][1] = r
level4[4][3] = R

# level 5
level5 = [
    generate_empty_with_wall(10, 1, 7),
    [e, e, w, e, e, e, e, e, w, e],
    [e, w, w, e, e, e, e, e, w, e],
    [w, w, e, e, e, e, w, e, w, e],
    [w, e, e, e, w, e, e, e, w, w],
    generate_empty_with_wall(10, 0, 0, w, w),
    [w, e, w, e, e, e, e, e, e, w],
    generate_empty_with_wall(10, 6, 2, w, w),
    generate_empty_with_wall(10, 0, 7, w, e),
]
level5[3][7] = r
level5[2][5] = R

# level 6
level6 = [
    generate_empty_with_wall(9, 0, 5, w, e),
    generate_empty_with_wall(9, 4, 2, w, e),
    generate_empty_with_wall(9, 5, 3, w, e),
    generate_empty_with_wall(9, 0, 0, w, w),
    generate_h_wall(9),
]
level6[3][7] = r
level6[3][6] = b
level6[1][1] = R
level6[2][3] = B

# level 7
level7 = [
    generate_empty_with_wall(9, 3, 4, e, w),
    generate_empty_with_wall(9, 3, 1, e, w),
    [w, w, w, w, w, e, w, e, w],
    [w, e, e, e, e, e, w, e, w],
    [w, e, e, e, w, e, w, e, w],
    generate_empty_with_wall(9, 0, 0, w, w),
    generate_empty_with_wall(9, 0, 0, w, w),
    generate_h_wall(9),
]
level7[3][4] = r
level7[4][5] = b
level7[2][5] = R
level7[4][3] = B

# level 8
level8 = [
    generate_h_wall(7),
    generate_empty_with_wall(7, 0, 0, w, w),
    [w, e, e, e, w, e, w],
    [w, e, w, e, w, e, w],
    [w, e, e, e, w, e, w],
    [w, e, e, w, w, e, w],
    generate_empty_with_wall(7, 0, 0, w, w),
    generate_empty_with_wall(7, 4, 1, w, w),
    generate_wall_with_empty(7, 3, 2),
    generate_empty_with_wall(7, 0, 1, e, w),
    generate_empty_with_wall(7, 0, 5, e, w),
]
level8[3][1] = r
level8[2][3] = b
level8[4][3] = R
level8[1][5] = B

# level 9
level9 = [
    generate_empty_with_wall(11, 0, 5, e, e),
    [w, w, e, e, e, w, w, w, w, w, e],
    [w, e, e, e, e, w, w, e, e, w, e],
    generate_empty_with_wall(11, 8, 1, w, w),
    [w, e, e, e, w, w, w, e, e, e, w],
    generate_empty_with_wall(11, 8, 1, w, w),
    generate_wall_with_empty(11, 1, 2, w, e),
    generate_empty_with_wall(11, 0, 4, e, e),
]
level9[1][2] = r
level9[6][2] = b
level9[2][7] = B
level9[4][9] = R

# level 10
level10 = [
    generate_empty_with_wall(12, 1, 8, e, e),
    [e, w, w, e, e, e, e, e, e, w, w, e],
    [w, w, e, e, w, e, e, w, e, e, w, w],
    [w, e, e, w, e, e, e, e, w, e, e, w],
    [w, e, e, e, e, w, e, e, w, w, e, w],
    [w, e, w, e, w, w, e, e, e, w, e, w],
    [w, e, e, e, w, e, e, e, e, e, e, w],
    generate_h_wall(12),
]
level10[5][1] = r
level10[5][10] = b
level10[3][5] = R
level10[2][6] = B

# level 11
level11 = [
    generate_empty_with_wall(8, 0, 3, e, e),
    generate_wall_with_empty(8, 1, 1),
    generate_empty_with_wall(8, 0, 0, w, w),
    [w, e, w, e, w, w, w, w],
    generate_empty_with_wall(8, 0, 4, w, e),
]
level11[2][2] = r
level11[2][3] = b
level11[2][1] = o
level11[3][1] = B
level11[3][3] = R
level11[1][2] = O

# level 12
level12 = [
    generate_empty_with_wall(7, 1, 5, e, 2),
    generate_wall_with_empty(7, 2, 3),
    generate_wall_with_empty(7, 0, 5, w, w),
    [w, e, e, e, w, e, w],
    [w, e, e, e, w, e, w],
    [w, w, e, e, w, e, w],
    [e, w, w, e, w, w, w],
    [e, e, w, w, w, e, e],
]
level12[3][5] = r
level12[4][5] = o
level12[5][5] = b
level12[2][1] = R
level12[1][4] = O
level12[5][2] = B


# level 13
level13 = [
    [e, e, w, w, w, w, w, e, e, e, e],
    [w, w, w, e, e, e, w, e, e, e, e],
    [w, e, w, e, e, e, w, w, w, w, w],
    [w, e, w, e, e, e, e, w, e, e, w],
    [w, e, w, w, e, w, w, w, e, e, w],
    [w, e, e, e, e, e, e, e, e, w, w],
    [w, e, e, w, e, e, e, e, w, w, e],
    [w, w, w, w, w, w, w, w, w, e, e],
]
level13[1][3] = b
level13[1][4] = r
level13[1][5] = o
level13[2][5] = B
level13[3][8] = R
level13[6][4] = O

# level 14
level14 = [
    generate_h_wall(7),
    [w, e, w, e, w, e, w],
    generate_empty_with_wall(7, 0, 0, w, w),
    generate_empty_with_wall(7, 0, 0, w, w),
    generate_empty_with_wall(7, 0, 1, w, w),
    generate_empty_with_wall(7, 0, 1, e, w),
    generate_wall_with_empty(7, 0, 0, e, w),
]
level14[1][1] = oB
level14[1][3] = rO
level14[1][5] = bR


# level 15
level15 = [
    generate_wall_with_empty(8, 0, 0, e, w),
    generate_empty_with_wall(8, 0, 1, e, w),
    [e, w, e, e, e, w, e, w],
    [w, w, e, w, w, w, e, w],
    generate_empty_with_wall(8, 0, 0, w, w),
    [w, e, w, w, w, w, e, w],
    [w, e, w, e, e, w, e, w],
    generate_empty_with_wall(8, 0, 0, w, w),
    generate_h_wall(8),
]
level15[4][2] = o
level15[4][3] = r
level15[4][4] = b
level15[2][3] = B
level15[6][4] = O
level15[6][6] = R

# level16
level16 = [
    generate_h_wall(11),
    generate_empty_with_wall(11, 0, 0, w, w),
    generate_empty_with_wall(11, 0, 0, w, w),
    generate_empty_with_wall(11, 0, 1, w, w),
    [e, w, e, e, e, e, w, w, w, w, w],
    [e, w, e, e, e, e, w, e, e, e, e],
    generate_wall_with_empty(11, 6, 3, e, e),
]
level16[1][1] = o
level16[1][2] = r
level16[1][3] = b
level16[1][4] = g
level16[2][6] = O
level16[3][5] = G
level16[4][4] = B
level16[5][3] = R

# level17
level17 = [
    generate_wall_with_empty(9, 6, 2, w, e),
    [w, e, e, e, e, e, w, w, w],
    [w, e, e, e, e, e, w, e, w],
    [w, w, w, w, e, e, w, e, w],
    [e, e, w, e, e, e, e, e, w],
    [w, w, w, e, w, w, e, e, w],
    [w, e, e, e, w, e, e, e, w],
    generate_empty_with_wall(9, 0, 0, w, w),
    generate_empty_with_wall(9, 0, 0, w, w),
    generate_wall_with_empty(9, 6, 1, w, w),
    generate_empty_with_wall(9, 5, 4, e, w),
]
level17[8][1] = o
level17[1][1] = r
level17[1][5] = b
level17[6][1] = g
level17[2][7] = O
level17[6][3] = G
level17[9][7] = B
level17[6][5] = R

# level 18
level18 = [
    generate_wall_with_empty(10, 7, 2, w, e),
    [w, e, e, e, w, e, e, w, e, e],
    generate_empty_with_wall(10, 6, 1, w, e),
    [w, e, e, e, w, e, e, w, e, e],
    [w, e, w, e, w, w, w, w, w, w],
    generate_empty_with_wall(10, 0, 1, w, w),
    [w, e, e, w, e, e, w, e, e, w],
    generate_h_wall(10),
]
level18[6][7] = r
level18[5][7] = b
level18[5][8] = o
level18[1][5] = R
level18[4][1] = O
level18[3][5] = G
level18[6][8] = gB


# level 19
level19 = [
    [e, w, w, w, e, e, e, e],
    [w, w, e, w, w, e, e, e],
    [w, e, e, e, w, e, e, e],
    [w, w, w, e, w, w, w, w],
    [w, e, e, e, e, w, w, w],
    [w, w, e, e, e, e, e, w],
    [w, e, e, w, e, e, e, w],
    [w, w, w, w, e, w, w, w],
    [e, e, e, w, e, e, e, w],
    [e, e, e, w, e, e, e, w],
    [e, e, e, w, w, e, w, w],
    [e, e, e, e, w, w, w, e],
]
level19[4][4] = o
level19[6][1] = r
level19[4][1] = b
level19[6][6] = g
level19[1][2] = O
level19[6][4] = R
level19[8][5] = B
level19[10][5] = G


# level 20
level20 = [
    [e, e, e, w, w, w, w, e, e],
    [w, w, w, w, e, e, w, w, w],
    generate_empty_with_wall(9, 0, 0, w, w),
    [w, e, e, w, e, e, w, e, w],
    generate_h_wall(9),
]
level20[1][4] = r
level20[2][3] = b
level20[2][2] = p
level20[1][5] = O
level20[3][4] = R
level20[2][1] = B
level20[3][2] = gP
level20[3][7] = oG
