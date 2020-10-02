def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    # create a cache
    cache = {}
    # create a answers array
    result = []

    # loop through both arrays  
    for array in arrays:
        for num in array:
            # if num not in cache add each item in 2nd array as key
            if num not in cache:
                # set value to 1
                cache[num] = 1
            # if key exists
            else:
                # each time a key appears in another array increment by 1
                cache[num] += 1
                # if count matches # of arrays num is in every array
                if cache[num] == len(arrays):
                    # add it to reults array
                    result.append(num)

    # print(cache)


    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))