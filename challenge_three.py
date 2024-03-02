# Challenge 3: Write a function solution that, given an integer N, returns a string of length N containing as many different lower-case letters ('a'-'z') as possible, in which each letter occurs an equal number of times.

def solution(N):

    max_num_letters = min(26, (N // 2) + 1)


    letters = []

    for i in range(max_num_letters):
        letter = chr(ord('a') + i)
        letters.extend([letter, letter])


    while len(letters) < N:
        letter = chr(ord('a') + len(letters) // 2)
        letters.append(letter)

    return ''.join(letters[:N])


print(solution(3))