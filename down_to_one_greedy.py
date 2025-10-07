import sys

def down_to_one_greedy(n):
    if n == 1:
        return 0
    if n % 3 == 0:
        print(r"\3")
        return 1 + down_to_one_greedy(n / 3)
    if n % 2 == 0:
        print(r"\2")
        return 1 + down_to_one_greedy(n / 2)
    print(r"-1")
    return 1 + down_to_one_greedy(n - 1)

print(down_to_one_greedy(int(sys.argv[1])))