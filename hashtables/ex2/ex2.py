#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    ticket = dict()
    for i in tickets:
      ticket[i.source] = i.destination
    route = [ticket["NONE"]]
    curr = ticket["NONE"]
    while curr != "NONE":
      curr = ticket[curr]
      route.append(curr)
      

    return route
