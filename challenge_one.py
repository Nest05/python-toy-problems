# Challenge 1: There are N boxes (numbered from 0 to N−1) arranged in a row. The K-th box contains A[K] bricks. In one move you can take one brick from some box and move it to a box next to it (on the left or on the right). What is the minimum number of moves needed to end up with exactly 10 bricks in every box?

# Write a function:

# function solution(A);

# that, given an array A of N integers, returns the minimum number of moves needed to end up with exactly 10 bricks in every box. If this is not possible, the function should return −1.

def solution(A):
    total_bricks = sum(A)
    target_sum = 10 * len(A)
    difference = abs(target_sum - total_bricks)

    if difference % 2 != 0:
        return -1
    
    running_sum = 0
    excess_bricks = 0

    for i in range(len(A)):
        current_bricks = A[i]
        needed_bricks = 10 - current_bricks
        excess_bricks += needed_bricks

        if excess_bricks > 0:
            moves = min(excess_bricks, current_bricks)
            running_sum += moves
            current_bricks -= moves
            excess_bricks -= moves

        running_sum += abs(current_bricks)
            
    return running_sum
 

bricks_in_boxes = [7, 15, 10, 8]
print(solution(bricks_in_boxes))