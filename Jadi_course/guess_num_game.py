import random


def welcome():
    print('''
    Welcome to my 'GUESS NUM' GAME.
    This game is about guessing a number choose by computer (between 1 to 20).
    G00D L0CK WITH THAT *_*
    Let's Play 🏃‍➡️
    ''')
    res = input("Enter the game's numerical range. (ex : 1,20) : ")
    n1 , n2 = map(int, res.split(','))
    return n1, n2


def win(pc, player_g):
    return pc == player_g


def get_a_guess():
    g = input(f"Guess a Number ({n1}, {n2}) : ")
    return int(g)


def answer(pc, player_g):
    if player_g < n1 or player_g > n2:
        return "Out of Range 💀"
    else:
        if player_g > pc:
            return "Try somthing smaller dude 😏"
        elif player_g < pc:
            return "Woof pick a larger num 🤨"
        return "WoW YOU WON 🏆"


def high_score(player_count, high_s):
    if high_s == 0:
        high_s = player_count
        print("Your record added.")
        return high_s

    if player_count < high_s:
        print(f'''
        DAMN !!, You are HIT the top record.
        The previous record is {high_s} try.
        NOW you with {player_count} ON the top of all records🔥
        ''')
        return player_count
    else:
        print(f'''
        Someone before you guess less then you with {high_s} guesses.
        You should try to be better✌️
        ''')
        return high_s


def finish(player_g, try_count):
    print(f"\nThe {player_g} is right and you came here with {try_count} try 😎")


def play_again():
    res = input("\nDo You want to play again ? (Y/N) : ")
    if res.upper() in ['Y', 'YES']:
        return True
    else:
        print("Good Bye 👋")
        return False


n1, n2 = welcome()

guess = 0
isPlaying = True
high_score_int = 0

while isPlaying:

    count = 0
    pc_answer = random.randint(n1, n2)

    while not win(pc_answer, guess):
        guess = get_a_guess()
        count += 1
        print(answer(pc_answer, guess))

    finish(guess, count)
    high_score_int = high_score(count, high_score_int)
    isPlaying = play_again()
