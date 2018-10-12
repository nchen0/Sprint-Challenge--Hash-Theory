def reconstruct_trip(tickets):
    ht = {}
    for ticket in tickets:
        ht[ticket[0]] = ticket[1]

    # One of the keys will contain None, that value will be our starting destination.
    trip = []
    trip.append(ht[None])

    for i in range(len(ht)-2):
        try:
            # Each time, we find in the dictionary the key from our trip list.
            trip.append(ht[trip[i]])
        except:
            # If there is a missing layover, it will return an empty array.
            trip = []
            return trip
    return trip


if __name__ == '__main__':
    # You can write code here to test your implementation using the Python repl
    pass
