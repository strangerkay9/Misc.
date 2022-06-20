import time
import random
import string
import sys
#all char in an array guessed in random order

def brute_force(solution):
	start = list(' ' * (len(solution)))
	alphabet = list(string.printable)
	random.shuffle(alphabet)
	index = 0
	while ''.join(start) != solution:
		for num in range(len(solution)):
			if start[num] == solution[num]:
				pass
			else:
				rand_letter = alphabet[index]
				start[num] = rand_letter
		index +=1
		print(''.join(start))
		time.sleep(0.1)

t0 = time.perf_counter()
brute_force(sys.argv[1])
print(time.perf_counter() -t0)
