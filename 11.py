# June 7, 2018

"""
This problem was asked by Apple.

Implement a job scheduler which takes in a function f and
an integer n, and calls f after n milliseconds.
"""

def scheduler(f, n):
    from time import sleep
    sleep(n / 1000)
    f()

def ten_returner():
    pass

if __name__ == '__main__':
    scheduler(ten_returner, 2000)