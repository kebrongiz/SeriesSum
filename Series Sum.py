def series_sum():
    sum = 1/3
    num = 1
    den = 3
    for i in range(0, 48):
        num += 2
        den += 2
        sum += num/den
    return sum
print("The sum of the series is: {}".format(series_sum()))