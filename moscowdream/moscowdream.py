import sys


def validate_problem_set(line):
    a, b, c, n = map(int, line.split(' '))
    valid = False
    response = { False: 'NO', True: 'YES' }

    if a != 0 and b != 0 and c != 0 and n >= 3 and n <= (a + b + c):
        valid = True
    return response[valid]


if __name__ == '__main__':

    inputs = []
    for line in sys.stdin:
        inputs.append(line)
# with open('sample_data/2.in') as f:
#     inputs = [line.strip() for line in f]

line = inputs[0]
print(validate_problem_set(line))
exit(0)
