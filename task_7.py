def counter(number):
    total_sum = number
    while total_sum >= 10:
        total_sum = sum(int(i) for i in str(total_sum))
    return total_sum
