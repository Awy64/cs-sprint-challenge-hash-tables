def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    pos = dict()
    result = []
    for i in a:
      if i > 0:
        pos[i] = 0
    for i in a:
      if i < 0:
        if i * -1 in pos:
          result.append(i * -1)

  

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
