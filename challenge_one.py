# # Challenge 1: 
# There are N boxes (numbered from 0 to N−1) arranged in a row. The K-th box contains A[K] bricks. In one move you can take one brick from some box and move it to a box next to it (on the left or on the right). What is the minimum number of moves needed to end up with exactly 10 bricks in every box?


# Write a function:

# function solution(A);

# that, given an array A of N integers, returns the minimum number of moves needed to end up with exactly 10 bricks in every box. If this is not possible, the function should return −1.

# Examples:

# 1. For A = [7, 15, 10, 8], the function should return 7. You can perform the following sequence of moves:
#    - move three bricks from box number 1 to the box on the left: [10, 12, 10, 8];
#    - move two bricks from box number 1 to the box on the right: [10, 10, 12, 8];
#    - finally, move two bricks from box number 2 to the last box: [10, 10, 10, 10].


# 2. For A = [11, 10, 8, 12, 8, 10, 11], the function should return 6. You can perform the following sequence of moves:
#     - move a brick from box number 0 to box number 2 (using two moves);
#     - move a brick from the last box two positions to the left (using two moves);
#     - move a brick from the middle box to each of its neighbors (another two moves).


# 3. For A = [7, 14, 10], the function should return −1. It is not possible to end up with exactly 10 bricks in each box.

