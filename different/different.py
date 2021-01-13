import sys


if __name__ == '__main__':

    inputs = []
    for line in sys.stdin:
        inputs.append(line)
# with open('sample_data/sample.in') as f:
#     inputs = [line.strip() for line in f]

for line in inputs:
    n1, n2 = map(int, line.split(' '))
    print(abs(n1 - n2))
exit(0)
