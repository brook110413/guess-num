import random
r = random.randint(1, 100)
while True:
	num = input('請輸入數字: ')
	num = int(num)
	if r == num:
		print('你猜中了! ')
		break
	elif r > num:
		print('比你的數字大: ')
	elif r < num:
		print('比你的數字小: ')

