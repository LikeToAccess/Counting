import random
from string import digits
from tqdm import tqdm


min_length = 1000
max_length = 2000
target = 3
operations = ["+", "-", "*"]
# operations = ["+", "-", "*", "/"]
operations_no_divide = ["+", "-", "*"]


def calculate(x, y):
	operation = random.choice(operations)
	y = int(y)
	if x == 0 and operation == "/":
		operation = random.choice(operations_no_divide)

	if operation == "+":
		return x+y, (x, operation, y)
	if operation == "-":
		return x-y, (x, operation, y)
	if operation == "*":
		return x*y, (x, operation, y)
	if operation == "/":
		try:
			result = x/y, (x, operation, y)
		except ZeroDivisionError:
			return x*0, (x, "*", 0)
		while True:
			if x % y == 0:
				return result
			x, y = random.randint(1,9), random.randint(1,9)
	return x

def main():
	number = (random.randint(0,9), "+")
	history = [str(number[0])]
	for _ in range(max_length):
		number = calculate(number[0], random.choice(digits))
		operation = number[1][1]
		history.append(operation)
		history.append(str(number[1][2]))
		# print(f"{number[1][0]} {number[1][1]} {number[1][2]} = {number[0]}")
		result = "".join(history)
		if len(history) >= max_length*2+2:
			return False
		if eval(result) == target and len(history) >= min_length:
			return result
	return False


result = False
for i in tqdm(range((int(min_length/max_length)+1)*500)):
	result = main()
	if result:
		break

print(result.replace("*","*"))
print(eval(result))
