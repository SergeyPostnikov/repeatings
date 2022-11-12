def get_special_sum(num: 'log10(num) = 5'):
    flag_odd = False
    odd_sum = 0
    even_sum = 0
    while num > 0:
        if flag_odd:
            odd_sum += num % 10
        else:
            even_sum += num % 10
        flag_odd = not flag_odd
        num //= 10
    return even_sum - odd_sum
 
print(get_special_sum(212121))
