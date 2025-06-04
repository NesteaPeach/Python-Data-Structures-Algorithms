"""
big O(n) - scaling proportionally to n
O(nlog n) - this is the most efficient you can make a string sort algorithm
my_list.append/ pop is O(1)
my_list.pop(0)/ insert(0,11) - will require the list to reindex O(n)
looking for a number in a list by number is O(n)
looking for a number by index is O(1)
"""


def print_items(n):
    # this function does n operations
    for i in range(n):
        # 10 items printed
        print(i)


def print_items_2(n):
    # this function does n+n operations
    # dropping constant - we do no write O(2n) we can drop the constant 2 so it is still O(n)
    for i in range(n):
        print(i)
        # (printed 20 items)
    for j in range(n):
        print(j)


def print_items_3(n):
    # this function does O(squared n) operations
    for i in range(n):
        for j in range(n):
            # printed 99 items
            print(j, i)


def print_items_4(target):
    """
    this function does O(log n) operations
    the list must be sorted - then we split the list in half, and we check if it's in the first half or the second
    half, and we continue to split the list. in this way we will need 3 operation to find a number out of 8.
    so that will mean its log(2)8 = 3. log(n) - is checking 2 to what power equals the number of the items in the list.
    :return:
    """
    item_list = [1, 2, 3, 4, 5, 6, 7, 8]
    counter = 0
    left, right = 0, len(item_list) - 1
    while left <= right:
        counter += 1
        print(f" run num {counter}")
        mid = left + (right - left) // 2
        if item_list[mid] == target:
            return mid
        elif item_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


number = 7
print(print_items_4(number))
