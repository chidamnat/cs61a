import sys

#for line in sys.stdin:
#    sys.stdout.write(' '.join(line))

def vowels(line):
    for v in 'aeiou':
        if v in line:
            yield (v, line.count(v))
