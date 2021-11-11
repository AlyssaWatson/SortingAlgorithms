import random
from algorithms import *

randomNumbers = random.sample(range(1, 100), 20)

print(randomNumbers)
print(bubble_sort(randomNumbers))
print(bucket_sort(randomNumbers, 5))
