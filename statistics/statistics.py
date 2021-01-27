import sys


def produce_stats(i, line):
    values = list(map(int, line.split(' ')))
    values = values[1:]
    maximum = float('-inf')
    minimum = float('inf')

    for val in values:
        if val > maximum:
            maximum = val
        if val < minimum:
            minimum = val

    return f"Case {i}: {minimum} {maximum} {maximum - minimum}"


if __name__ == '__main__':

    inputs = []
    for line in sys.stdin:
        inputs.append(line)
# with open('sample_data/sample.in') as f:
#     inputs = [line.strip() for line in f]

for i in range(len(inputs)):
    print(produce_stats(i+1, inputs[i]))
exit(0)