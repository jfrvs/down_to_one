import os, sys

class HiddenPrints:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout

def down_to_one_dp_memo(n, memo=None):
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n == 1:
        return 0
    
    if n % 6 == 0:
        with HiddenPrints():
            a = down_to_one_dp_memo(n / 3, memo)
            b = down_to_one_dp_memo(n / 2, memo)
            c = down_to_one_dp_memo(n - 1, memo)

        if a > b:
            if b > c:
                print(r"-1")
                result = 1 + down_to_one_dp_memo(n - 1, memo)
            else:
                print(r"\2")
                result = 1 + down_to_one_dp_memo(n / 2, memo)
        else:
            if a > c:
                print(r"-1")
                result = 1 + down_to_one_dp_memo(n - 1, memo)
            else:
                print(r"\3")
                result = 1 + down_to_one_dp_memo(n / 3, memo)
        memo[n] = result
        return result
    
    if n % 3 == 0:
        with HiddenPrints():
            a = down_to_one_dp_memo(n / 3, memo)
            c = down_to_one_dp_memo(n - 1, memo)

        if a > c:
            print(r"-1")
            result = 1 + down_to_one_dp_memo(n - 1, memo)
        else:
            print(r"\3")
            result = 1 + down_to_one_dp_memo(n / 3, memo)
        memo[n] = result
        return result
    
    if n % 2 == 0:
        with HiddenPrints():
            b = down_to_one_dp_memo(n / 2, memo)
            c = down_to_one_dp_memo(n - 1, memo)
        if b > c:
            print(r"-1")
            result = 1 + down_to_one_dp_memo(n - 1, memo)
        else:
            print(r"\2")
            result = 1 + down_to_one_dp_memo(n / 2, memo)
        memo[n] = result
        return result
    
    print(r"-1")
    result = 1 + down_to_one_dp_memo(n - 1, memo)
    memo[n] = result
    return result

result = down_to_one_dp_memo(int(sys.argv[1]))
print("N° of steps:")
print(result)