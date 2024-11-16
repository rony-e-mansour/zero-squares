from cell import Cell
import numpy as np

w = Cell(type="wall", color=None)
n = Cell()
e = Cell(type="empty", color=None)
r = Cell(type="player", color="red")
b = Cell(type="player", color="blue")
g = Cell(type="player", color="green")
o = Cell(type="player", color="orange")
R = Cell(type="goal", color="red")
B = Cell(type="goal", color="blue")
G = Cell(type="goal", color="green")
O = Cell(type="goal", color="orange")


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


# level test
leveltest = [
    [w, w, w, w, w, w, w],
    [w, e, e, R, e, e, w],
    [w, e, e, e, e, e, w],
    [w, e, e, e, e, e, w],
    [w, e, e, r, e, g, w],
    [w, e, e, e, e, G, w],
    [w, w, w, w, w, w, w],
]


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

# TODO level10 (not created)

# level 9
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

# TODO skip level from 10 to 15

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

# level16
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

level2 = level2
