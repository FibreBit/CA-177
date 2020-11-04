def sum_to_k(lst, k):
    for i in range(len(lst)):
        for j in lst[i:]:
            if lst[i] + j == k:
                print(lst[i], j)
