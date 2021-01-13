import sys


if __name__ == '__main__':

    inputs = []
    for line in sys.stdin:
        inputs.append(line)
# with open('sample_data/b.in') as f:
#     inputs = [line.strip() for line in f]

N = int(inputs[0])
for i in range(1, N+1):
    print(f"{i} Abracadabra")
exit(0)
