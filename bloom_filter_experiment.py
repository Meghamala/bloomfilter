import csv
import mmh3 
import math
import psutil
import random
import time

class BloomFilter:
    """
    Bloom Filter
    """
    def __init__(self, n = 10000, delta = 0.01):
        """
        n: the maximum number of insertions
        delta: false positive rate 
        """

        self.m = math.ceil((n * math.log(1/delta)) / math.log(2)**2)
        self.delta = delta
        self.n = n
        self.k = math.ceil( math.log(1/delta))
        self.filter = [0] * int(self.m) 
        self.max_128_int = (1 << 128) - 1

    def _hash(self, token, seed):
        # this is a hash functions that hashes elements to a random integer between 0 and self.m - 1
        # There is no need to modify this function
        # To generate different hash functions, use different seed
        x = mmh3.hash128(token, seed, signed=False)/self.max_128_int
        return int(x*(self.m-1))
    
    def insert(self, x):
        
        for seed in range(self.k): 
            index = self._hash(x, seed)
            self.filter[index] = 1
        return

    def membership(self, x):
       
        for seed in range(self.k):
            index = self._hash(x, seed)
            if self.filter[index] == 0:
                return False
        return True


# No need to make any modification to the code below

B = BloomFilter(n = 24000, delta = 0.05)
positive_count = 0
start_time = time.time()
fake_count = 0
true_count = 0

# insert fake news items into the bloom filter
with open("fake_formatted.txt", "r") as f:
    for d in f:
        B.insert(d)
        fake_count += 1

# test for membership of fake news items and true news items
with open("fake_formatted.txt", "r") as f:
    for d in f:
        if B.membership(d) == True:
            positive_count += 1
    
with open("true_formatted.txt", "r") as f:
    for d in f:
        true_count += 1
        if B.membership(d) == True:
            positive_count += 1


print("-"*40)
print("The number of fake news items detected is: {}".format(positive_count))
print("The false positive rate is: {0:.10f}".format((positive_count-fake_count)/true_count))
print("-"*40)
print("Running time in seconds is: {}".format((time.time() - start_time)))
print("Memory usage in MB is: {}".format(psutil.Process().memory_info().rss / (1024 * 1024)))
print("-"*40)