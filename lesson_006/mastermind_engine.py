from random import randint

_NUMBER = ''


def pick_number():
    global _NUMBER
    _NUMBER = ''
    _NUMBER += str(randint(1, 9))
    i = 1
    while i <= 3:
        temp_number = str(randint(0, 9))
        if _NUMBER.find(temp_number) == -1:
            _NUMBER += temp_number
            i += 1

    print(_NUMBER)


def check_number(user_number):
    bulls_cows = {'bulls': 0, 'cows': 0}
    for key in range(4):
        if _NUMBER[key] == user_number[key]:
            bulls_cows['bulls'] += 1
            continue
        for key_user in user_number:
            if _NUMBER[key] == key_user:
                bulls_cows['cows'] += 1
    return bulls_cows


def is_gameover(bulls):
    if bulls == 4:
        return True
    else:
        return False