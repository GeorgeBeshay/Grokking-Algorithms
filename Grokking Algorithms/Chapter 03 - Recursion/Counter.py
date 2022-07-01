def bad_count_down(i):
    print(i)
    bad_count_down(i - 1)


def good_count_down(i):
    if i <= 0:      # Base Case
        return
    print(i)
    good_count_down(i - 1)


# bad_count_down(5)
good_count_down(10)
