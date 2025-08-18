"""Given two strings A and B, find the minimum length substring of A that contains all characters of B (order doesn't matter)"""

from collections import Counter, defaultdict

def min_window(A: str, B: str) -> str:
    if not A or not B:
        return ""
    
    # Count characters required from B
    required = Counter(B)
    required_chars = len(required)   # number of unique chars in B
    
    # Current window counters
    window_counts = {}
    formed = 0  # how many unique chars are satisfied in current window
    
    # Sliding window pointers
    left = 0
    best_len = float("inf")
    best_window = (0, 0)
    
    for right, char in enumerate(A):
        # Add char to current window
        window_counts[char] = window_counts.get(char, 0) + 1
        
        # Check if requirement for this char is satisfied
        if char in required and window_counts[char] == required[char]:
            formed += 1
        
        # Try to shrink window if all requirements are satisfied
        while left <= right and formed == required_chars:
            window_len = right - left + 1
            if window_len < best_len:
                best_len = window_len
                best_window = (left, right)
            
            # Remove the leftmost char
            left_char = A[left]
            window_counts[left_char] -= 1
            if left_char in required and window_counts[left_char] < required[left_char]:
                formed -= 1
            left += 1
    
    # Return result
    if best_len == float("inf"):
        return ""
    return A[best_window[0]:best_window[1]+1]



if __name__ == "__main__":
    A = "ADOBECODEBANC"
    B = "ABC"
    print(min_window(A, B))
