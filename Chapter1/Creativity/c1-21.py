# Write a program that repeatedly reads lines from standard input until EOFError is raised (via Ctrl-D) and outputs those lines in reverse order.
import sys

input_str = sys.stdin.readlines()
for i in range(len(input_str)):
    print(input_str.pop())
