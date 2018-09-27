def dutch_flag(A, pivot_index):
    pivot = A[pivot_index]
    smaller = 0
    for i in range(len(A)):
        if A[i] < pivot:
            A[i], A[smaller] = A[smaller], A[i]
            smaller += 1
            print(A)
    print('small done')

    larger = len(A) - 1
    for j in reversed(range(len(A))):
        if A[j] > pivot:
            A[j], A[larger] = A[larger], A[j]
            larger -= 1
            print(A)
    return A
