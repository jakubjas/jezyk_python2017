def flatten(seq):

    flattened_sequence = []

    for i in range(len(seq)):

        if isinstance(seq[i], (list, tuple)):
            flattened_sequence.extend(flatten(seq[i]))
        else:
            flattened_sequence.append(seq[i])

    return flattened_sequence

sequence = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]

print flatten(sequence)
