import os, sys

class HiddenPrints:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout

def down_to_one_dp(n):
    if n == 1:
        return 0
    
    if n % 6 == 0:
        with HiddenPrints():
            a = down_to_one_dp(n / 3)
            b = down_to_one_dp(n / 2)
            c = down_to_one_dp(n - 1)

        if a > b:
            if b > c:
                print(r"-1")
                result = 1 + c
            else:
                print(r"\2")
                result = 1 + b
        else:
            if a > c:
                print(r"-1")
                result = 1 + c
            else:
                print(r"\3")
                result = 1 + a
        return result
    
    if n % 3 == 0:
        with HiddenPrints():
            a = down_to_one_dp(n / 3)
            c = down_to_one_dp(n - 1)

        if a > c:
            print(r"-1")
            result = 1 + c
        else:
            print(r"\3")
            result = 1 + a
        return result
    
    if n % 2 == 0:
        with HiddenPrints():
            b = down_to_one_dp(n / 2)
            c = down_to_one_dp(n - 1)
        if b > c:
            print(r"-1")
            result = 1 + c
        else:
            print(r"\2")
            result = 1 + b
        return result
    
    print(r"-1")
    result = 1 + down_to_one_dp(n - 1)
    return result

print(down_to_one_dp(int(sys.argv[1])))