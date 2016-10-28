def sum_sequence(seq):

    s = 0

    for i in range(len(seq)):

        if isinstance(seq[i], (list, tuple)):
            s += sum_sequence(seq[i])
        else:
            s += seq[i]

    return s

sequence = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]

print sum_sequence(sequence)
