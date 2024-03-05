# Challenge 1: There are N boxes (numbered from 0 to N−1) arranged in a row. The K-th box contains A[K] bricks. In one move you can take one brick from some box and move it to a box next to it (on the left or on the right). What is the minimum number of moves needed to end up with exactly 10 bricks in every box?

# Write a function:

# function solution(A);

# that, given an array A of N integers, returns the minimum number of moves needed to end up with exactly 10 bricks in every box. If this is not possible, the function should return −1.

def solution(A):
    excess_bricks = 0
    running_sum = 0

    for bricks in A:
        needed_bricks = bricks - 10
        excess_bricks += needed_bricks
        running_sum += abs(needed_bricks)

    if excess_bricks % 2 != 0:
        return -1

    return int(running_sum/2)

bricks_in_boxes = [7, 15, 10, 8]
print(solution(bricks_in_boxes))