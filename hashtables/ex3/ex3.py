def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    amount = len(arrays)
    total = dict()
    result = []
    for i in arrays:
      for a in i:
        if a in total:
          total[a] += 1
        else:
          total[a] = 1
    for i in total:
      if total[i] == amount:
        result.append(i)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
