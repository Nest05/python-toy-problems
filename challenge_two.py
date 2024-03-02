# Challenge 2: Write a function:

# function solution(A);

# that, given an array A consisting of N integers, returns the maximum sum of two numbers whose digits add up to an equal sum. If there are no two numbers whose digits have an equal sum, the function should return -1.

def solution(A):
    max_sum = -1

    for i in range (len(A)):
        for j in range(i+1, len(A)):

            digit_sum_i = sum([int(digit) for digit in str(A[i])])
            digit_sum_j = sum([int(digit) for digit in str(A[j])])

            if digit_sum_i == digit_sum_j:

                current_sum = A[i] + A[j]
                if current_sum > max_sum:
                    max_sum = current_sum

    return max_sum

print(solution([51, 71, 17, 42]))
print(solution([60, 33, 42]))
print(solution([51, 43, 32]))

