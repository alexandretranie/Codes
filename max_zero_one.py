
def max_zero_one(L: list) -> list:
    if not L:
        return []

    # Replace 0 with -1
    arr = [-1 if x == 0 else 1 for x in L]

    # Hashmap for prefix sums
    prefix_index = {0: -1} 
    prefix_sum = 0
    max_len = 0
    start, end = 0, -1

    for i, val in enumerate(arr):
        prefix_sum += val

        if prefix_sum in prefix_index:
            prev_idx = prefix_index[prefix_sum]
            length = i - prev_idx
            if length > max_len:
                max_len = length
                start, end = prev_idx + 1, i
        else:
            prefix_index[prefix_sum] = i

    return L[start:end+1] if max_len > 0 else []



if __name__ == '__main__':
    L = [1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0]
    print(max_zero_one(L)) 
