def solve():
    # Read the input strings s, t, and p for the current query
    s = input()
    t = input()
    p = input()

    # Check if s is a subsequence of t
    i, j = 0, 0  
    while i < len(s) and j < len(t):
        # If characters match, move to the next character in s
        if s[i] == t[j]:
            i += 1
        # Always move to the next character in t
        j += 1  

    # If we couldn't match all characters of s in t, then s is not a subsequence of t
    if i != len(s):
        print("NO")
        return

    # Count the frequency of each character in t
    freq_t = {}
    for char in t:
        freq_t[char] = freq_t.get(char, 0) + 1

    # Count the frequency of each character in both s and p combined
    freq_s_p = {}
    for char in s + p:
        freq_s_p[char] = freq_s_p.get(char, 0) + 1

    # Ensure that for every character in t, we have enough occurrences in s and p
    for char, required_count in freq_t.items():
        available_count = freq_s_p.get(char, 0)
        if required_count > available_count:
            print("NO")
            return

    # If all checks pass, s can be transformed into t using characters from p
    print("YES")


# Read the number of queries and process each one
q = int(input())  
for _ in range(q):
    solve()
