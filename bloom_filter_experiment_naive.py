import psutil
import time

start_time = time.time()
data = []
positive_count = 0
fake_count = 0
true_count = 0

with open("fake_formatted.txt", "r") as f:
    for d in f:
        fake_count += 1
        data.append(d)

with open("fake_formatted.txt", "r") as f:
    for d in f:
        if d in data:
            positive_count += 1

with open("true_formatted.txt", "r") as f:
    for d in f:
        true_count += 1
        if d in data:
            positive_count += 1

print("-"*40)
print("The number of fake news items detected is: {}".format(positive_count))
print("The false positive rate is: {0:.10f}".format((positive_count-fake_count)/true_count))
print("-"*40)
print("Running time in seconds is: {}".format((time.time() - start_time)))
print("Memory usage in MB is: {}".format(psutil.Process().memory_info().rss / (1024 * 1024)))
print("-"*40)