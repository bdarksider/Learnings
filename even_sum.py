def even_sum(numbers):
    counter = 0
    flag = 1

    for item in numbers:
        if item % 2 == 0:
            # skips the first time
            if flag:
                # set the flag to 0 if even number is found
                flag = 0
                continue
            else:
                counter += item

    return counter


assert even_sum([2,2,2,2,2]) == 8
assert even_sum([3,2,5]) == 0
assert even_sum([1,2,2,1,2,3]) == 4
