import random


def primary():
    print("Keep it logically awesome.")

    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()

    # MADE VAR CALLED "last" TO HOLD ALL ELEMENTS IN THE ARRAY
    # USED THE RANDOM FUNCTION
    last = 13
    rnd = random.randint(0, last)

    print(quotes[rnd])


if __name__ == "__main__":
    primary()
