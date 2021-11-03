def seq_length(num):
    iter_count = 1
    while num != 1:
        iter_count += 1
        if num % 2 == 0:
            num /= 2
        else:
            num = num * 3 + 1
    return iter_count

max_length = 1
number = 1
for i in range(2, 1000001):
    curent_length = seq_length(i)
    if curent_length > max_length:
        max_length = curent_length
        number = i

print("Max sequence = {}. It's number - {}".format(max_length, number))
