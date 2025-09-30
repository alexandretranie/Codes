import pandas as pd
import re

# Path
chemin = "/Users/alexandretranie/Downloads/input3.txt"

with open(chemin, 'r', encoding='utf-8') as f:
    content = f.read()


def sum_corrupt_file(content, action=True):
    """
    content : str, texte à scanner
    action : bool, True si mul() activé au départ, False sinon
    """
    total = 0
    multiplication_enabled = action

    # Pattern pour détecter do(), don't() et mul(X,Y)
    pattern = r"(do\(\)|don't\(\)|mul\((\d{1,3}),(\d{1,3})\))"

    for match in re.finditer(pattern, content):
        full_match = match.group(0)
        x = match.group(2)
        y = match.group(3)

        if full_match == "do()":
            multiplication_enabled = True
        elif full_match == "don't()":
            multiplication_enabled = False
        elif x and y and multiplication_enabled :
            total += int(x) * int(y)

    return total



if __name__ ==  '__main__':
    print(content)
    result = sum_corrupt_file(content, action=True)
    print(f"Sum of all valid multiplications: {result}")