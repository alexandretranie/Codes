import pandas as pd

# Path
chemin = "/Users/alexandretranie/Downloads/input4.txt"

with open(chemin, 'r', encoding='utf-8') as f:
    grid = [line.strip() for line in f if line.strip()]


def count_xmas(grid, word="XMAS"):
    rows = len(grid)
    cols = len(grid[0])
    word_len = len(word)
    count = 0

    directions = [
        (0, 1),   # right
        (1, 0),   # bottom
        (1, 1),   # bottom-right diag
        (1, -1),  # bottom-left diag
        (0, -1),  # left
        (-1, 0),  # top
        (-1, -1), # top-left diag
        (-1, 1)   # top-right diag
    ]

    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                match = True
                for k in range(word_len):
                    x = i + dx*k
                    y = j + dy*k
                    if 0 <= x < rows and 0 <= y < cols:
                        if grid[x][y] != word[k]:
                            match = False
                            break
                    else:
                        match = False
                        break
                if match:
                    count += 1
    return count


def count_x_mas(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    # Patern to identify : 4 configurations
    patterns = [
        [['M', None, 'S'], [None, 'A', None], ['M', None, 'S']],
        [['S', None, 'M'], [None, 'A', None], ['S', None, 'M']], 
        [['M', None, 'M'], [None, 'A', None], ['S', None, 'S']],
        [['S', None, 'S'], [None, 'A', None], ['M', None, 'M']],
    ]

    for i in range(rows - 2):
        for j in range(cols - 2):
            subgrid = [row[j:j+3] for row in grid[i:i+3]]
            for pat in patterns:
                match = True
                for r in range(3):
                    for c in range(3):
                        if pat[r][c] and pat[r][c] != subgrid[r][c]:
                            match = False
                            break
                    if not match:
                        break
                if match:
                    count += 1
    return count



if __name__ == "__main__":

    total = count_xmas(grid)
    total2 = count_x_mas(grid)
    print(f"Total XMAS found: {total}")
    print(f"Total X-MAS found: {total2}")
