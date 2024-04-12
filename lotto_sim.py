from random import randint


def check_number():
    """ Get number from user

    Try until its type is int

    """
    while True:
        try:
            checked_num = int(input("Type a number : "))
            break
        except ValueError:
            print("It's not a number!")

    return checked_num


def get_nums():
    """Collect a list of six numbers form user


    """
    user_nums = []
    for i in range(1, 7):
        while True:
            num = check_number()
            if num in user_nums:
                print("This number is already existing on the list, try again")
            else:
                if 1 <= num <= 49:
                    user_nums.append(num)
                    i += 1
                    break
                else:
                    print("This number is out of range!")
    user_nums.sort()
    return user_nums


def lotto_draw():
    """Draw six different numbers

    """
    lotto_nums = []
    for i in range(1, 7):
        while True:
            random_num = randint(1, 49)
            if random_num in lotto_nums:
                continue
            else:
                lotto_nums.append(random_num)
                i += 1
                break

    return lotto_nums


def lotto_game():
    """Main version of the simulator

    """
    print("#This is a lotto simulator!\n", "Match 3 or more numbers to win!\n")
    user_nums = get_nums()
    lotto_nums = lotto_draw()
    print(f'There are the numbers you have chosen : {user_nums}')
    print(f'There are the current lotto numbers : {lotto_nums}')
    compared_nums = len([i for i in user_nums if i in lotto_nums])
    if compared_nums > 2:
        print(f'Congratulations! You have matched {compared_nums} numbers')
    else:
        print(f'That is too bad, you have just matched {compared_nums} numbers\n', 'Maybe next tme ;))')


lotto_game()
