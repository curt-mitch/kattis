import sys


if __name__ == '__main__':

    inputs = []
    for line in sys.stdin:
        inputs.append(line)
# with open('sample_data/2.in') as f:
#     inputs = [line.strip() for line in f]

S = inputs[0]
print(f"Thank you, {S}, and farewell!")
exit(0)
