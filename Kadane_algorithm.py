

def kadane_algorithm(L):
    max_ending_here = max_so_far = L[0]
    for x in L[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far


if __name__ == '__main__':
    test = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print("Maximum subarray sum is:", kadane_algorithm(test))

