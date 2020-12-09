import random

for n in range(10):
    random_n = random.randint(1, 50)

    if not (random_n % 2):
        continue
    
    random_n_sqrt = random_n ** 2

    if random_n_sqrt > 400:
        while True:
            random_n = random.randint(1, 50)

            if not (random_n % 2):
                break
