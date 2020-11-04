def above_average(numbers):
    average = sum(numbers) / len(numbers)
    lst = []
    for i in numbers:
        if i > average:
            lst.append(i)
    return(lst)
