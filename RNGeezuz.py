import random

seed_value = 42  # the seed value for the PRNG
random.seed(seed_value)  # set the seed value

# print 10 "random" numbers
for _ in range(10):
    print(random.randint(0, 100))
