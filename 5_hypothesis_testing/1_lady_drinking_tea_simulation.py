import random

n_trials=1_000_000
succeeded = 0

for _ in range(n_trials):

   cups = list(range(8))
   true_milk_first = set(random.sample(cups, 4))
   guess_milk_first = set(random.sample(cups, 4))
   correct = len(true_milk_first & guess_milk_first)

   if correct == 4:
       succeeded += 1

print(f"\nProportion of outcomes with all 4 correct: ~{succeeded / n_trials:.4f}")
