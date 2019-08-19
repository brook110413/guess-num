import random
r = random.randint(1, 100)
count = 0
while True:
	count += 1
	num = input('請輸入數字: ')
	num = int(num)
	if r == num:
		print('你猜中了! ')
		print('這是你猜的第', count, '次')
		break
	elif r > num:
		print('比你的數字大: ')
	elif r < num:
		print('比你的數字小: ')
	print('這是你猜的第', count, '次')


