import time
def compute1():
	value_of_n = 50000
	value_of_out = 0
	for i in range(value_of_n):
		for j in range(value_of_n):
			if (i == j):
				value_of_out += i
	print(value_of_out)
def compute2():
	value_of_n = 50000
	value_of_out = 0
	for i in range(value_of_n):
		value_of_out += i
	print(value_of_out)
if __name__ == "__main__":
	start = time.time()
	compute1()
	end = time.time()
	# get the execution time
	elapsed_time = end - start
	print('Execution time:', elapsed_time, 'seconds')