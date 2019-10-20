def find_max(num):
    max_num = num[0]

    for number in num:
        if number > max_num:
            max_num = number
    return max_num


def find_min(num):
    min_num = num[0]

    for number in num:
        if number < min_num:
            min_num = number
    return min_num
