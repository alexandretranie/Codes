
def max_sliding_window(L: list, k: int) -> tuple:
    if not L or k <= 0 or k > len(L):
        return None
    
    # Initial sum of first window
    window_sum = sum(L[:k])
    max_sum = window_sum
    max_window = L[:k]  # store actual window
    
    # Slide the window
    for i in range(k, len(L)):
        window_sum += L[i] - L[i - k]  # add new, remove old
        
        if window_sum > max_sum:
            max_sum = window_sum
            max_window = L[i - k + 1 : i + 1]  # update best window
    
    return max_window, max_sum



if __name__ == '__main__':
    L = [2, 1, 5, 1, 3, 2]
    k = 3
    print(max_sliding_window(L, k))  # Output: 9 (window [5,1,3])
