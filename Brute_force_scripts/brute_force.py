import time
import random
import string
import sys
#brute force guessing
def brute_force(solution):
	start = ''
	index = 0
	alphabet = list(string.printable)
	while start != solution:
		holder = random.choice(alphabet)
		if holder != solution[index]:
			alphabet.remove(holder)
			print(start+holder)
			time.sleep(0.05)
		else:
			alphabet = list(string.printable)
			start += holder
			print(start)
			index +=1
			time.sleep(0.05)
t0 = time.perf_counter()
brute_force(sys.argv[1])
print(time.perf_counter() -t0)
