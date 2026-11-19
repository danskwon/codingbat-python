# Logic-1: Exercise 5: sorta_sum
# Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.
# Solved. Mistake(s) made: sum is on the built-in names list from the near_hundred discussion. Naming a variable sum replaces Python’s sum() function inside this function. It doesn’t break anything here, but it will bite you once you start using sum() on lists. Use total instead.

def sorta_sum(a, b):
  total = a + b
  if 10 <= total <= 19:
    return 20
  return total


if __name__ == "__main__":
  print(sorta_sum(3, 4))    # 7
  print(sorta_sum(9, 4))    # 20
  print(sorta_sum(10, 11))  # 21