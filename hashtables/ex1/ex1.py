def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    we = dict()
    for i in range(length):
      we[weights[i]] = i
    for i in weights:
      other = limit - i
      if other in we:
        answer = [we[other], weights.index(i)]
        
        return answer

    return None
