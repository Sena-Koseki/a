#!/usr/bin/python3
impor sys


def tonum(s):
    try:
        return int(s)
    except:
        return float(s)

ans = 0
for line in sys.stdin:
        ans += tonum(line)

print(ans)
