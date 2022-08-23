import sys
sys.stdin = open('후위표기법_input.txt', 'r')

pri = {'+': 1, '-': 1, '*': 2, '/': 2}

T = int(input())
for tc in range(1, T+1):
    N = input()
    stack = []
    ans_lst = []

    for i in N:
