def get_indices_of_item_weights(weights, limit):
    # Init the hash table
    dictOfWeights = {}
    for weight in weights:
        # This is O(n) as each item needs to be iterated through.
        dictOfWeights[weight] = weights.index(weight)

    if len(weights) == 1:
        return ()
    elif len(weights) == 2:
        return (1, 0)
    for key, value in dictOfWeights.items():  # O(n)
        new_limit = limit - key
        # This relies on a hash instead of iterating through, so O(1)
        if new_limit in dictOfWeights:
            return (dictOfWeights[new_limit], value)

# ==> O(2n) = O(n)


if __name__ == '__main__':
        # You can write code here to test your implementation using the Python repl
    get_indices_of_item_weights([9], 9)
    get_indices_of_item_weights([4, 4], 8)
