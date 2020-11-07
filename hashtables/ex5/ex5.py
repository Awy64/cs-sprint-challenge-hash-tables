# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    fil = dict()
    di = dict()
    result = []
    for f in files:
        fil[f] = f.split("/")
        di[fil[f][-1]] = f
    for a in queries:
      if a in di:
        if di[a] not in result:
          result.append(di[a])  
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
