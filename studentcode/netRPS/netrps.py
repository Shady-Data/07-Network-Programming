#!/usr/bin/env python3

# 2. (Game: rock, paper, scissors) Programming Exercise 4.17 gives a program that
# plays the rock, paper, scissors game. Revise the program to let the user play continuously until either the user or the
# computer wins more than two times.
import socket
import argparse
# import concurrent.futures
from random import randint

def start_server():
    HOST = ''
    PORT = 31373
    SIZE = 512

    ADDR = (HOST, PORT)
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    serv.bind(ADDR)
    serv.listen(5)
    conn_sock, conn_addr = serv.accept()
    net_rps(conn_sock, conn_addr, SIZE)
    serv.close()


def net_rps(p_conn, p_addr, p_buff):
    # refactor this!!!
    # Optional prompt user for best of # games, otherwise set 3
    BEST_OF = 3
    # set a games needed to win variable to be 1 more than half of the best of # games
    games_2_win = (BEST_OF // 2) + 1
    # set variables to store the # of wins
    player_wins = 0
    opponent_wins = 0
    # optional set player 2/computer opponent
    opponent = 'Computer'
    # build a ditionary containing acceptable choices
    rock_paper_scissors = {
        1 : 'rock',
        2 : 'paper',
        3 : 'scissors'
    }
    # continuously play until wins == games to win
    while player_wins < games_2_win and opponent_wins < games_2_win:
        # display current wins
        # print(f'\nCurrent Wins:\tYou: {player_wins}\t{opponent}: {opponent_wins}')
        msg = f'\nCurrent Wins:\tYou: {player_wins}\t{opponent}: {opponent_wins}\n'
        p_conn.send(msg.encode())
        # get comp choice
        comp_rps = randint(1, 3)
        # prompt user for input
        player_rps = get_player_rps(p_conn, p_addr, p_buff)
        # print the selected choices
        # print(f'You played: {rock_paper_scissors[player_rps]}\t{opponent} played: {rock_paper_scissors[comp_rps]}')
        msg = f'You played: {rock_paper_scissors[player_rps]}\t{opponent} played: {rock_paper_scissors[comp_rps]}\n'
        p_conn.send(msg.encode())
        # check for win conditions
        if comp_rps == player_rps:
            # display draw for equal choices
            # print("Draw!\nPlay Again!")
            msg = "Draw!\nPlay Again!\n"
            p_conn.send(msg.encode())
            # rock crushes scissors
        elif player_rps == 1 and comp_rps == 3 or comp_rps == 1 and player_rps == 3:
            # print('Rock crushes scissors!', end = ' ')
            msg = 'Rock crushes scissors! '
            p_conn.send(msg.encode())
            # if player played rock
            if player_rps == 1:
                # print('You Win!')
                msg = 'You Win!\n'
                p_conn.send(msg.encode())
                player_wins += 1
            # if computer played rock
            elif comp_rps == 1:
                # print(f'{opponent} Win!')
                msg = f'{opponent} Win!\n'
                p_conn.send(msg.encode())
                opponent_wins += 1
            # paper covers rock
        elif player_rps == 2 and comp_rps == 1 or comp_rps == 2 and player_rps == 1:
            # print('Paper covers rock!', end = ' ')
            msg = 'Paper covers rock! '
            p_conn.send(msg.encode())
            # if player played paper
            if player_rps == 2:
                # print('You Win!')
                msg = 'You Win!\n'
                p_conn.send(msg.encode())
                player_wins += 1
            # if computer played paper
            elif comp_rps == 2:
                # print(f'{opponent} Win!')
                msg = f'{opponent} Win!\n'
                p_conn.send(msg.encode())
                opponent_wins += 1
            # scissors cut paper
        elif player_rps == 3 and comp_rps == 2 or comp_rps == 3 and player_rps == 2:
            # print('Scissors cut paper!', end = ' ')
            msg = 'Scissors cut paper! '
            p_conn.send(msg.encode())
            # if player played scissors
            if player_rps == 3:
                # print('You Win!')
                msg = 'You Win!\n'
                p_conn.send(msg.encode())
                player_wins += 1
            # if computer played scissors
            elif comp_rps == 3:
                # print(f'{opponent} Win!')
                msg = f'{opponent} Win!\n'
                p_conn.send(msg.encode())
                opponent_wins += 1

def get_player_rps(p_conn, p_addr, p_buff):
    # prompts user for input and returns 1, 2, or 3 depending on choice
    # look into refactoring input validation
    try:
        msg = 'Enter your choice (1 = rock, 2 = paper, 3 = scissors): '
        p_conn.send(msg.encode())
        p_conn.send(token.encode))
        user_input = int(p_conn.recv(p_buff))
        if user_input not in range(1, 4):
            while user_input not in range(1, 4):
                msg = 'Invalid Choice: Enter your choice (1, 2, 3):'
                p_conn.send(msg.encode())
                user_input = int(p_conn.recv(p_buff))
    except ValueError:
        while user_input not in range(1, 4):
            if user_input.isdigit():
                user_input = int(user_input)
            elif user_input == 'rock':
                user_input = 1
            elif user_input == 'paper':
                user_input = 2
            elif user_input == 'scissors':
                user_input == 3
            else:
                msg = 'Invalid Choice: Enter your choice (1, 2, 3):'
                p_conn.send(msg.encode())
                user_input = int(p_conn.recv(p_buff))
    return user_input

def get_args():
    parser = argparse.ArgumentParser('Rock, Paper, Scissors Client/Server')
    parser.add_argument('-n', '--net', type=str,help='Network IP of the server for the client connect to (disables server start call)/runs program as client')
    return parser.parse_args()

def client_connect(p_ip):
    port = 31373
    buff = 512
    addr = (p_ip, port)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(addr)
    token = client.recv(buff)
    while True:
        user_input = input('Player > ')
        client.send(user_input.encode())



args = get_args()
if args.net:
    client_connect(args.net)
else:
    start_server()
