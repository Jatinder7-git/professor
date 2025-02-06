import random


def main():
    level = get_level()
    generate_integer(level)
    simulate_level(level)


def get_level():

    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
            else:
                print("Invalid level")
        except ValueError:
            print("Please enter a valid integer")


def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(0, 99)
        y = random.randint(0, 99)
    else:
        x = random.randint(0, 999)
        y = random.randint(0, 999)
    return x, y


def simulate_level(level):

    questions = 1
    score = 0

    while questions <= 10:
        x, y = generate_integer(level)
        count_tries = 1
        while count_tries <= 3:
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == int(x + y):
                    score += 1
                    break

                else:
                    print("EEE")
                    count_tries += 1

            except ValueError:
                print("Enter a valid integer")
                count_tries += 1

            if count_tries == 4:
                print(f"{x} + {y} = {x+y}")

        questions += 1
        if questions == 11:
            print(f"score: {score}")
            break


if __name__ == "__main()__":
    main()
