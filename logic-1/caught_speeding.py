# Logic-1: caught_speeding

def caught_speeding(speed, is_birthday):
    if is_birthday:
        speed -= 5
    if speed <= 60:
        return 0
    if speed <= 80:
        return 1
    return 2


if __name__ == "__main__":
    print(caught_speeding(60, False))  # expect 0
    print(caught_speeding(65, False))  # expect 1
    print(caught_speeding(65, True))   # expect 0