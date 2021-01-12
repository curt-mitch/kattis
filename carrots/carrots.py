import sys


if __name__ == '__main__':

    inputs = []
    for line in sys.stdin:
        inputs.append(line)
# with open('sample_data/carrots.02.in') as f:
#     inputs = [line.strip() for line in f]

first_row = inputs[0]
num_carrots = int(first_row.split(' ')[1])
print(num_carrots)
exit(0)
