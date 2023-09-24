#!/usr/bin/env python3

seed = 19970404
a = 1103515245
c = 12345
m = 2**31

x = seed

DEBUG = False
def update_x():
    global x

    new_x = (a * x + c) % m
    x = new_x
    if DEBUG:
        print(f"DEBUG {new_x}")
    return new_x

def set_offset(n):
    x = seed
    for _ in range(n):
        update_x()

def gen_randoms(sample, fromm, to):
    for i in range(sample):
        yield update_x() % to + fromm


import statistics as stats

def print_avg(fromm, to, inc=1):
    FROM = 1
    TO = 6
    print(f"i\tavg\tdiff")
    print(21 * "=")
    for i in range(fromm, to +1, inc):
        avg = stats.mean(gen_randoms(i, FROM, TO))
        print(f"{i}\t{round(avg, 2)}\t{round(abs(3.5 - avg), 2)}")
    print()

print_avg(2, 9, 1)

print_avg(10, 99, 10)

print_avg(100, 999, 100)

print_avg(10000, 10000)



