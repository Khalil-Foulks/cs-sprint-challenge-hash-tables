#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source # key
        self.destination = destination # value


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here

    # creating a array to hold the route for the trip
    route = [None] * length
    cache = {}

    # loop through tickets to get ticket Node
    for ticket in tickets:
        # store ticket node in cache
        if ticket not in cache:
            # source = key; destination = value
            cache[ticket.source] = ticket.destination 

    # store the value that has a key of NONE in cache; that becomes the cur
    cur = cache["NONE"]

    for i in range(0, length):
        # each destination is stored at a given index in route
        route[i] = cur

        # current cur becomes the lookup key in cache; new cur becomes the associated value 
        cur = cache[cur]
        
    # print(cache)
    

    return route


# ticket_1 = Ticket("PIT", "ORD")
# ticket_2 = Ticket("XNA", "SAP")
# ticket_3 = Ticket("SFO", "BHM")
# ticket_4 = Ticket("FLG", "XNA")
# ticket_5 = Ticket("NONE", "LAX")
# ticket_6 = Ticket("LAX", "SFO")
# ticket_7 = Ticket("SAP", "SLC")
# ticket_8 = Ticket("ORD", "NONE")
# ticket_9 = Ticket("SLC", "PIT")
# ticket_10 = Ticket("BHM", "FLG")

# tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5, ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]

# print(reconstruct_trip(tickets, 10))
