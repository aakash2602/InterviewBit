#!/bin/python3

import sys

def chess_move_horizontal(rQ, cQ, n, chess_board, move):
    if cQ + move == n or cQ + move < 0:
        return 0
    elif chess_board[rQ][cQ + move] == 1:
        return 0
    else:
        return 1 + chess_move_horizontal(rQ, cQ + move, n, chess_board, move)

def chess_move_vertical(rQ, cQ, n, chess_board, move):
    if rQ + move == n or rQ + move < 0:
        return 0
    elif chess_board[rQ + move][cQ] == 1:
        return 0
    else:
        return 1 + chess_move_vertical(rQ + move, cQ, n, chess_board, move)

def chess_move_across(rQ, cQ, n, chess_board, rMove, cMove):
    if rQ + rMove == n or rQ + rMove < 0 or cQ + cMove == n or cQ + cMove < 0:
        return 0
    elif chess_board[rQ + rMove][cQ + cMove] == 1:
        return 0
    else:
        return 1 + chess_move_across(rQ + rMove, cQ + cMove, n, chess_board, rMove, cMove)

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
rQueen,cQueen = input().strip().split(' ')
rQueen,cQueen = [int(rQueen),int(cQueen)]
# print (rQueen, end=" ")
# print (cQueen)
# chess_board = [[0 for j in range(n)] for i in range(n)]
chess_board = {}

for a0 in range(k):
    rObstacle,cObstacle = input().strip().split(' ')
    rObstacle,cObstacle = [int(rObstacle),int(cObstacle)]
    # your code goes here
    # chess_board[rObstacle - 1][cObstacle - 1] = 1
    if rObstacle == rQueen and cObstacle < cQueen:
        if 'horizontal_left' in chess_board:
            if chess_board['horizontal_left'][1] < cObstacle:
                chess_board['horizontal_left'] = (rObstacle, cObstacle)
        else:
            chess_board['horizontal_left'] = (rObstacle, cObstacle)
    elif rObstacle == rQueen and cObstacle > cQueen:
        if 'horizontal_right' in chess_board:
            if chess_board['horizontal_right'][1] > cObstacle:
                chess_board['horizontal_right'] = (rObstacle, cObstacle)
        else:
            chess_board['horizontal_right'] = (rObstacle, cObstacle)
    elif cObstacle == cQueen and rObstacle < rQueen:
        if 'vertical_down' in chess_board:
            if chess_board['vertical_down'][0] < rObstacle:
                chess_board['vertical_down'] = (rObstacle, cObstacle)
        else:
            chess_board['vertical_down'] = (rObstacle, cObstacle)
    elif cObstacle == cQueen and rObstacle > rQueen:
        if 'vertical_up' in chess_board:
            if chess_board['vertical_up'][0] > rObstacle:
                chess_board['vertical_up'] = (rObstacle, cObstacle)
        else:
            chess_board['vertical_up'] = (rObstacle, cObstacle)
    elif rObstacle - rQueen == cObstacle - cQueen and rObstacle - rQueen > 0:
        if 'across_I' in chess_board:
            if chess_board['across_I'][0] > rObstacle:
                chess_board['across_I'] = (rObstacle, cObstacle)
        else:
            chess_board['across_I'] = (rObstacle, cObstacle)
    elif rQueen - rObstacle == cQueen - cObstacle  and rQueen - rObstacle > 0:
        if 'across_III' in chess_board:
            if chess_board['across_III'][0] < rObstacle:
                chess_board['across_III'] = (rObstacle, cObstacle)
        else:
            chess_board['across_III'] = (rObstacle, cObstacle)
    elif rQueen - rObstacle == cObstacle - cQueen and rQueen - rObstacle > 0:
        if 'across_II' in chess_board:
            if chess_board['across_II'][0] < rObstacle:
                chess_board['across_II'] = (rObstacle, cObstacle)
        else:
            chess_board['across_II'] = (rObstacle, cObstacle)
    elif rObstacle - rQueen == cQueen - cObstacle and rObstacle - rQueen > 0:
        if 'across_IV' in chess_board:
            if chess_board['across_IV'][0] > rObstacle:
                chess_board['across_IV'] = (rObstacle, cObstacle)
        else:
            chess_board['across_IV'] = (rObstacle, cObstacle)
        
# print (chess_board)
count = 0

if 'horizontal_left' in chess_board:
    count = count + (cQueen - chess_board['horizontal_left'][1] - 1)
else:
    count = count + (cQueen - 1)
# print (count)

if 'horizontal_right' in chess_board:
    count = count + (chess_board['horizontal_right'][1] - cQueen - 1)
else:
    count = count + (n - cQueen)
# print (count)

if 'vertical_down' in chess_board:
    count = count + (rQueen - chess_board['vertical_down'][0] - 1)
else:
    count = count + (rQueen - 1)
# print (count)

if 'vertical_up' in chess_board:
    count = count + (chess_board['vertical_up'][0] - rQueen - 1)
else:
    count = count + (n - rQueen)
# print (count)

if 'across_I' in chess_board:
    # print (chess_board['across_I'])
    count = count + (chess_board['across_I'][0] - rQueen - 1)
else:
    count = count + min(n - rQueen, n - cQueen)
# print (count)

if 'across_III' in chess_board:
    # print(chess_board['across_III'])
    count = count + (rQueen - chess_board['across_III'][0] - 1)
else:
    count = count + min(rQueen - 1 , cQueen - 1)
# print (count)

if 'across_II' in chess_board:
    # print(chess_board['across_II'])
    count = count + (rQueen - chess_board['across_II'][0] - 1)
else:
    count = count + min(rQueen - 1 , n - cQueen)
# print (count)

if 'across_IV' in chess_board:
    # print(chess_board['across_IV'])
    count = count + (chess_board['across_IV'][0] - rQueen - 1)
else:
    count = count + min(n - rQueen , cQueen - 1)
    
print (count)
# count = count + chess_move_horizontal(rQueen - 1, cQueen - 1, n, chess_board, 1)
# count = count + chess_move_horizontal(rQueen - 1, cQueen - 1, n, chess_board, -1)

# count = count + chess_move_vertical(rQueen - 1, cQueen - 1, n, chess_board, 1)
# count = count + chess_move_vertical(rQueen - 1, cQueen - 1, n, chess_board, -1)

# count = count + chess_move_across(rQueen - 1, cQueen - 1, n, chess_board, 1, 1)
# count = count + chess_move_across(rQueen - 1, cQueen - 1, n, chess_board, -1, -1)

# count = count + chess_move_across(rQueen - 1, cQueen - 1, n, chess_board, 1, -1)
# count = count + chess_move_across(rQueen - 1, cQueen - 1, n, chess_board, -1, 1)

