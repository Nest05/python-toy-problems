# Challenge 1: There are N boxes (numbered from 0 to N−1) arranged in a row. The K-th box contains A[K] bricks. In one move you can take one brick from some box and move it to a box next to it (on the left or on the right). What is the minimum number of moves needed to end up with exactly 10 bricks in every box?

# Write a function:

# function solution(A);

# that, given an array A of N integers, returns the minimum number of moves needed to end up with exactly 10 bricks in every box. If this is not possible, the function should return −1.

def solution(A):
    N = len(A)  # Number of boxes
    total_bricks = sum(A)  # Total number of bricks across all boxes
    desired_total = N * 10  # Desired total number of bricks for equal distribution

    # Check if redistribution to exactly 10 bricks per box is possible
    if total_bricks != desired_total:
        return -1

    # Calculate the minimum number of moves required for redistribution
    moves = 0
    cumulative_diff = 0
    for bricks in A:
        # Calculate the difference for the current box
        diff = bricks - 10
        cumulative_diff += diff
        # Accumulate the absolute value of the cumulative difference
        moves += abs(cumulative_diff)

    return moves

print(solution([19, 2])) # -1
print(solution([19, 1])) # 9
print(solution([21, 2, 7])) # 14
print(solution([7, 15, 10, 8])) # 7
print(solution([7, 14, 10])) # -1
print(solution([11, 10, 8, 12, 8, 10, 11])) # 6

