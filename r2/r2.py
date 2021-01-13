import sys


if __name__ == '__main__':

    inputs = []
    for line in sys.stdin:
        inputs.append(line)
# with open('sample_data/2.in') as f:
#     inputs = f.readline()

r1, mean = map(int, inputs[0].split(' '))
r2 = 2 * mean - r1
print(r2)
exit(0)
