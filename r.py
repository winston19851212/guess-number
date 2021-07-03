import random
r = random.randint(1, 100)
while True:
	num = input('give it a nuumber')
	num = int(num)
	if num == r:
		print('yes you got it! YAYAYAYA')
		break
	elif num > r:
		print('more than the answer')
	elif num < r:
		print('less than the answer')
		
