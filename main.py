import random


def play():
    user = input(" 'r' for rock, 'p' for paper, 's' for scissors: ")
    ai = random.choice(['r', 'p', 's'])

    if user == ai:
        return 'It\'s a tie'
    if win(user, ai):
        return 'Yon won'

    return 'You lost'


def win(player, opponent):
    # r>s, s>p, p>s
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 's'):
        return True


print(play())