def bubble(lst, desc=False):
    for i in range(len(lst) - 1):
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    if desc:
        return lst
    return lst[::-1]


if __name__ == '__main__':
    nums: list = input().split()
    nums = map(int, nums)
    nums = list(nums)

    print(bubble(nums))