import sys


if __name__ == '__main__':
    date = str(input())
# with open('sample_data/2.in') as f:
#     date = [line.strip() for line in f][0]

reply = 'nope'
if date == 'OCT 31' or date == 'DEC 25':
    reply = 'yup'

print(reply)
exit(0)