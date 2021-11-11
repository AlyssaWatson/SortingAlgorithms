import random
import timeit
from algorithms import *

imports = '''
import random
from algorithms import bubble_sort, bucket_sort
'''
testBubble = '''
randomNumbers = random.sample(range(1, 20000), 100)
bubble_sort(randomNumbers)
'''
testBucket = '''
randomNumbers = random.sample(range(1, 20000), 100)
bucket_sort(randomNumbers,5)
'''
testSorted = '''
randomNumbers = random.sample(range(1, 20000), 100)
sorted(randomNumbers)
'''

randomNumbers = random.sample(range(1, 100), 20)

print(randomNumbers)
print(bubble_sort(randomNumbers))
print("Time to sort using Bubble Sort: " + str(timeit.timeit(stmt=testBubble, setup=imports, number=10000)))
print(bucket_sort(randomNumbers, 5))
print("Time to sort using Bucket Sort: " + str(timeit.timeit(stmt=testBucket, setup=imports, number=10000)))
print(sorted(randomNumbers))
print("Time to sort using built-in sorted function: " + str(timeit.timeit(stmt=testSorted, setup=imports, number=10000)))
