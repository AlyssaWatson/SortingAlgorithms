# Bubble sort algorithm
def bubble_sort(numbers):
    # make same number of passes as numbers in list
    for j in range(len(numbers)):
        # loop through the entire list (-1 to prevent index out of bounds)
        for i in range(len(numbers)-1):
            # switch numbers if necessary
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
    # return the sorted list
    return numbers


# Bucket sort algorithm - requires number of buckets to create
def bucket_sort(numbers, buckets):
    # find max min and range to create buckets
    list_min = min(numbers)
    list_max = max(numbers)
    list_range = list_max-list_min
    bucket_size = list_range/buckets
    bucket_lists = []
    # create the buckets
    for i in range(buckets):
        bucket_lists.append([[], i*bucket_size + list_min, (i+1)*bucket_size + list_min])
    # sort numbers into the buckets
    for num in numbers:
        for i in bucket_lists:
            if (num >= i[1]) and (num <= i[2]):
                i[0].append(num)
                # break prevents number from being included in multiple buckets
                break
    sorted_list = []
    # sort values in buckets using bubble sort
    for bucket in bucket_lists:
        sorted_list.append(bubble_sort(bucket[0]))
    # flatten and return sorted list
    return [item for sublist in sorted_list for item in sublist]


