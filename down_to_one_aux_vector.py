import os, sys

def down_to_one_aux_vector(n):
    if n == 1:
        return 0
    
    aux_array = [0] * (n + 1)

    aux_array[1] = 0

    ops_array = aux_array.copy()

    for i in range(2, n + 1):
        aux_array[i] = 1 + aux_array[i - 1]
        operation = r"-1"

        if i % 2 == 0:
            if 1 + aux_array[i // 2] < aux_array[i]:
                aux_array[i] = 1 + aux_array[i // 2]
                operation = r"\2"
        
        if i % 3 == 0:
            if 1 + aux_array[i // 3] < aux_array[i]:
                aux_array[i] = 1 + aux_array[i // 3]
                operation = r"\3"

        ops_array[i] = operation

    aux = n

    final_ops_array = []

    while aux > 1:
        if ops_array[aux] == "\\3":
            final_ops_array.append(ops_array[aux])
            aux //= 3
        if ops_array[aux] == "\\2":
            final_ops_array.append(ops_array[aux])
            aux //= 2
        if ops_array[aux] == "-1":
            final_ops_array.append(ops_array[aux])
            aux -= 1

    return aux_array[n], final_ops_array

result = down_to_one_aux_vector(int(sys.argv[1]))
print("N° of steps:")
print(result[0])
print("Sequence of steps:")
print(result[1])

